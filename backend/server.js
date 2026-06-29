const express = require("express");
const cors = require("cors");
const axios = require("axios");
const mongoose = require("mongoose");

require("dotenv").config();

const authRoutes = require("./routes/auth");
const searchHistoryRoutes = require("./routes/searchHistory");
const semanticSearchRoutes = require("./routes/semanticSearch");

const app = express();

/* =========================
   MongoDB Connection
========================= */

mongoose
  .connect(process.env.MONGO_URI)
  .then(() => {
    console.log("✅ MongoDB Connected");
  })
  .catch((err) => {
    console.error("❌ MongoDB Connection Failed");
    console.error(err);
  });

/* =========================
   Middleware
========================= */

app.use(cors());
app.use(express.json());

/* =========================
   Routes
========================= */

app.use("/api/auth", authRoutes);
app.use("/api/history", searchHistoryRoutes);
app.use("/api/semantic-search", semanticSearchRoutes);

/* =========================
   Health Check
========================= */

app.get("/", (req, res) => {
  res.json({
    message: "Backend Running",
  });
});

/* =========================
   ML Search Endpoint
========================= */

app.post("/api/search", async (req, res) => {
  try {
    const response = await axios.post(
      `${process.env.ML_SERVICE}/search`,
      {
        query: req.body.query,
        top_k: req.body.top_k || 10,
      },
      {
        timeout: 120000,
      }
    );

    res.json(response.data);
  } catch (error) {
    console.error("Search Error:", error.message);

    res.status(500).json({
      error: "Search failed",
      details: error.message,
    });
  }
});

/* =========================
   ML Evaluation Endpoint
========================= */

app.get("/api/evaluate", async (req, res) => {
  try {
    const response = await axios.get(
      `${process.env.ML_SERVICE}/evaluate`,
      {
        timeout: 300000,
      }
    );

    res.json(response.data);
  } catch (error) {
    console.error("Evaluation Error:", error.message);

    res.status(500).json({
      error: "Evaluation failed",
      details: error.message,
    });
  }
});

/* =========================
   Start Server
========================= */

const PORT = process.env.PORT || 5000;

app.listen(PORT, () => {
  console.log(`🚀 Server running on port ${PORT}`);
});