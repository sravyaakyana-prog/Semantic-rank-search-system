const express = require("express");

const Search = require("../models/Search");
const auth = require("../middleware/auth");

const router = express.Router();

/* Save Search */

router.post("/", auth, async (req, res) => {
  try {
    const search = await Search.create({
      userId: req.user.id,
      query: req.body.query,
    });

    res.json(search);
  } catch (err) {
    console.error(err);

    res.status(500).json({
      message: "Server Error",
    });
  }
});

/* Get User Searches */

router.get("/", auth, async (req, res) => {
  try {
    const searches = await Search.find({
      userId: req.user.id,
    })
      .sort({ createdAt: -1 })
      .limit(10);

    res.json(searches);
  } catch (err) {
    console.error(err);

    res.status(500).json({
      message: "Server Error",
    });
  }
});

module.exports = router;