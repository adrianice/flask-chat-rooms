window.onload = function(){
    const socket = io()
    const connectingMessage = document.querySelector('#connecting')
    const sendButton = document.querySelector('#send-message')
    const chatDiv = document.querySelector('#chat')
    const messageInput = document.querySelector('#message')
    
    messageInput.addEventListener('keydown', (event)=>{
        if(event.key === 'Enter'){
            if(!event.shiftKey){
                sendMessage()
                event.preventDefault()
            }
        }
    })

    function getDate(){
        let date = new Date()

        let offset = -420

        let adjustedDate = new Date(date.getTime() + offset * 60 * 1000)

        let year = adjustedDate.getUTCFullYear()
        let month = ('0' + (adjustedDate.getUTCMonth() + 1)).slice(-2)
        let day = ('0' + adjustedDate.getUTCDate()).slice(-2)

        let formattedDate = year + '-' + month + '-' + day

        return formattedDate
    }

    function sendMessage(){
        let message = messageInput.value.trim()
        if(message != ""){
            socket.emit('send-message', {'message': message})
        }
        messageInput.value = ""
    }

    sendButton.onclick = ()=>{
        sendMessage()
    }

    function scrollToBottom(){
        let card = document.querySelector('#chat')
        card.scrollTop = card.scrollHeight
    }

    function resetChat(){
        chatDiv.innerHTML = ''
    }

    function putMessage(userid, username, message, date, time){
        if(getDate() == date){
            date = 'Today'
        }

        if(userid != user_id){
            chatDiv.insertAdjacentHTML('beforeend',
            `<div class="row my-2">
            <div class="col-lg-12">
                <div class="card card-body w-75 p-2">
                    <h4 class=>${username}</h4>
                    <p class="my-0">${message}</p>
                </div>
            </div>
            <p>${date} ${time}</p>
        </div>`)
        }
        else{
            chatDiv.insertAdjacentHTML('beforeend', 
            `<div class="row my-2">
            <div class="col-lg-12 d-flex flex-column align-items-end">
                <div class="card card-body w-75 p-2 text-end align-self-end">
                    <h4 class=>Me</h4>
                    <p class="my-0">${message}</p>
                </div>
            </div>
            <p class="text-end">${date} ${time}</p>
        </div>`)
        }

        scrollToBottom()
    }
    
    socket.on('connect', ()=>{
        connectingMessage.style.display = 'none'
    })

    socket.on('disconnect', ()=>{
        connectingMessage.style.display = 'block'
    })

    socket.on('recieve_message', (data)=>{
        putMessage(data.id_user, data.username, data.message, data.date, data.time)
    })

    socket.on('receive-all-messages', (data) => {
        resetChat()
        jsonData = JSON.parse(data)
        for(let i = 0; i < jsonData.length; i++){
            putMessage(jsonData[i][0], jsonData[i][1], jsonData[i][2], jsonData[i][3], jsonData[i][4])
        }
    })

    
    scrollToBottom()
}