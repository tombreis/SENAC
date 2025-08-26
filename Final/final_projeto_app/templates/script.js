document.addEventListener('DOMContentLoaded', () => {
    const botoesAdicionar = document.querySelectorAll('.adicionar-carrinho');
    const contadorCarrinho = document.getElementById('contador-carrinho');
    let totalItens = 0;

    botoesAdicionar.forEach(botao => {
        botao.addEventListener('click', () => {
            totalItens++;
            contadorCarrinho.textContent = totalItens;
            alert('Item adicionado ao carrinho!');
        });
    });
});