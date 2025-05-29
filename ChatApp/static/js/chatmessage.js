// 1. DOM 要素の取得
const userSelectorBtn = document.querySelector('#user-selector') //11行目
const user2SelectorBtn = document.querySelector('#user2-selector') //12行目
const chatHeader = document.querySelector('.chat-header') //15行目
const chatMessages = document.querySelector('.chat-messages') //17行目
const chatInputForm = document.querySelector('.chat-input-form') //30行目
const chatInput = document.querySelector('.chat-input') //31行目
const clearChatBtn = document.querySelector('.clear-chat-button') //34行目

const messages = JSON.parse(localStorage.getItem('messages')) || []

// •document：今開いている HTMLページ全体
// •querySelector('#'または’.')：その中から、id が user-selector の要素を1つ取得
// •const userSelectorBtn：取得した要素を userSelectorBtn という変数に入れて記憶

//--------------------------------------------------------------------------------------------\\

// 2.メッセージ要素を返す関数の作成 18~27行目メッセージ要素として存在
// userまたはuser2が各メッセージに対して、18~27行目のメッセージ要素を作成
//名前、メッセージ、タイムスタンプを取得、この関数を作成して、毎回入力する必要を省く。

const createChatMessageElement = (message) => `
    <div class="message ${message.sender == 'user' ? 'blue-bg' : 'gray-bg'}">
        <div class="message-sender">${message.sender}</div>
        <div class="message-text">${message.text}</div>
        <div class="message-timestamp">${message.timestamp}</div>
        </div>
        `
// アロー関数（message というオブジェクトを受け取る）戻り値はテンプレート文字列（HTML）
// `${message.sender == 'user' ? 'blue-bg' : 'gray-bg'}`
// 三項演算子でクラス名を切り替えてる → sender が "user" のときは blue-bg クラス（自分のメッセージ）→ それ以外なら gray-bg クラス（相手のメッセージ）
// ${message.sender}, ${message.text}, ${message.timestamp} メッセージの送信者・本文・タイムスタンプを埋め込んでいる

// --------------------------------------------------------------------------------------------------------------------\\

// 3.メッセージ送信関数を作成

window.onload = () => {
    messages.forEach((message) => {
        chatMessages.innerHTML += createChatMessageElement(message)
  })
}

//チャットしているユーザーの表示切り替え(<h2>)
let messageSender = 'user'

const updateMessageSender = (name) => {
    messageSender = name
    chatHeader.innerText = `${messageSender} chattting...`
    chatInput.placeholder = `Type here, ${messageSender}`

        // ユーザー切り替えボタンをクリックすると色が切り替わる
        if (name === 'user') {
            userSelectorBtn.classList.add('active-person')
            user2SelectorBtn.classList.remove('active-person')
        }
        if (name === 'user2') {
            user2SelectorBtn.classList.add('active-person')
            userSelectorBtn.classList.remove('active-person')
        }

        chatInput.focus()
}

userSelectorBtn.onclick = () => updateMessageSender('user')
user2SelectorBtn.onclick = () => updateMessageSender('user2')


// 関数でイベントの引数を渡します。リロードアクションを制御します
 const sendMessage = (e) => {
    e.preventDefault()
    

    // タイムスタンプの取得
    const timestamp = new Date().toLocaleString('en-US', { hour: 'numeric', minute: 'numeric', hour12: true})
    const message = {
       sender: messageSender,
       text: chatInput.value,
       timestamp,



    //1.new Date()　現在の日時を表す JavaScript の Date オブジェクトを生成します。
    //2.toLocaleString('en-US', { hour: 'numeric', minute: 'numeric', hour12: true })生成した Date オブジェクトを、指定したロケール（ここではアメリカ英語）とオプションで文字列に変換します。
    //3.const timestamp = … 上記で得られた時刻文字列を変数 timestamp に格納します。
    //4.const message = { … } メッセージ情報をまとめたオブジェクトリテラルを定義し、変数 message に代入します。
    //5.後続処理へ）こうして作成した message オブジェクトを、画面への表示やサーバ送信など、チャット機能の次のステップに渡して使います。
    }

        messages.push(message)
        localStorage.setItem('messages', JSON.stringify(messages))
        chatMessages.innerHTML += createChatMessageElement(message)


    // チャットを送信すると最新のメッセージを表示してくれる
    chatInputForm.reset()
    chatMessages.scrollTop = chatMessages.scrollHeight
}

chatInputForm.addEventListener('submit', sendMessage)

clearChatBtn.addEventListener('click',() => {
    localStorage.clear()
    chatMessages.innerHTML = ''
})
    