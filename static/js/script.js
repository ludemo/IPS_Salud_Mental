
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
        //console.log("ntro scroll");
        //console.log(window.scrollY);
        const header = document.querySelector('header');
        header.classList.toggle("header-active",window.scrollY>0)
    })
}

//Formularios scripts
try{
    navSlide();
    headerEfect();
    formulario();
}
catch(error){
    console.error(error);
}
try{
    carrusel();

}
catch(error){
    console.log(error);
}

function carrusel(){
    var cantidad = 0;
    var comentario = document.getElementsByClassName("comentario-carrusel__comentario");
    var izquierda = document.getElementById("flecha-izquierda");
    var derecha = document.getElementById("flecha-derecha");


    izquierda.onclick = function(){anterior();}
    derecha.onclick = function(){siguiente();}
    demo();

    async function demo(){
        while(true){
            await new Promise(r => setTimeout(r, 3000));
            siguiente();
        }
    }
    function siguiente(){
        cantidad-=100;
        for(let i = 0 ; i<comentario.length; i++){
            comentario[i].style.transform="translateX("+cantidad+"%)";
        }
        if(cantidad<-400){
            moverInicio();
        }
    }
    function moverInicio(){
        for(let i = 0 ; i<comentario.length; i++){
            comentario[i].style.transform="translateX("+0+"%)";
        }
        cantidad = 0;
    }
    function moverFin(){
        for(let i = 0 ; i<comentario.length; i++){
            comentario[i].style.transform="translateX(-"+(comentario.length-1)*100+"%)";
        }
        cantidad = -400;
    }
    function anterior(){
        cantidad+=100;
        for(let i = 0 ; i<comentario.length; i++){
            comentario[i].style.transform="translateX("+cantidad+"%)";
        }
        if(cantidad>0){
            moverFin();
        }
    }
}
function formulario() {

    var SI = document.getElementById("si");
    var NO = document.getElementById("no");
    var pregunta = document.getElementsByClassName("pregunta__texto");
    var barra = document.getElementById("barra-carga");
    var contSI = 0;
    var contNO = 0;
    var cantidad = 0;
    var carga = 0;
    //pregunta 1
    SI.onclick = function(){
        contSI++;
        cantidad+=100;
        carga+=5;
        siguiente();
        cargaFunction();
        if(carga==100){
            termino();
        }
    }
    NO.onclick = function(){
        contNO++;
        cantidad+=100;
        carga+=5;
        siguiente();
        cargaFunction();
        if(carga==100){
            termino();
        }
    }
    function siguiente(){
        for(let i = 0 ; i<pregunta.length; i++){
            pregunta[i].style.transform="translateX(-"+cantidad+"%)";
        }
    }
    function cargaFunction(){
        barra.style.width=carga+"%";
    }
    function termino(){
        //contador final
        var text = document.getElementById("cantidadVeces");
        text.innerHTML = contSI;
        console.log("Se presionaron "+contSI+ " si" );
        console.log("Se presionaron "+contNO+ " no" );
        //msotrar respuesta
        var respuesta= document.getElementById("respuesta");
        respuesta.style.display="block";
        var formulario = document.getElementById("formulario");
        formulario.style.display="none"; 
    }
}
