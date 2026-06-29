import { motion } from "framer-motion";

export default function AnswerCard({ data, loading }) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 18 }}
      animate={{ opacity: 1, y: 0 }}
      className="rounded-2xl border border-cyan-400/20 bg-cyan-500/10 backdrop-blur-xl p-6"
    >
      <div className="flex justify-between mb-3">
        <h2 className="text-white font-semibold">🤖 Evidence-Based Answer</h2>

        {loading && (
          <span className="text-xs text-cyan-300 animate-pulse">
            thinking...
          </span>
        )}
      </div>

      <div className="text-gray-200 text-sm leading-relaxed whitespace-pre-wrap min-h-[60px]">
        {loading && !data?.answer ? (
          <div className="space-y-2">
            <div className="h-3 bg-white/10 rounded animate-pulse" />
            <div className="h-3 bg-white/10 rounded w-5/6 animate-pulse" />
          </div>
        ) : (
          data?.answer
        )}
      </div>

      {data?.expanded_query && (
        <div className="mt-4 text-xs text-slate-400">
          Expanded query:{" "}
          <span className="text-cyan-300">{data.expanded_query}</span>
        </div>
      )}
    </motion.div>
  );
}