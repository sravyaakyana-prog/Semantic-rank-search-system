import { useEffect, useState } from "react";
import API from "../services/api";
import Navbar from "../components/Navbar";

export default function Evaluation() {
  const [metrics, setMetrics] = useState(null);
  const [loading, setLoading] = useState(false);

  const loadEvaluation = async () => {
    try {
      setLoading(true);
      const res = await API.get("/api/evaluate");
      setMetrics(res.data);
    } catch (err) {
      console.error("Evaluation Error:", err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadEvaluation();
  }, []);

  return (
    <div className="min-h-screen bg-gradient-to-b from-slate-950 via-slate-900 to-black text-white">
      <div className="max-w-6xl mx-auto px-4 sm:px-6 py-8 sm:py-12">
        <Navbar />

        <h1 className="text-3xl font-bold mb-3">📊 Retrieval Evaluation</h1>
        <p className="text-slate-400 mb-8">
          BM25 vs Semantic vs Hybrid vs Reranker performance on SciFact.
        </p>

        {loading && <div className="text-cyan-300">Running evaluation...</div>}

        {metrics && (
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            {Object.entries(metrics).map(([key, value]) => (
              <div
                key={key}
                className="rounded-2xl border border-white/10 bg-white/5 p-5"
              >
                <div className="text-xs text-slate-400">{key}</div>
                <div className="text-2xl font-bold text-cyan-300 mt-2">
                  {String(value)}
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}