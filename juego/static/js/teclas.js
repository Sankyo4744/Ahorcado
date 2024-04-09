let lifes = 7;
let incorrectas = "";

const input_palabra = document.getElementById("input-palabra").value;
const palabra_lower = input_palabra.toLowerCase();
const pista_categoria = document.getElementById("pista-categoria");
const pista_caracter = document.getElementById("pista-caracter");
const pista_frase = document.getElementById("pista-frase");

function mostrar_pistas(self) {
    /* querySelector es para seleccionar varios elementos en html y selecciona los inputs que tienen el nombre igual al id que el boton que fue espichado */
    const input = document.querySelector('input[name="' + self.id + '"]');
    console.log(self);
    if (self === pista_categoria){
        pista_categoria.textContent= input.value;
        pista_categoria.disabled = true;
        pista_categoria.style.backgroundColor = "#000080"
    }else if (self === pista_caracter){
        pista_caracter.textContent= input.value;
        pista_caracter.disabled = true;
        pista_caracter.style.backgroundColor = "#000080"
    }else if (self === pista_frase){
        pista_frase.textContent= input.value;
        pista_frase.disabled = true;
        pista_frase.style.backgroundColor = "#000080";
        pista_frase.style.fontSize = "1em";
        pista_frase.style.height = "100px";
    }
}       


document.addEventListener("keydown", function(event) {
    /* se obtiene el valor ASCII de la letra para que evite numeros, signos especiales y teclas especiales */
    if(event.keyCode >= 65 && event.keyCode <= 90){
        const adivina = document.getElementById("adivina");
        const visible = window.getComputedStyle(adivina).getPropertyValue("display") !== "none";
        if (!visible) {
            let teclas = event.key.toLowerCase();
            document.getElementById("teclas").value=teclas;
            if (!palabra_lower.includes(teclas.toLowerCase())){ 
                if (!incorrectas.includes(teclas.toLowerCase())){
                    lifes = lifes - 1;
                    incorrectas += teclas.toLowerCase();
                }
            }else {
                let linea = document.querySelectorAll("#" + teclas);
                linea.forEach(linea => {
                    linea.textContent=teclas;
                    linea.style.borderBottom = "white solid 4px";
                    linea.style.padding = "10px";
                } );            
            }
            /* submit le dice al formulario que se envie a la url asignada */
            document.getElementById("formTeclas").submit();
            console.log("La tecla seleccionada es: " + teclas);
            console.log("La cantidad de vidas que tiene es: " + lifes);
            console.log(palabra_lower);
            console.log(incorrectas + "este es el valor de incorrectas");
        }

        vidas();
    }
    
});

function vidas(){

    const cabeza_izquierda = document.getElementById("cabeza-izquierda");
    const cabeza_derecha = document.getElementById("cabeza-derecha");
    const torso_izquierdo_1 = document.getElementById("torso-izquierdo-1");
    const torso_izquierdo_2 = document.getElementById("torso-izquierdo-2");
    const torso_derecho_1 = document.getElementById("torso-derecho-1");
    const torso_derecho_2 = document.getElementById("torso-derecho-2");
    const pierna_derecha = document.getElementById("pierna-derecha");
    const pierna_izquierda = document.getElementById("pierna-izquierda");
    const corazon_1 = document.getElementById("corazon-1");
    const corazon_2 = document.getElementById("corazon-2");
    const corazon_3 = document.getElementById("corazon-3");
    const corazon_4 = document.getElementById("corazon-4");
    const corazon_5 = document.getElementById("corazon-5");
    const corazon_6 = document.getElementById("corazon-6");
    const corazon_7 = document.getElementById("corazon-7");
    /* const game_over = document.getElementById("game-over"); */


    if (lifes === 6) {
        cabeza_derecha.style.backgroundImage= "url('/static/images/cabeza derecha.png')";
        cabeza_izquierda.style.backgroundImage= "url('/static/images/cabeza izquierda.png')";
        corazon_7.style.color = "transparent";
    }else if (lifes === 5) {
        torso_izquierdo_1.style.borderRigth = "white solid 4px";
        torso_derecho_1.style.borderLeft = "white solid 4px";
        corazon_6.style.color = "transparent"
    }else if (lifes === 4) {
        torso_izquierdo_2.style.borderRigth = "white solid 4px";
        torso_derecho_2.style.borderLeft = "white solid 4px";
        corazon_5.style.color = "transparent"
    }else if (lifes === 3) {
        torso_izquierdo_1.style.backgroundImage= "url('/static/images/brazo y pierna derecha.png')";
        corazon_4.style.color = "transparent"
    }else if (lifes === 2){
        torso_derecho_1.style.backgroundImage= "url('/static/images/brazo y pierna izquierda.png')";
        corazon_3.style.color = "transparent"
    }else if (lifes === 1){
        pierna_derecha.style.backgroundImage= "url('/static/images/brazo y pierna izquierda.png')";
        corazon_2.style.color = "transparent"
    }else if (lifes === 0){
        pierna_izquierda.style.backgroundImage= "url('/static/images/brazo y pierna derecha.png')";
        corazon_1.style.color = "transparent"
        /* game_over.style.display = "flex" */
    }

}




