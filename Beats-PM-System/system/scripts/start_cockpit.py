import os
import subprocess
import platform
import sys
import signal
import time

def print_cyan(text): print(f"\033[96m{text}\033[0m")
def print_green(text): print(f"\033[92m{text}\033[0m")
def print_yellow(text): print(f"\033[93m{text}\033[0m")

# Paths
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
SERVER_DIR = os.path.join(ROOT, "Beats-PM-System", "cockpit", "server")
CLIENT_DIR = os.path.join(ROOT, "Beats-PM-System", "cockpit", "client")

processes = []

def signal_handler(sig, frame):
    print_yellow("\n🛑 Shutting down Antigravity Cockpit...")
    for p in processes:
        p.terminate()
    sys.exit(0)

def run_npm(directory, command):
    system = platform.system()
    npm_cmd = "npm.cmd" if system == "Windows" else "npm"
    
    # Check if node_modules exists, if not, install
    if not os.path.exists(os.path.join(directory, "node_modules")):
        print_cyan(f"📦 Installing dependencies in {os.path.basename(directory)}...")
        subprocess.run([npm_cmd, "install"], cwd=directory, check=True)

    print_cyan(f"🚀 Running 'npm run {command}' in {os.path.basename(directory)}...")
    return subprocess.Popen([npm_cmd, "run", command], cwd=directory)

def main():
    signal.signal(signal.SIGINT, signal_handler)
    
    print_cyan("--- Antigravity Cockpit Launcher v1.0 ---")
    
    try:
        # Start Server
        server_p = run_npm(SERVER_DIR, "dev")
        processes.append(server_p)
        
        # Start Client
        client_p = run_npm(CLIENT_DIR, "dev")
        processes.append(client_p)
        
        print_green("\n✅ Cockpit is launching!")
        print_green("   Backend: http://localhost:3000")
        print_green("   Frontend: http://localhost:5173")
        print_yellow("\nPress CTRL+C to stop both services.")
        
        while True:
            time.sleep(1)
            
    except Exception as e:
        print(f"❌ Launch failed: {e}")
        signal_handler(None, None)

if __name__ == "__main__":
    main()
