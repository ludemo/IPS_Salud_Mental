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

function GuardarComentario(){
    let form = new FormData(document.getElementById("formComentario"));
    console.log(form);

    
    fetch("/mapa/", {
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
            array_com = data.posts;
            console.log(array_com);
            // crear un div y meter todo
            

        }
    )
}