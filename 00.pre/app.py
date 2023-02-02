from flask import Flask, render_template

# 웹 서버 역할 Flask APP 생성
app = Flask(__name__)

# 라우팅 설정
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/page')
def page():
    return render_template('page.html')

if __name__ == "__main__":
    app.run()