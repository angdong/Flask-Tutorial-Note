from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

# login, logout, sign-up 페이지의 url정의하기
# route 함수에 추가적인 url을 작성하여 분기를 만들어준다
@auth.route('/sign-in')
def sign_in():
    # 함수에 인자를 넣어서 원하는 값을 추가하기
    return render_template('sign_in.html' ,user="SemiCircle")

@auth.route('/logout')
def logout():
    return render_template('logout.html')

@auth.route('/sign-up')
def sign_up():
    return render_template('sign_up.html')