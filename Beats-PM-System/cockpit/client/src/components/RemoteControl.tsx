import React, { useState, useEffect } from "react";
import { Smartphone, QrCode, X, Terminal, Loader2, Globe } from "lucide-react";
import { QRCodeSVG } from "qrcode.react";
import axios from "axios";
import { io } from "socket.io-client";
import clsx from "clsx";

const API_BASE = import.meta.env.DEV ? "http://localhost:3000" : "";
const socket = io(API_BASE);

export const RemoteControl: React.FC = () => {
  const [status, setStatus] = useState<"off" | "starting" | "live" | "error">(
    "off"
  );
  const [url, setUrl] = useState<string | null>(null);
  const [showQR, setShowQR] = useState(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchStatus = async () => {
      try {
        const res = await axios.get(`${API_BASE}/api/tunnel/status`);
        setStatus(res.data.status);
        setUrl(res.data.url);
      } catch (e) {
        console.error("Failed to fetch tunnel status");
      }
    };

    fetchStatus();

    socket.on("tunnel-status", (data) => {
      setStatus(data.status);
      setUrl(data.url);
      if (data.status === "error") {
        setError(data.error);
      } else {
        setError(null);
      }
    });

    return () => {
      socket.off("tunnel-status");
    };
  }, []);

  const toggleTunnel = async () => {
    if (status === "live" || status === "starting") {
      try {
        await axios.post(`${API_BASE}/api/tunnel/stop`);
      } catch (e) {
        console.error("Failed to stop tunnel");
      }
    } else {
      try {
        setError(null);
        await axios.post(`${API_BASE}/api/tunnel/start`);
      } catch (e: any) {
        setError(e.response?.data?.error || "Failed to start tunnel");
      }
    }
  };

  return (
    <div className="mt-4">
      <div
        className={clsx(
          "bg-white/50 rounded-2xl p-4 flex items-center justify-between border border-transparent transition-all duration-300",
          status === "live" && "border-clay-accent-success/20 shadow-sm"
        )}
      >
        <div className="flex items-center space-x-3">
          <div className="relative">
            <Smartphone
              className={clsx(
                "w-5 h-5",
                status === "live"
                  ? "text-clay-accent-success"
                  : "text-clay-muted"
              )}
            />
            {status === "live" && (
              <div className="absolute -top-1 -right-1 w-2 h-2 rounded-full bg-clay-accent-success animate-ping" />
            )}
          </div>
          <div>
            <p className="text-xs font-black text-clay-foreground/80 uppercase tracking-tighter">
              Remote Control
            </p>
            <p className="text-[10px] text-clay-muted font-bold opacity-60">
              {status === "live"
                ? "External Interface Active"
                : "Local Access Only"}
            </p>
          </div>
        </div>

        <div className="flex items-center space-x-2">
          {status === "live" && (
            <button
              onClick={() => setShowQR(true)}
              className="p-2 bg-clay-accent/10 rounded-xl text-clay-accent hover:bg-clay-accent/20 transition-colors"
              title="Show QR Code"
            >
              <QrCode className="w-4 h-4" />
            </button>
          )}
          <button
            onClick={toggleTunnel}
            disabled={status === "starting"}
            className={clsx(
              "px-3 py-1.5 rounded-xl text-[10px] font-black uppercase tracking-widest transition-all",
              status === "live"
                ? "bg-clay-accent-success/10 text-clay-accent-success hover:bg-clay-accent-success/20"
                : "bg-clay-accent/10 text-clay-accent hover:bg-clay-accent/20",
              status === "starting" && "opacity-50 cursor-not-allowed"
            )}
          >
            {status === "starting"
              ? "..."
              : status === "live"
              ? "LIVE"
              : "GO LIVE"}
          </button>
        </div>
      </div>

      {error && (
        <div className="mt-2 p-3 bg-red-50 rounded-xl border border-red-100 flex items-start space-x-2">
          <X className="w-3 h-3 text-red-500 mt-0.5 shrink-0" />
          <p className="text-[10px] text-red-600 font-bold leading-tight">
            {error}
          </p>
        </div>
      )}

      {/* QR Modal */}
      {showQR && (
        <div className="fixed inset-0 z-[100] flex items-center justify-center p-6 bg-black/60 backdrop-blur-md">
          <div className="bg-white rounded-[40px] p-8 max-w-sm w-full shadow-2xl relative overflow-hidden">
            <div className="absolute top-0 left-0 w-full h-2 bg-gradient-to-r from-clay-accent via-clay-accent-secondary to-clay-accent-tertiary" />

            <button
              onClick={() => setShowQR(false)}
              className="absolute top-6 right-6 p-2 bg-gray-100 rounded-full text-gray-400 hover:text-gray-600 transition-colors"
            >
              <X className="w-5 h-5" />
            </button>

            <div className="text-center mb-8">
              <div className="w-16 h-16 bg-clay-accent/10 rounded-3xl flex items-center justify-center mx-auto mb-4">
                <Globe className="w-8 h-8 text-clay-accent" />
              </div>
              <h3 className="font-display font-black text-2xl text-clay-foreground tracking-tight">
                Mobile Brain Link
              </h3>
              <p className="text-sm text-clay-muted font-medium px-4 mt-2">
                Scan this code to control your Brain Mesh from any mobile
                device.
              </p>
            </div>

            <div className="bg-gray-50 p-6 rounded-[32px] mb-6 flex justify-center border border-gray-100 relative group">
              {url ? (
                <QRCodeSVG
                  value={url}
                  size={200}
                  level="H"
                  includeMargin={false}
                  className="rounded-xl"
                />
              ) : (
                <div className="w-[200px] h-[200px] flex items-center justify-center">
                  <Loader2 className="w-8 h-8 text-clay-accent animate-spin" />
                </div>
              )}

              <div className="absolute inset-0 bg-clay-accent/5 opacity-0 group-hover:opacity-100 transition-opacity rounded-[32px] pointer-events-none" />
            </div>

            <div className="space-y-4">
              <div className="bg-clay-accent/5 p-4 rounded-2xl border border-clay-accent/10">
                <p className="text-[10px] font-black text-clay-accent uppercase tracking-widest mb-1">
                  Interface URL
                </p>
                <p className="text-xs font-mono text-clay-foreground truncate break-all opacity-80 select-all">
                  {url}
                </p>
              </div>

              <p className="text-[10px] text-center text-clay-muted font-bold uppercase tracking-widest opacity-40">
                Secured by Cloudflare Tunnel
              </p>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};
