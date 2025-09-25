from flask import Flask, request, jsonify
import pypinyin
from jyutping import get_jyutping

app = Flask(__name__)

@app.route("/convert")
def convert():
    text = request.args.get("text", "")
    if not text:
        return jsonify({"error": "no text provided"}), 400

    # Mandarin Pinyin
    pinyin_list = pypinyin.lazy_pinyin(text, style=pypinyin.Style.TONE3)
    pinyin = " ".join(pinyin_list)

    # Cantonese Jyutping
    jyutping_list = [get_jyutping(char) or "" for char in text]
    jyutping = " ".join(jyutping_list)

    return jsonify({
        "input": text,
        "pinyin": pinyin,
        "jyutping": jyutping
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
