const axios = require("axios");

const ML_URL = process.env.ML_SERVICE_URL || "http://127.0.0.1:8000/search";

async function semanticSearch(query) {
  try {
    const response = await axios.post(
      ML_URL,
      { 
        query,
        top_k: 10
      },
      {
        timeout: 120000, // 2 minutes for CrossEncoder first load
      }
    );

    return response.data;
  } catch (error) {
    console.error("ML Service Error:", error.message);

    if (error.response) {
      console.error("ML Status:", error.response.status);
      console.error("ML Data:", error.response.data);
    }

    return {
      answer: "Search service unavailable",
      results: [],
      latency_ms: 0,
      documents_searched: 0,
      returned_results: 0,
    };
  }
}

module.exports = semanticSearch;