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
