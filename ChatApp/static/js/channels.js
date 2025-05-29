// static/js/channels.js
<<<<<<< HEAD
=======
// 1. DOM 要素の取得
>>>>>>> 019d0d6212a8e47b742d33f85094e8889a820abc
const form  = document.querySelector('#inviteform');
const input = document.querySelector('#channelName');
const ul    = document.querySelector('#invitedList');

/**
 * 新しい <li> を作って返す
 * @param {number} teamId      チームID（固定でもOK）
 * @param {number} channelId   チャンネルID（Date.now() で仮生成）
 * @param {string} channelName チャンネル名
 */
<<<<<<< HEAD
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
=======

// 2. 保存済みチャンネルの復元
let channels = JSON.parse(localStorage.getItem('channels') || '[]');
channels.forEach(ch => {
  ul.appendChild(createLi(ch.teamId, ch.id, ch.name));
})

// 3. <li> を組み立てるヘルパー関数 
function createLi(teamId, channelId, channelName) {
  const li = document.createElement('li');

  // チャンネルへのリンクを作成
  const a = document.createElement('a');
  a.textContent = channelName; // リンクテキスト
  a.href        = `/channels/${teamId}/messages/${channelId}`;// 遷移先URL
  a.classList.add('channel-link');

  // 編集／削除ボタン 
  const editBtn   = document.createElement('button');
  editBtn.textContent   = 'edit';
  const removeBtn = document.createElement('button');
  removeBtn.textContent = 'remove';

  // 一度にまとめて <li> に追加
  li.append(a, editBtn, removeBtn);

  // 後で配列を検索しやすいように dataset に ID を保存
  li.dataset.channelId = channelId;
  li.dataset.teamId = teamId;
  return li;
}

// 4. フォーム送信時の処理
form.addEventListener('submit', event => {
  event.preventDefault(); // ページ再読み込みを防ぐ
  const name = input.value.trim(); // 前後スペースを除去
>>>>>>> 019d0d6212a8e47b742d33f85094e8889a820abc
  if (!name) {
    alert('Enter the name please!');
    return;
  }

  // 仮のID生成（本番はサーバーから返ってくるIDを使う）
<<<<<<< HEAD
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
=======
  const newId = Date.now();
  const teamId = 1;  // 今は固定、将来はサーバーから

  // 画面に反映
  const li = createLi(teamId, newId, name);
  ul.appendChild(li);

  // localStorageに保存
  channels.push({ teamId, id: newId, name });
  localStorage.setItem('channels', JSON.stringify(channels));

  input.value = '';　 // 入力欄をクリア
});

// 5. 編集／削除ボタンのイベント処理
ul.addEventListener('click', event => {
  if (event.target.tagName !== 'BUTTON') return;
  const btn = event.target;
  const li  = btn.closest('li');
  const channelId = Number(li.dataset.channelId);

  if (btn.textContent === 'remove') {

    // 削除
    ul.removeChild(li);
    channels = channels.filter(ch => ch.id !== channelId);
    localStorage.setItem('channels', JSON.stringify(channels));

    
  } else if (btn.textContent === 'edit') {

    // 編集モードに切り替え 
    const a = li.querySelector('a');
    const inp = document.createElement('input');
    inp.type  = 'text';
    inp.value = a.textContent;

    // hrefを保存しておく
    inp.dataset.href = a.href;
    li.replaceChild(inp, a);
    btn.textContent = 'save';

  } else {

    // 保存モードに切り替え 
    const inp  = li.querySelector('input[type="text"]');
    const newName = inp.value.trim() || '(無題)';
    const aNew = document.createElement('a');
    aNew.textContent = newName;
    aNew.href = inp.dataset.href;
    aNew.classList.add('channel-link');
    li.replaceChild(aNew, inp);
    btn.textContent = 'edit';

     // 状態も更新
     const ch = channels.find(ch => ch.id === channelId);
    if (ch) {
      ch.name = newName;
      localStorage.setItem('channels', JSON.stringify(channels));
    }
>>>>>>> 019d0d6212a8e47b742d33f85094e8889a820abc
  }
});