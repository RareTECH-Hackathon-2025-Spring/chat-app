    const form = document.querySelector('#inviteform')
    const input = document.querySelector('input')
    const ul = document.querySelector('#invitedList')


    function createLi() {
        const li = document.createElement('li');
        const span = document.createElement('span');
        span.textContent = input.value;
        const label = document.createElement('label');
        // label.textContent = 'confirmed';
        const checkbox = document.createElement('input');
        // checkbox.type = "checkbox";
        const editBtn = document.createElement('button');
        editBtn.textContent = 'edit';
        const removeBtn  = document.createElement('button')
        removeBtn.textContent = 'remove';


        li.appendChild(span);
        li.appendChild(label);
        // label.appendChild(checkbox);
        li.appendChild(editBtn);
        li.appendChild(removeBtn);

        return li;
    }

    form.addEventListener('submit', (event) => {
        event.preventDefault();

        const li = createLi();

        if(input.value === '') {
            alert('Enter the name please!')
        } else {
            ul.appendChild(li);
        }
    });

    // 2 Add resopnded class

    ul.addEventListener('change', (event) => {
        const checkbox = event.target;
        const checked = checkbox.checked;
        const li = checkbox.parentNode.parentNode;
            if(checked) {
                li.className = 'responded';
            }   else {
                li.className = '';
            }
    });

    // 3 button aciton

    ul.addEventListener('click', event => {
    if (event.target.tagName !== 'BUTTON') return;

    const button = event.target;
    const li     = button.closest('li');

    if (button.textContent === 'remove') {

        // 削除
        li.remove();
    } else if (button.textContent === 'edit') {

        // 編集開始
        const span = li.querySelector('span');
        const inputTxt = document.createElement('input');
        inputTxt.type = 'text'
        inputTxt.value = span.textContent;
        li.replaceChild(inputTxt, span);
        button.textContent = 'save';
    } else if(button.textContent === 'save') {

        // 編集保存
        const inputTxt = li.querySelector('input[type="text"]');
        const spanNew = document.createElement('span');
        spanNew.textContent = inputTxt.value;
        li.replaceChild(spanNew, inputTxt);
        button.textContent = 'edit';
        }
    });