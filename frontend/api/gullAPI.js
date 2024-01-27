//import from 

function loading() {
    if (message) {
        return true;
    }
    return false;
}

function pushNewMessage() {
    if (message == user){
        loading(message)
    }
    else if (message == bot){
        loading(message)
    }
}

function sendMessage() {
    
}