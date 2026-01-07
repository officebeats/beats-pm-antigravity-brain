import { spawn, ChildProcess } from "child_process";
import path from "path";
import fs from "fs";

export class TunnelManager {
  private process: ChildProcess | null = null;
  private url: string | null = null;
  private status: "off" | "starting" | "live" | "error" = "off";

  private getBinaryPath(): string {
    const isWindows = process.platform === "win32";
    if (isWindows) {
      const commonPaths = [
        path.join(
          process.env.PROGRAMFILES || "C:\\Program Files",
          "cloudflared",
          "cloudflared.exe"
        ),
        path.join(
          process.env["PROGRAMFILES(X86)"] || "C:\\Program Files (x86)",
          "cloudflared",
          "cloudflared.exe"
        ),
      ];
      for (const p of commonPaths) {
        if (fs.existsSync(p)) return p;
      }
    }
    return "cloudflared"; // Default to PATH
  }

  async start(port: number): Promise<string> {
    if (this.process) {
      await this.stop();
    }

    this.status = "starting";
    const binary = this.getBinaryPath();

    return new Promise((resolve, reject) => {
      // Use ephemeral tunnel (no account needed)
      this.process = spawn(binary, [
        "tunnel",
        "--url",
        `http://localhost:${port}`,
      ]);

      let resolved = false;

      this.process.stderr?.on("data", (data) => {
        const output = data.toString();
        // Regex to find the Cloudflare tunnel URL
        const urlMatch = output.match(
          /https:\/\/[a-z0-9-]+\.trycloudflare\.com/i
        );

        if (urlMatch && !resolved) {
          this.url = urlMatch[0];
          this.status = "live";
          resolved = true;
          resolve(this.url);
        }
      });

      this.process.on("error", (err: any) => {
        if (err.code === "ENOENT") {
          this.status = "error";
          if (!resolved) {
            reject(
              new Error("cloudflared not found. Please install cloudflared.")
            );
          }
        }
      });

      this.process.on("exit", () => {
        this.status = "off";
        this.url = null;
        this.process = null;
      });

      // Timeout if it takes too long
      setTimeout(() => {
        if (!resolved && this.status === "starting") {
          this.stop();
          reject(new Error("Tunnel startup timed out."));
        }
      }, 30000);
    });
  }

  async stop(): Promise<void> {
    if (this.process) {
      this.process.kill();
      this.process = null;
    }
    this.url = null;
    this.status = "off";
  }

  getStatus() {
    return {
      status: this.status,
      url: this.url,
    };
  }
}
