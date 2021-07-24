
    var mymap = L.map('mapid').setView([-16.3989, -71.5369], 5);

    L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
        maxZoom: 18,
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, ' +
            'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        id: 'mapbox/streets-v11',
        tileSize: 512,
        zoomOffset: -1
    }).addTo(mymap);

    L.marker([51.5, -0.09]).addTo(mymap);

    L.marker([53.5, -0.09]).addTo(mymap);

// Codigo se centro de salud seleccionado

 var centro_medico = document.getElementById('centro__medico');
 /*
 var coordenadas = centro_medico.value;
 console.log(coordenadas);
 var list_coordenadas = coordenadas.split(",")
 console.log(list_coordenadas);

var lat_centro_medico = list_coordenadas[0];
var long_centro_medico = list_coordenadas[1];
console.log(lat_centro_medico);
console.log(long_centro_medico);*/

centro_medico.addEventListener('input', function (event) {
    var coordenadas = centro_medico.value;
    console.log(coordenadas);
    var list_coordenadas = coordenadas.split(",")
    console.log(list_coordenadas);

    var lat_centro_medico = list_coordenadas[0];
    var long_centro_medico = list_coordenadas[1];
    console.log(lat_centro_medico);
    console.log(long_centro_medico);
    navigator.geolocation.getCurrentPosition(getPosition);
    function getPosition(position) {
        console.log(position);
        lat = position.coords.latitude;
        long = position.coords.longitude;
        console.log(lat);
        console.log(long);
        var accuracy = position.coords.accuracy;
    
        L.Routing.control({
            waypoints:   [
            L.latLng(parseFloat(lat), parseFloat(long)),
            L.latLng(parseFloat(lat_centro_medico), parseFloat(long_centro_medico)),
            //L.latLng(-16.3989, -71.5369)
            ]
         }).addTo(mymap);
         L.DomEvent.on(startBtn, 'click', function() {
            control.spliceWaypoints(0, 1, e.latlng);
            mymap.closePopup();
        });
    }
}, false);
/*
navigator.geolocation.getCurrentPosition(getPosition);

var lat;
var long;
function getPosition(position) {
    console.log(position);
    lat = position.coords.latitude;
    long = position.coords.longitude;
    console.log(lat);
    console.log(long);
    var accuracy = position.coords.accuracy;

    L.Routing.control({
        waypoints:   [
        L.latLng(parseFloat(lat), parseFloat(long)),
        L.latLng(parseFloat(lat_centro_medico), parseFloat(long_centro_medico)),
        //L.latLng(-16.3989, -71.5369)
        ]
     }).addTo(mymap)
}*/






console.log(lat);
console.log(long);