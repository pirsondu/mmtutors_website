function showTutorFields(val) {
    const tutorType = val;
    const subjectFields = document.getElementById('subjectChoices');
    const languageFields = document.getElementById('languageChoices');

    if (tutorType === 'subject') {
        subjectFields.classList.remove('hidden');
        languageFields.classList.add('hidden');
    } else if (tutorType === 'language') {
        subjectFields.classList.add('hidden');
        languageFields.classList.remove('hidden');
    } else {
        subjectFields.classList.add('hidden');
        languageFields.classList.add('hidden');
    }
}

function addslot() {
    const div = document.createElement('div');
    div.classList.add('d-flex')
    div.classList.add('mb-3')

    const inputDay = document.createElement('input');
    inputDay.classList.add('form-control')
    inputDay.classList.add('mr-2')
    inputDay.placeholder = 'Day (e.g., Monday)'
    inputDay.type = 'text'
    console.log("FINDING NAME")
    inputDay.name = "timeslot"
    div.appendChild(inputDay)

    const inputStart = document.createElement('input');
    inputStart.classList.add('form-control')
    inputStart.classList.add('mr-2')
    inputStart.name = 'timeslot';
    inputStart.placeholder = 'From (e.g., 1:00 PM)'
    inputStart.type = 'text'
    div.appendChild(inputStart)
    

    const inputEnd = document.createElement('input');
    inputEnd.classList.add('form-control')
    inputEnd.name = 'timeslot';
    inputEnd.classList.add('mr-2')
    inputEnd.placeholder = 'To (e.g., 3:00 PM)'
    inputEnd.type = 'text'
    div.appendChild(inputEnd)

    const btnRemove = document.createElement('button');
    btnRemove.classList.add('btn')
    btnRemove.classList.add('btn-decrease')
    btnRemove.type = 'button'
    btnRemove.innerHTML = '-'
    // btnRemove.onclick = 'removeslot()'
    btnRemove.setAttribute("onclick","removeslot(this)");

    div.appendChild(btnRemove)
    // <button class="btn btn-decrease" type="button" onclick="removeslot()">-</button>

    document.getElementById('ava').appendChild(div)

}

function removeslot(_this) {
    $(_this).parent().remove();
}