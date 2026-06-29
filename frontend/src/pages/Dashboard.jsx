import { useState, useEffect } from "react";
import API from "../services/api";

import Navbar from "../components/Navbar";
import Hero from "../components/Hero";
import SearchBar from "../components/SearchBar";
import LoadingState from "../components/LoadingState";
import ResultsLayout from "../components/ResultsLayout";

import {
  getHistory,
  saveHistory,
} from "../services/historyService";

export default function Dashboard() {
  const [query, setQuery] = useState("");
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [loadingText, setLoadingText] = useState("");
  const [history, setHistory] = useState([]);

  useEffect(() => {
    loadHistory();
  }, []);

  const loadHistory = async () => {
    try {
      const data = await getHistory();

      setHistory(
        data.map((item) => item.query)
      );
    } catch (err) {
      console.error("History Load Error:", err);
    }
  };

  const search = async () => {
    if (!query.trim()) return;

    setLoading(true);
    setData(null);

    try {
      setLoadingText("Analyzing Query...");

      setTimeout(
        () => setLoadingText("Generating Embeddings..."),
        400
      );

      setTimeout(
        () => setLoadingText("Ranking Documents..."),
        900
      );

      setTimeout(
        () => setLoadingText("Extracting Answer..."),
        1400
      );

      const res = await API.post(
        "/api/search",
        {
          query,
        }
      );

      setData(res.data);

      try {
        await saveHistory(query);
        await loadHistory();
      } catch (historyErr) {
        console.error("History Save Error:", historyErr);
      }

    } catch (err) {
      console.error("Search Error:", err);
      alert("Search failed. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-b from-slate-950 via-slate-900 to-black text-white relative overflow-hidden">

      <div className="absolute inset-0 bg-cyan-500/5 blur-3xl opacity-30 pointer-events-none" />

      <div className="max-w-6xl mx-auto px-4 sm:px-6 py-8 sm:py-12 relative">

        <Navbar />

        <div className="space-y-10 mt-8">

          {!data && <Hero />}

          <SearchBar
            query={query}
            setQuery={setQuery}
            onSearch={search}
            loading={loading}
          />

          {history.length > 0 && (
            <div>
              <h3 className="text-slate-400 mb-3 text-sm">
                Recent Searches
              </h3>

              <div className="flex flex-wrap gap-2">
                {history.map((item, idx) => (
                  <button
                    key={idx}
                    onClick={() => setQuery(item)}
                    className="px-3 py-1 rounded-full text-xs bg-white/5 border border-white/10 hover:scale-105 hover:border-cyan-400 transition-all duration-200 active:scale-95"
                  >
                    {item}
                  </button>
                ))}
              </div>
            </div>
          )}

          {loading && (
            <LoadingState
              loadingText={loadingText}
            />
          )}

          {data && (
            <ResultsLayout
              data={data}
              loading={loading}
            />
          )}

        </div>
      </div>
    </div>
  );
}