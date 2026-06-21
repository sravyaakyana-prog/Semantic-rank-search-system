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

// Auth
app.use("/api/auth", authRoutes);

// Search History
app.use("/api/history", searchHistoryRoutes);

// Semantic Search Route
app.use(
  "/api/semantic-search",
  semanticSearchRoutes
);

/* =========================
   Health Check
========================= */

app.get("/", (req, res) => {
  res.json({
    message: "Backend Running",
  });
});

/* =========================
   Legacy Search Endpoint
========================= */

app.post("/api/search", async (req, res) => {
  try {
    const response = await axios.post(
      `${process.env.ML_SERVICE}/search`,
      {
        query: req.body.query,
      }
    );

    res.json(response.data);
  } catch (error) {
    console.error(error);

    res.status(500).json({
      error: "Search failed",
    });
  }
});

/* =========================
   Start Server
========================= */

const PORT = process.env.PORT || 5000;

app.listen(PORT, () => {
  console.log(
    `🚀 Server running on port ${PORT}`
  );
});