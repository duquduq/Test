import os
from flask import Flask
#수정했어용 3:56
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, Render!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # PORT 환경 변수를 사용
    app.run(host="0.0.0.0", port=port)        # 0.0.0.0으로 설정해 외부 접근 허용
