const express = require("express");
const semanticSearch = require("../services/mlService");

const router = express.Router();

router.post("/", async (req, res) => {
  try {
    const { query } = req.body;

    const results = await semanticSearch(query);

    res.json(results);
  } catch (error) {
    console.error(error);

    res.status(500).json({
      message: "Search failed",
    });
  }
});

module.exports = router;