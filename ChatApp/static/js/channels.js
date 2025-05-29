// static/js/channels.js
const form  = document.querySelector('#inviteform');
const input = document.querySelector('#channelName');
const ul    = document.querySelector('#invitedList');

/**
 * 新しい <li> を作って返す
 * @param {number} teamId      チームID（固定でもOK）
 * @param {number} channelId   チャンネルID（Date.now() で仮生成）
 * @param {string} channelName チャンネル名
 */
function createLi(teamId, channelId, channelName) {
  const li = document.createElement('li');

  // ——— チャンネルリンク ———
  const a = document.createElement('a');
  a.textContent = channelName;
  a.href        = `/channels/${teamId}/messages/${channelId}`;
  a.classList.add('channel-link');

  // ——— 編集／削除ボタン ———
  const editBtn   = document.createElement('button');
  editBtn.textContent   = 'edit';
  const removeBtn = document.createElement('button');
  removeBtn.textContent = 'remove';

  // <li> にまとめて追加
  li.append(a, editBtn, removeBtn);
  return li;
}

// ——— フォーム送信時 ———
form.addEventListener('submit', event => {
  event.preventDefault();
  const name = input.value.trim();
  if (!name) {
    alert('Enter the name please!');
    return;
  }

  // 仮のID生成（本番はサーバーから返ってくるIDを使う）
  const fakeChannelId = Date.now();
  const li = createLi(1, fakeChannelId, name);

  ul.appendChild(li);
  input.value = '';
});

// ——— edit/remove ボタンのハンドリング ———
ul.addEventListener('click', event => {
  if (event.target.tagName !== 'BUTTON') return;
  
  const btn = event.target;
  const li  = btn.closest('li');

  if (btn.textContent === 'remove') {
    li.remove();
  } else if (btn.textContent === 'edit') {
    const a   = li.querySelector('a');
    const inp = document.createElement('input');
    inp.type  = 'text';
    inp.value = a.textContent;
    li.replaceChild(inp, a);
    btn.textContent = 'save';
  } else { // save
    const inp  = li.querySelector('input[type="text"]');
    const aNew = document.createElement('a');
    aNew.textContent = inp.value;
    // href を再設定（必要なら）
    aNew.href = inp.previousElementSibling.href;
    li.replaceChild(aNew, inp);
    btn.textContent = 'edit';
  }
});