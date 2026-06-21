import { motion } from "framer-motion";

export default function DocumentCard({ doc, index }) {
  const isTop = index === 0;

  const rawScore = doc.score ?? doc.semantic_score ?? 0;
  const normalized = rawScore > 1 ? rawScore / 100 : rawScore;
  const percent = Math.min(100, Math.max(0, normalized * 100));

  return (
    <motion.div
      initial={{ opacity: 0, y: 15 }}
      animate={{ opacity: 1, y: 0 }}
      whileHover={{ scale: 1.02 }}
      transition={{ duration: 0.25, delay: index * 0.05 }}
      className={`relative rounded-2xl border p-5 backdrop-blur-xl overflow-hidden
        transition-all duration-200
        ${
          isTop
            ? "bg-cyan-500/10 border-cyan-400/50 shadow-cyan-500/20"
            : "bg-white/5 border-white/10"
        }`}
    >
      {/* glow */}
      {isTop && (
        <div className="absolute inset-0 bg-cyan-400/10 blur-2xl opacity-40" />
      )}

      <div className="relative flex justify-between items-center mb-3">
        <div className="flex items-center gap-2">
          <span className="text-xs text-gray-300">#{index + 1}</span>

          {isTop && (
            <span className="text-[10px] px-2 py-0.5 rounded-full bg-cyan-500/20 text-cyan-300 border border-cyan-400/40">
              Top Evidence
            </span>
          )}
        </div>

        <span className="text-xs text-green-400 font-semibold">
          {normalized.toFixed(3)}
        </span>
      </div>

      <div className="text-white text-sm font-medium mb-2">
        {doc.docid}
      </div>

      <div className="text-gray-300 text-xs line-clamp-3">
        {doc.doc_text}
      </div>

      {/* progress */}
      <div className="mt-4">
        <div className="h-1 bg-white/10 rounded-full overflow-hidden">
          <motion.div
            initial={{ width: 0 }}
            animate={{ width: `${percent}%` }}
            transition={{ duration: 0.5, delay: index * 0.05 }}
            className={`h-full ${
              isTop ? "bg-cyan-400" : "bg-green-400"
            }`}
          />
        </div>

        <div className="flex justify-between text-[10px] text-gray-500 mt-1">
          <span>relevance</span>
          <span>{percent.toFixed(0)}%</span>
        </div>
      </div>
    </motion.div>
  );
}