const axios = require("axios");

const ML_URL = "http://127.0.0.1:8000/search";

async function semanticSearch(query) {
  try {
    const response = await axios.post(
      ML_URL,
      { query }
    );

    return response.data;
  } catch (error) {
    console.error("ML Service Error:", error.message);

    return {
      answer: "Search service unavailable",
      results: [],
    };
  }
}

module.exports = semanticSearch;