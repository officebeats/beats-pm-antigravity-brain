import { useState } from "react";
import { Sidebar } from "./components/Sidebar";
import { UploadZone } from "./components/UploadZone";
import { ChatInterface } from "./components/ChatInterface";
import { StatusPanel } from "./components/StatusPanel";
import { Brain } from "lucide-react";
import ReactMarkdown from "react-markdown";
import axios from "axios";
import { useEffect } from "react";

function App() {
  const [currentView, setCurrentView] = useState("Dashboard");
  const [kernelContent, setKernelContent] = useState("");
  const [stats, setStats] = useState({
    entities: 0,
    storagePercent: "0",
    activeProjects: 0,
  });

  const API_BASE = import.meta.env.DEV ? "http://localhost:3000" : "";

  useEffect(() => {
    const fetchKernel = async () => {
      try {
        const res = await axios.get(`${API_BASE}/api/kernel`);
        setKernelContent(res.data.content);
      } catch (e) {
        console.error("Kernel fetch failed");
      }
    };
    const fetchStats = async () => {
      try {
        const res = await axios.get(`${API_BASE}/api/stats`);
        setStats(res.data);
      } catch (e) {
        console.error("Stats fetch failed");
      }
    };
    fetchKernel();
    fetchStats();
    const interval = setInterval(fetchStats, 5000); // Polling stats
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="flex min-h-screen relative overflow-hidden font-sans selection:bg-clay-accent/20">
      {/* 1. Animated Background Blobs */}
      <div className="fixed inset-0 pointer-events-none -z-10 overflow-hidden">
        <div className="clay-blob w-[50vh] h-[50vh] bg-clay-accent/10 top-[-10%] left-[-10%] animate-clay-float" />
        <div className="clay-blob w-[60vh] h-[60vh] bg-clay-accent-secondary/10 bottom-[-10%] right-[-10%] animate-clay-float-delayed" />
        <div className="clay-blob w-[40vh] h-[40vh] bg-clay-accent-tertiary/10 top-[20%] right-[20%] animate-clay-float-slow" />
      </div>

      {/* 2. Main Layout */}
      <Sidebar currentView={currentView} setView={setCurrentView} />

      <main className="flex-1 flex flex-col h-screen overflow-hidden relative z-10 p-4 lg:p-8">
        {/* Compact Header */}
        <header className="flex flex-col md:flex-row justify-between items-center gap-2 mb-6 shrink-0 px-2 lg:px-4">
          <div className="flex items-center gap-4">
            <div className="bg-white/80 p-2 rounded-2xl shadow-sm border border-white/50 backdrop-blur-md">
              <Brain className="w-8 h-8 text-clay-accent animate-pulse" />
            </div>
            <div>
              <h2 className="font-display font-black text-3xl lg:text-5xl text-clay-foreground tracking-tighter">
                Beats{" "}
                <span className="text-transparent bg-clip-text bg-gradient-to-r from-clay-accent via-clay-accent-secondary to-clay-accent-tertiary">
                  Antigravity Brain
                </span>
              </h2>
              <div className="flex items-center gap-2 mt-1">
                <div className="relative flex h-2 w-2">
                  <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-clay-accent-success opacity-75"></span>
                  <span className="relative inline-flex rounded-full h-2 w-2 bg-clay-accent-success"></span>
                </div>
                <span className="text-[10px] font-black uppercase tracking-[0.2em] text-clay-muted">
                  Neural Mesh Active
                </span>
              </div>
            </div>
          </div>
          <div className="hidden md:flex items-center gap-6">
            <div className="text-right">
              <p className="text-[10px] font-black text-clay-muted uppercase tracking-widest opacity-40">
                Session Efficiency
              </p>
              <p className="text-sm font-bold text-clay-foreground">98.2%</p>
            </div>
            <div className="h-10 w-[1px] bg-clay-accent/10" />
            <button
              onClick={() => setCurrentView("Dashboard")}
              className="bg-clay-accent text-white px-6 py-2.5 rounded-2xl font-bold shadow-clay-button hover:scale-105 active:scale-95 transition-all text-sm"
            >
              Quick Query
            </button>
          </div>
        </header>

        {/* Compact Bento Layout */}
        <div className="flex-1 grid grid-cols-1 lg:grid-cols-12 gap-6 overflow-hidden min-h-0">
          {/* Main Hero: Dynamic View based on state */}
          <div className="lg:col-span-8 flex flex-col gap-6 overflow-hidden min-h-0">
            {currentView === "Dashboard" && (
              <>
                <div className="flex-1 min-h-0 transform transition-all duration-500 hover:scale-[1.005]">
                  <ChatInterface />
                </div>
                <div className="shrink-0 transform transition-all duration-500 hover:scale-[1.005]">
                  <UploadZone />
                </div>
              </>
            )}

            {currentView === "Action Plan" && (
              <div className="flex-1 overflow-y-auto glass-card rounded-[32px] p-8 custom-scrollbar bg-white/40 backdrop-blur-md">
                <StatusPanel />
              </div>
            )}

            {currentView === "System Logic" && (
              <div className="flex-1 overflow-y-auto glass-card rounded-[32px] p-8 custom-scrollbar bg-white/40 backdrop-blur-md">
                <div className="prose prose-sm max-w-none text-clay-foreground">
                  <ReactMarkdown>{kernelContent}</ReactMarkdown>
                </div>
              </div>
            )}
          </div>

          {/* Right Panel: Stats (Spans 4 cols) */}
          <div className="lg:col-span-4 flex flex-col gap-6 overflow-y-auto lg:overflow-visible pr-2 lg:pr-0 scrollbar-hide">
            {/* Stat Card 1 - Compact */}
            <div className="bg-gradient-to-br from-clay-accent to-clay-accent-secondary rounded-3xl shadow-clay-card p-6 text-white relative overflow-hidden group shrink-0">
              <div className="relative z-10">
                <p className="text-white/60 font-black text-[10px] uppercase tracking-[0.2em] mb-1">
                  Total Entities
                </p>
                <h3 className="font-display font-black text-4xl tracking-tighter">
                  {stats.entities.toString().padStart(2, "0")}
                </h3>
              </div>
              <div className="absolute top-0 right-0 w-24 h-24 bg-white/10 rounded-full -translate-y-1/2 translate-x-1/2 blur-2xl" />
            </div>

            {/* Stat Card 2 - Compact */}
            <div className="glass-card rounded-3xl p-6 relative overflow-hidden group shrink-0">
              <div className="flex justify-between items-start mb-2">
                <p className="text-clay-muted font-black text-[10px] uppercase tracking-[0.2em] opacity-60">
                  Neural Density
                </p>
                <span className="text-clay-accent-success font-black text-[9px] px-1.5 py-0.5 bg-clay-accent-success/10 rounded-md">
                  CONNECTED
                </span>
              </div>

              <div className="flex items-baseline space-x-1 mb-4">
                <h3 className="font-display font-black text-3xl text-clay-foreground tracking-tighter">
                  {stats.storagePercent}
                </h3>
                <span className="text-sm font-black text-clay-accent/40 tracking-tighter">
                  %
                </span>
              </div>

              <div className="w-full bg-gray-100/50 h-2 rounded-full overflow-hidden p-0.5 shadow-inner">
                <div
                  className="h-full bg-gradient-to-r from-clay-accent to-clay-accent-tertiary rounded-full transition-all duration-1000"
                  style={{ width: `${stats.storagePercent}%` }}
                />
              </div>
            </div>

            {/* Action Plan Status - Compacted inside scroll area or height-aware */}
            {currentView !== "Action Plan" && (
              <div className="flex-1 min-h-0 overflow-y-auto custom-scrollbar">
                <StatusPanel />
              </div>
            )}

            {/* Intelligence Tip - Hidden on small height or last */}
            <div className="hidden xl:block bg-clay-accent-tertiary/5 border border-clay-accent-tertiary/10 rounded-3xl p-6 shrink-0">
              <p className="text-clay-foreground/70 font-medium text-xs leading-relaxed">
                <span className="text-clay-accent-tertiary font-bold">
                  Tip:
                </span>{" "}
                Use the <span className="font-bold">#vibe</span> command to
                check system health.
              </p>
            </div>
          </div>
        </div>
      </main>
    </div>
  );
}

export default App;
