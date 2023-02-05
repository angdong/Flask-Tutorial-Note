const deleteNote = function (noteId){
    console.log('삭제할 메모 id ${noteId}');

    // 전달할 데이터 정보(메모 정보)
    let note = {
        noteId : noteId
    }

    // 삭제 ajax
    fetch('/delete-note',{
        method: 'POST',
        body: JSON.stringify(note),
        headers: {
            "Content-Type": "application/json"
        },
    }).then((response) => response.json())
    .then(() => {
        window.location.href = '/';
    })
}

// 상수 및 변수
const modal = new bootstrap.Modal('#updateNoteModal'); // 메모 수정 모달
let updateNoteId; // 현재 수정 중인 메모

// 메모 수정 모달 호출 함수
const showUpdateNoteModal = function(noteId){
    console.log(`현재 클릭된 메모 id ${noteId}`);

    // 현재 수정할 메모 반영
    updateNoteId = noteId;

    // Modal show
    modal.show();
}

const updateNote = function(){
    // 현재 수정할 메모의 제목과 내용 불러오기
    let updateTitle = document.querySelector('#update-title');
    let updateContent = document.querySelector('#update-content');

    // 전달할 데이터 정보(수정 메모 정보)
    let note = {
        noteId: updateNoteId,
        title: updateTitle.value,
        content: updateContent.value,
    }
    console.log(note);
    // 수정 ajax
    fetch('/update-note',{
        method: 'PUT',
        body: JSON.stringify(note),
        headers: {
            "Content-Type": "application/json"
        },
    }).then((response) => response.json())
    .then(() =>{
        window.location.href = '/';
    });
}