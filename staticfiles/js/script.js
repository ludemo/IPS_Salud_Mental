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

headerEfect();
navSlide();
//Formularios scripts
formulario();
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
