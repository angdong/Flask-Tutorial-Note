from flask import Blueprint, render_template

views = Blueprint('views', __name__) # flas.Blueprint를 가져온다

# 뷰를 정의해서 보여질 페이지와 경로를 정의하기
@views.route('/') # url의 끝부분(end-point)를 인자로 입력
def home():
    # url 접속시에 템플릿(html)들을 되돌려주도록 만들기
    return render_template('home.html') # 클라이언트 요청에 응답할 데이터를 return 시키는 함수 생성하기