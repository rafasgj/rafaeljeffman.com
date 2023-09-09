function show_answer(element) {
    document.querySelector(`#pergunta_${element}`).style.display = "none";
    document.querySelector(`#resposta_${element}`).style.display = "inline";
}
function hide_answer(element) {
    document.querySelector(`#pergunta_${element}`).style.display = "inline";
    document.querySelector(`#resposta_${element}`).style.display = "none";
}

