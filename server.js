import express from "express";
import { pinyin } from "pinyin-pro";

const app = express();

app.get("/pinyin", (req, res) => {
  const text = req.query.text || "";
  const result = pinyin(text, {
    toneType: "num", // "num" (ni3 hao3), "mark" (nǐ hǎo), "none"
    type: "array"    // trả về mảng
  });
  res.json({ input: text, pinyin: result });
});

const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Pinyin API running on port ${port}`);
});
