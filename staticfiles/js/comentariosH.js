function getCookie(name){
    let cookieValue = null;
    if(document.cookie && document.cookie !== ''){
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++){
            let cookie = cookies[i].trim();
            if (cookie.substring(0,name.length +1) === (name + '=')){
                cookieValue = decodeURIComponent(cookie.substring(name.length +1));
                break;
            }
        }
    }
    return cookieValue;
}

function GuardarComentarioH(){
    let form = new FormData(document.getElementById("formComentarioH"));
    console.log(form);
    let divP = document.getElementById('comentario-carrusel');

    
    fetch("/", {
        method: "POST",
        body: form,
        headers:{
            "X-CSRFToken": getCookie('csrftoken'),
            "X-Requested-With": "XMLHttpRequest"
        }
    }).then(
        function(response){
        return response.json()
        }
    ).then(
        function(data){
            array_com = data.postsH;
            console.log(array_com);
            // crear un div y meter todo

         /*   let divE = document.createElement('div');
            divE.setAttribute("class", "comentario-carrusel__comentario");

            let h4E = document.createElement("h4");
            let imgE = document.createElement("img");
            //let stri = document.querySelector(".img-comilla");
            //imgE.setAttribute("src", stri.src);
            //imgE.setAttribute("alt", "comillas");
            let pE = document.createElement("p");

            h4E.innerHTML = array_com[array_com.length - 1].nombreUserH;
            pE.innerHTML = array_com[array_com.length - 1].comentarioH;

            divE.appendChild(h4E);
            //divE.appendChild(imgE);
            divE.appendChild(pE);

            divP.appendChild(divE);
            console.log(divP);*/

            location.reload();
        }
    )
}