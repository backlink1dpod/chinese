from flask import Flask, request, jsonify
from pypinyin import pinyin, Style
import pycantonese

app = Flask(__name__)

@app.route("/convert", methods=["GET"])
def convert():
    text = request.args.get("text", "")
    
    # Mandarin Pinyin
    mandarin = " ".join(
        ["".join(x) for x in pinyin(text, style=Style.TONE3, heteronym=False)]
    )
    
    # Cantonese Jyutping
    try:
        jy_list = pycantonese.characters_to_jyutping(text)
        jyutping = " ".join([t[1] for t in jy_list if t[1]])
    except Exception as e:
        jyutping = ""
    
    return jsonify({
        "input": text,
        "pinyin": mandarin,
        "jyutping": jyutping
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
