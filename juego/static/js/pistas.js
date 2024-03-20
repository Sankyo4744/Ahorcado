const btnPistas = document.getElementById("btnPistas");
const btnClose = document.getElementById("close");
const pistas = document.getElementById("pistas");

function pistasVisible() {
    pistas.style.display="flex"
}
function pistasInvisible() {
    pistas.style.display="none"
}
btnPistas.addEventListener("click", pistasVisible);
btnClose.addEventListener("click", pistasInvisible);