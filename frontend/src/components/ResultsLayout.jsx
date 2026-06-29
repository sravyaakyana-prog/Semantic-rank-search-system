import { motion } from "framer-motion";
import AnswerCard from "./AnswerCard";
import DocumentCard from "./DocumentCard";

export default function ResultsLayout({ data, loading }) {
  return (
    <div className="space-y-8">
      <motion.div initial={{ opacity: 0, y: 18 }} animate={{ opacity: 1, y: 0 }}>
        <AnswerCard data={data} loading={loading} />
      </motion.div>

      <div className="grid grid-cols-2 md:grid-cols-4 gap-3">
        <Stat label="Latency" value={`${data?.latency_ms ?? 0} ms`} />
        <Stat label="Docs searched" value={data?.documents_searched ?? 0} />
        <Stat label="Returned" value={data?.returned_results ?? 0} />
        <Stat label="Confidence" value={`${data?.confidence ?? 0}%`} />
      </div>

      <div className="h-px bg-white/10" />

      <div className="space-y-4">
        <h2 className="text-white text-lg font-semibold">
          📚 Ranked Evidence
        </h2>

        {data?.results?.map((doc, index) => (
          <DocumentCard key={index} doc={doc} index={index} />
        ))}
      </div>
    </div>
  );
}

function Stat({ label, value }) {
  return (
    <div className="rounded-xl border border-white/10 bg-white/5 p-4">
      <div className="text-xs text-slate-400">{label}</div>
      <div className="text-white font-semibold mt-1">{value}</div>
    </div>
  );
}