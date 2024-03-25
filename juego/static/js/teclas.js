let lifes = 7
const input_palabra = document.getElementById("input-palabra").value;
const palabra_lower = input_palabra.toLowerCase();


document.addEventListener("keydown", function(event) {
    const adivina = document.getElementById("adivina");
    const visible = window.getComputedStyle(adivina).getPropertyValue("display") !== "none";
    if (!visible) {
        let teclas = event.key;
        document.getElementById("teclas").value=teclas;
        if (!palabra_lower.includes(teclas.toLowerCase())){ 
            lifes = lifes - 1;
        }else {
            let linea = document.querySelectorAll("#" + teclas);
            linea.forEach(linea => {
                linea.textContent=teclas;
                linea.style.borderBottom = "white solid 4px";
                linea.style.padding = "10px";
            } )
            console.log(linea);
        }
        document.getElementById("formTeclas").submit();
        console.log("La tecla seleccionada es: " + teclas);
        console.log("La cantidad de vidas que tiene es: " + lifes);
        console.log(palabra_lower);

        const cabeza_izquierda = document.getElementById("cabeza-izquierda");
        const cabeza_derecha = document.getElementById("cabeza-derecha");
        const torso_izquierdo_1 = document.getElementById("torso-izquierdo-1");
        const torso_izquierdo_2 = document.getElementById("torso-izquierdo-2");
        const torso_derecho_1 = document.getElementById("torso-derecho-1");
        const torso_derecho_2 = document.getElementById("torso-derecho-2");
        const pierna_derecha = document.getElementById("pierna-derecha");
        const pierna_izquierda = document.getElementById("pierna-izquierda");

        if (lifes === 6) {
            cabeza_derecha.style.backgroundImage= "url('/static/images/cabeza derecha.png')";
            cabeza_izquierda.style.backgroundImage= "url('/static/images/cabeza izquierda.png')";
        }

        if (lifes === 5) {
            torso_izquierdo_1.style.borderRigth = "white solid 4px";
            torso_derecho_1.style.borderLeft = "white solid 4px";
        }

        if (lifes === 4) {
            torso_izquierdo_2.style.borderRigth = "white solid 4px";
            torso_derecho_2.style.borderLeft = "white solid 4px";
        }

        if (lifes === 3) {
            torso_izquierdo_1.style.backgroundImage= "url('/static/images/brazo y pierna derecha.png')";
        }

        if (lifes === 2){
            torso_derecho_1.style.backgroundImage= "url('/static/images/brazo y pierna izquierda.png')";
        }

        if (lifes === 1){
            pierna_derecha.style.backgroundImage= "url('/static/images/brazo y pierna izquierda.png')";
        }

        if (lifes === 0){
            pierna_izquierda.style.backgroundImage= "url('/static/images/brazo y pierna derecha.png')";
        }
    }
});






