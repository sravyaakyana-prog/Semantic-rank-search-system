import { motion } from "framer-motion";

import AnswerCard from "./AnswerCard";
import InsightsPanel from "./InsightsPanel";
import DocumentCard from "./DocumentCard";

export default function ResultsLayout({ data, loading }) {
  return (
    <div className="space-y-8 sm:space-y-10">

      {/* ANSWER */}
      <motion.div
        initial={{ opacity: 0, y: 18 }}
        animate={{ opacity: 1, y: 0 }}
      >
        <AnswerCard answer={data?.answer} loading={loading} />
      </motion.div>

      <div className="h-px bg-white/10" />

      {/* INSIGHTS */}
      <motion.div
        initial={{ opacity: 0, y: 18 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.05 }}
      >
        <InsightsPanel
          semanticNdcg={data?.semantic_ndcg}
          bm25Ndcg={data?.bm25_ndcg}
          improvement={data?.improvement}
          loading={loading}
        />
      </motion.div>

      <div className="h-px bg-white/10" />

      {/* DOCUMENTS */}
      <div className="space-y-4">
        <h2 className="text-white text-lg font-semibold">
          📚 Ranked Documents
        </h2>

        {data?.results?.map((doc, index) => (
          <DocumentCard
            key={index}
            doc={doc}
            index={index}
          />
        ))}
      </div>
    </div>
  );
}