import os
from flask import Flask, render_template
#수정해써 4:06
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")  # index.html 템플릿을 렌더링

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
