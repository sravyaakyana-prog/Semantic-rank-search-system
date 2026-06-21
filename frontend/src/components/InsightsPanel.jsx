import { motion } from "framer-motion";

export default function InsightsPanel({
  semanticNdcg,
  bm25Ndcg,
  improvement,
  loading,
}) {
  return (
    <motion.div
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      className="grid grid-cols-1 md:grid-cols-3 gap-4"
    >
      <div className="p-4 rounded-xl bg-white/5 border border-white/10">
        <p className="text-sm text-gray-400">Semantic NDCG</p>
        <p className="text-xl text-green-400">
          {loading ? "..." : semanticNdcg?.toFixed(3) || "0.000"}
        </p>
      </div>

      <div className="p-4 rounded-xl bg-white/5 border border-white/10">
        <p className="text-sm text-gray-400">BM25 NDCG</p>
        <p className="text-xl text-yellow-400">
          {loading ? "..." : bm25Ndcg?.toFixed(3) || "0.000"}
        </p>
      </div>

      <div className="p-4 rounded-xl bg-white/5 border border-white/10">
        <p className="text-sm text-gray-400">Improvement</p>
        <p className="text-xl text-blue-400">
          {loading ? "..." : improvement ? `${improvement.toFixed(2)}%` : "0%"}
        </p>
      </div>
    </motion.div>
  );
}