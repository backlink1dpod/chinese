import express from "express";
import { pinyin } from "pinyin-pro";

const app = express();
const PORT = process.env.PORT || 3000;

app.get("/convert", (req, res) => {
  const text = req.query.text || "";
  if (!text) {
    return res.status(400).json({ error: "Missing ?text= query parameter" });
  }

  const result = pinyin(text, { toneType: "symbol" });
  res.json({ text, pinyin: result });
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
