document.addEventListener("keydown", function(event) {
    let teclas = event.key;
    document.getElementById("teclas").value=teclas;
    document.getElementById("formTeclas").submit();
    console.log("La tecla sleccionada es: " + teclas)
});



