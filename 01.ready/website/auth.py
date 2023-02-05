from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash # 해싱
from flask_login import login_user, login_required, logout_user, current_user
from .models import User # User model 가져오기
from . import db

auth = Blueprint('auth', __name__)

# login, logout, sign-up 페이지의 url정의하기
# route 함수에 추가적인 url을 작성하여 분기를 만들어준다
@auth.route('/sign-in', methods=['GET', 'POST'])
def sign_in():
    # 가입된 유저 정보 가져오기
    if request.method == 'POST':
        email = request.form.get('email')
        password1 = request.form.get('password1')
        
        # Search User in database & compare password
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password1):
                flash('로그인 완료', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('비밀번호가 다릅니다', category='error')
        else:
            flash('해당 이메일 정보가 없습니다', category='error')
    # 함수에 인자를 넣어서 원하는 값을 추가하기
    return render_template('sign_in.html' ,user="SemiCircle")

@auth.route('/logout')
@login_required # login 필요하기 때문
def logout():
    # return render_template('logout.html')
    # 로그아웃을 여러 번 안하기 때문
    logout_user()
    return redirect(url_for('auth.sign_in'))

@auth.route('/sign-up', methods=['GET', 'POST']) # GET: 웹 자원 조회 POST: 웹 자원 생성
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        nickname = request.form.get('nickname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        # 유효성 검사
        user = User.query.filter_by(email=email).first()
        if user:
            flash("이미 가입된 이메일입니다.", category='error')
        elif len(email) < 5:
            flash("이메일은 5자 이상이어야 합니다.", category="error")
        elif len(nickname) < 2:
            flash("닉네임은 2자 이상이어야 합니다", category="error")
        elif password1 != password2:
            flash("비밀번호와 비밀번호재입력이 서로 다릅니다.", category="error")
        elif len(password1) < 7:
            flash("비밀번호가 너무 짧습니다.", category="error")
        else:
            # 회원가입 시 DB에 저장될 데이터 구성 가져오기
            new_user = User(
                email=email, 
                nickname=nickname, 
                password=generate_password_hash(password1, method='sha256') # password 해싱하기
            )
            # db에 회원가입 정보 저장
            db.session.add(new_user) # 생성한 User인스턴스 추가하기
            db.session.commit() # 임시상태인 db -> commit 해서 최종 반영하기
            db.session.commit()
            
            # auto-login
            login_user(new_user, remember=True)
            
            flash("회원가입 완료.", category="success")
            """
            * render_template -> Forward
            * redirect() -> Redirect
                Forward로 POST를 처리하면 새로고침시 같은 요청이 반복됨
                Redirect로 처리하면 POST로 처리한 결과를 GET을 통하여 조회화면으로 이동되도록 Redirect시킨다
            """
            return redirect(url_for('views.home'))
    return render_template('sign_up.html')