const container = document.querySelector('.container')
const botao = document.querySelector('#botao')
let botao_bool = false


function on_off(){
    container.classList.toggle('on')

    if(botao_bool) {
        botao.textContent = "LUMOS"
        botao_bool = false
    } else {
        botao.textContent = "NOX"
        botao_bool = true
    }
}

