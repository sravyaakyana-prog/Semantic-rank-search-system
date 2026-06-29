import { motion } from "framer-motion";

function formatScore(value) {
  if (value === undefined || value === null) return "0.000";
  return Number(value).toFixed(3);
}

export default function DocumentCard({ doc, index }) {
  const isTop = index === 0;

  const rerank = Number(doc.rerank_score ?? 0);
  const percent = Math.min(100, Math.max(0, (1 / (1 + Math.exp(-rerank))) * 100));

  return (
    <motion.div
      initial={{ opacity: 0, y: 15 }}
      animate={{ opacity: 1, y: 0 }}
      whileHover={{ scale: 1.02 }}
      transition={{ duration: 0.25, delay: index * 0.05 }}
      className={`relative rounded-2xl border p-5 backdrop-blur-xl overflow-hidden transition-all duration-200 ${
        isTop
          ? "bg-cyan-500/10 border-cyan-400/50 shadow-cyan-500/20"
          : "bg-white/5 border-white/10"
      }`}
    >
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
          {percent.toFixed(0)}%
        </span>
      </div>

      <div className="text-white text-sm font-medium mb-2">
        {doc.title || doc.docid}
      </div>

      <div className="text-gray-300 text-xs line-clamp-3">
        {doc.doc_text}
      </div>

      <div className="grid grid-cols-2 md:grid-cols-4 gap-2 mt-4">
        <Score label="Semantic" value={doc.semantic_score} />
        <Score label="BM25" value={doc.bm25_score} />
        <Score label="Hybrid" value={doc.hybrid_score} />
        <Score label="Rerank" value={doc.rerank_score} />
      </div>
    </motion.div>
  );
}

function Score({ label, value }) {
  return (
    <div className="rounded-lg bg-black/20 border border-white/10 px-3 py-2">
      <div className="text-[10px] text-slate-500">{label}</div>
      <div className="text-xs text-cyan-300 font-semibold">
        {formatScore(value)}
      </div>
    </div>
  );
}