from flask import Blueprint, render_template, request

auth = Blueprint('auth', __name__)

# login, logout, sign-up 페이지의 url정의하기
# route 함수에 추가적인 url을 작성하여 분기를 만들어준다
@auth.route('/sign-in', methods=['GET', 'POST'])
def sign_in():
    # 함수에 인자를 넣어서 원하는 값을 추가하기
    return render_template('sign_in.html' ,user="SemiCircle")

@auth.route('/logout')
def logout():
    return render_template('logout.html')

@auth.route('/sign-up', methods=['GET', 'POST']) # GET: 웹 자원 조회 POST: 웹 자원 생성
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        nickname = request.form.get('nickname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        if len(email) < 5:
            pass
        elif len(nickname) < 2:
            pass
        elif password1 != password2:
            pass
        elif len(password1) < 7:
            pass
        else:
            pass # create user -> DB
    return render_template('sign_up.html')