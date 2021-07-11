const navSlide = () =>{
    const burger = document.querySelector('.burger-box');
    const nav = document.querySelector('.ul-navbar');
    const header = document.querySelector('header');
    burger.addEventListener('click',()=>{
        nav.classList.toggle('navBar-active');
        header.classList.toggle("header-active");
    });
}

const headerEfect = () =>{
    window.addEventListener("scroll",function(){
        console.log("ntro scroll");
        console.log(window.scrollY);
        const header = document.querySelector('header');
        header.classList.toggle("header-active",window.scrollY>0)
    })
}

headerEfect();
navSlide();

//Formulario

//Función que se llama con el submit del formulario
function formulario() {
    var p1b1 =document.getElementById("p1b1");
    var p1b2 =document.getElementById("p1b2");
    console.log(p1b1.checked)
    var contSi = 0; //Contador de Sí
    var contNO = 0; //Contador de No


    //Revisa cada respuesta para generar los resultados pertinentes
    //pregunta 1
    if(p1b1.checked){contSi++;}
        else if(p1b2.checked){contNO++;}
    //pregunta 2
    if(p2b1.checked){contSi++;}
        else if(p2b2.checked){contNO++;}
    //pregunta 3
    if(p3b1.checked){contSi++;}
        else if(p3b2.checked){contNO++;}
    //pregunta 4
    if(p4b1.checked){contSi++;}
        else if(p4b2.checked){contNO++;}
    //pregunta 5
    if(p5b1.checked){contSi++;}
        else if(p5b2.checked){contNO++;}
    //pregunta 6
    if(p6b1.checked){contSi++;}
        else if(p6b2.checked){contNO++;}
    //pregunta 7
    if(p7b1.checked){contSi++;}
        else if(p7b2.checked){contNO++;}
    //pregunta 8
    if(p8b1.checked){contSi++;}
        else if(p8b2.checked){contNO++;}
    //pregunta 9
    if(p9b1.checked){contSi++;}
        else if(p9b2.checked){contNO++;}
    //pregunta 10
    if(p10b1.checked){contSi++;}
        else if(p10b2.checked){contNO++;}
    //pregunta 11
    if(p11b1.checked){contSi++;}
        else if(p11b2.checked){contNO++;}
    //pregunta 12
    if(p12b1.checked){contSi++;}
        else if(p12b2.checked){contNO++;}
    //pregunta 13
    if(p13b1.checked){contSi++;}
        else if(p13b2.checked){contNO++;}
    //pregunta 14
    if(p14b1.checked){contSi++;}
        else if(p14b2.checked){contNO++;}
    //pregunta 15
    if(p15b1.checked){contSi++;}
        else if(p15b2.checked){contNO++;}
    //pregunta 16
    if(p16b1.checked){contSi++;}
        else if(p16b2.checked){contNO++;}
    //pregunta 17
    if(p17b1.checked){contSi++;}
        else if(p17b2.checked){contNO++;}
    //pregunta 18
    if(p18b1.checked){contSi++;}
        else if(p18b2.checked){contNO++;}
    //pregunta 19
    if(p19b1.checked){contSi++;}
        else if(p19b2.checked){contNO++;}

    //contador final, Muestra la respuesta obtenida de la revisión
    var text = document.getElementById("cantidadVeces");
    text.innerHTML = contSi;
    console.log("Se presionaron "+contSi+ " si" );
    console.log("Se presionaron "+contNO+ " no" );
    //msotrar respuesta
    var respuesta= document.getElementById("respuesta");
    respuesta.style.display="block";//Modifica el bloque de html para mostrar
    var formulario = document.getElementById("formulario");
    formulario.style.display="none";//Modifica el bloque html para no mostrar
}
