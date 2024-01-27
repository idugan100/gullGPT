//import from 
messages=[]
document.addEventListener("DOMContentLoaded", render_messages)
function insertNewChat(event){
    event.preventDefault();
    let formData = new FormData(event.target);
  
    let inputValue = formData.get('message');
    messages.push({"user":inputValue})
    let input = document.getElementById("message");
    input.value=""
    render_message(messages[messages.length -1])
    chat_model()
}


function chat_model(){
    console.log("query llm")
    messages.push({"ai":"ai response"})
    render_message(messages[messages.length -1])
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
            span.classList.add( "px-2", "py-2", "mt-2", "mb-2", "rounded-b-xl", "rounded-tr-xl", "w-1/3",  "loading:animate-pulse");
            div.classList.add("bg-[#8A0000]", "px-2", "py-2", "rounded-b-xl", "rounded-tl-xl", "mb-2", "mt-2", "w-1/3", "text-white", "shadow-[#FFC31F]/25","shadow-md", "loading:animate-bounce")
        }
        chatHolder.appendChild(div);
        div.appendChild(span);
}