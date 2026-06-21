import { motion } from "framer-motion";

export default function AnswerCard({ answer, loading }) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 18 }}
      animate={{ opacity: 1, y: 0 }}
      className="rounded-2xl border border-white/10 bg-white/5 backdrop-blur-xl p-6"
    >
      <div className="flex justify-between mb-3">
        <h2 className="text-white font-semibold">🤖 AI Answer</h2>

        {loading && (
          <span className="text-xs text-cyan-300 animate-pulse">
            thinking...
          </span>
        )}
      </div>

      <div className="text-gray-200 text-sm leading-relaxed whitespace-pre-wrap min-h-[60px]">
        {loading && !answer ? (
          <div className="space-y-2">
            <div className="h-3 bg-white/10 rounded animate-pulse" />
            <div className="h-3 bg-white/10 rounded w-5/6 animate-pulse" />
          </div>
        ) : (
          answer
        )}
      </div>
    </motion.div>
  );
}