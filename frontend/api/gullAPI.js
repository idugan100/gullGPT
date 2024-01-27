//import from 
messages=[]
function insertNewChat(event){
    event.preventDefault();
    let formData = new FormData(event.target);
  
    let inputValue = formData.get('message');
    messages.push({"user":inputValue})
    loading_state()
    render_message(messages[messages.length -1])
    chat_model()
}

async function chat_model(){
    url="http://127.0.0.1:8000/su/invoke"
    const response = await fetch(url, {
        method: 'POST', // HTTP POST method
        headers: {
          'Content-Type': 'application/json' // Specify content type as JSON
        },
        body: JSON.stringify({
            "input": messages[messages.length -1].user,
            "config": {},
            "kwargs": {}
          })
    })
    const responseData = await response.json(); // Parse the response body as JSON
    messages.push({"ai":responseData.output})
    render_message(messages[messages.length -1])
    end_loading_state()
}

function render_message(element){
    let chatHolder = document.getElementById("chatHolder")

        let div = document.createElement("div");
        let span = document.createElement("span");
    
        if(element.hasOwnProperty("user")){
            span.textContent=element.user
            span.classList.add("bg-gray-300", "px-2", "py-2", "mt-2", "mb-2", "rounded-b-xl", "rounded-tr-xl", "w-1/3", "shadow-[#FFC31F]/25", "shadow-lg", "loading:animate-pulse");
            div.classList.add("flex", "flex-col" ,"items-end")
        }
        else{
            span.textContent=element.ai
            span.classList.add( "px-2", "py-2", "mt-2", "mb-2", "rounded-b-xl", "rounded-tr-xl", "w-1/2",  "loading:animate-pulse");
            div.classList.add("bg-[#8A0000]", "px-2", "py-2", "rounded-b-xl", "rounded-tl-xl", "mb-2", "mt-2", "w-1/2", "text-white", "shadow-[#FFC31F]/25","shadow-md", "loading:animate-bounce")
        }
        chatHolder.appendChild(div);
        div.appendChild(span);
}

function clear_conversation(){
    messages=[]
    let chatHolder = document.getElementById("chatHolder")
    chatHolder.innerHTML=""
}

function loading_state(){
    let input = document.getElementById("message");
    input.value=""
    let inputBar=document.getElementById("inputBar")
    inputBar.classList.add("animate-bounce")
    input.disabled=true
    input.placeholder="Loading response ..."
}

function end_loading_state(){
    let input = document.getElementById("message");
    let inputBar=document.getElementById("inputBar")
    inputBar.classList.remove("animate-bounce")
    input.disabled=false
    input.placeholder="Type here ..."
}