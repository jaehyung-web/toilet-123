from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>화장실 센서 모니터링 시스템</h1><p>정상 작동 중입니다.</p>'

if __name__ == '__main__':
    app.run(debug=True)
