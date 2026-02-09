import dotenv from "dotenv";

/* 👇 FORCE dotenv to read .env from project root */
dotenv.config({ path: "../.env" });

import express from "express";
import cors from "cors";
import axios from "axios";

const app = express();
app.use(cors());
app.use(express.json());

const OPENWEATHER_API_KEY = process.env.OPENWEATHER_API_KEY;

// console.log("API KEY:", OPENWEATHER_API_KEY); // should NOT be undefined

/* 🔹 CITY AUTOCOMPLETE */
app.get("/cities", async (req, res) => {
  const query = req.query.q;

  if (!query) return res.json([]);

  if (!OPENWEATHER_API_KEY) {
    return res.status(500).json({ error: "API key missing" });
  }

  try {
    const response = await axios.get(
      `https://api.openweathermap.org/geo/1.0/direct?q=${encodeURIComponent(
        query
      )}&limit=5&appid=${OPENWEATHER_API_KEY}`
    );

    const cities = response.data.map(c => ({
      name: `${c.name}, ${c.country}`
    }));

    res.json(cities);
  } catch (error) {
    console.error("Geo API error:", error.response?.data || error.message);
    res.status(500).json([]);
  }
});

/* 🔹 NODE → PYTHON */
app.post("/recommend", async (req, res) => {
  try {
    const response = await axios.post(
      "http://localhost:5000/predict",
      { city: req.body.city }
    );

    res.json(response.data);
  } catch (error) {
    console.error("Python API error:", error.message);
    res.status(500).json({
      error: "Python agent not responding"
    });
  }
});

app.listen(3000, () => {
  console.log("🌐 Node server running at http://localhost:3000");
});
