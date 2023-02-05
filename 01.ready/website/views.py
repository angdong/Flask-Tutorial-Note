from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db

views = Blueprint('views', __name__) # flask.Blueprint를 가져온다

# 뷰를 정의해서 보여질 페이지와 경로를 정의하기
@views.route('/', methods=['GET', 'POST']) # url의 끝부분(end-point)를 인자로 입력
@login_required # 로그인 여부에 따른 뷰의 분기 작업을 위함
def home():
    # POST: 메모 생성
    if request.method == "POST":
        title = request.form.get('note-title')
        content = request.form.get('note-content')
        
        if len(title) < 1 or len(content) < 1:
            flash("제목 또는 내용이 없습니다", category = "error")
        elif len(title) > 50:
            flash("제목이 너무 깁니다. 50자 이내", category="error")
        elif len(content) > 2000:
            flash("내용이 너무 깁니다. 2000자 이내", category="error")
        else:
            # note 인스턴스 생성 -> DB에 저장
            new_note = Note(title=title, content=content, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            
            flash("메모 생성 완료", category="success")
            # 메모 계속 생성되는 것을 방지하기 위함
            return redirect(url_for('views.home'))
    
    # url 접속시에 템플릿(html)들을 되돌려주도록 만들기
    return render_template('home.html') # 클라이언트 요청에 응답할 데이터를 return 시키는 함수 생성하기

# 메모 삭제 기능
@views.route('delete-note', methods=['POST'])
def delete_note():
    # POST : 메모 삭제
    if request.method == "POST":
        note = request.get_json()
        note_id = note.get('noteId')
        
        select_note = Note.query.get(note_id)
        if select_note:
            if select_note.user_id == current_user.id:
                db.session.delete(select_note)
                db.session.commit()
        return jsonify({})