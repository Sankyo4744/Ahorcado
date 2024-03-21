const btnAdivina = document.getElementById("btnAdivina");
const btnClose_Adivina = document.getElementById("close-adivina");
const adivina = document.getElementById("adivina");

function adivinaVisible() {
    adivina.style.display="flex"
}
function adivinaInvisible() {
    adivina.style.display="none"
}
btnAdivina.addEventListener("click", adivinaVisible)
btnClose_Adivina.addEventListener("click", adivinaInvisible)

// abrir ventana de adivina