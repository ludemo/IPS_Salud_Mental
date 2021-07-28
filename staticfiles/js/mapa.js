
var mymap = L.map('mapid').setView([-16.3989, -71.5369], 5);

L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
    maxZoom: 18,
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, ' +
            'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1
}).addTo(mymap);


// obtiene las coordenadas del centro de salud seleccionado

 var centro_medico = document.getElementById('centro__medico');

centro_medico.addEventListener('input', function (event) {
    var coordenadas = centro_medico.value;
    console.log(coordenadas);
    var list_coordenadas = coordenadas.split(",")
    console.log(list_coordenadas);
    var lat_centro_medico = list_coordenadas[0];
    var long_centro_medico = list_coordenadas[1];
    console.log(lat_centro_medico);
    console.log(long_centro_medico);
    
    //obtiene tu ubicacion
    navigator.geolocation.getCurrentPosition(getPosition);

    function getPosition(position) {
        // imprime en consola tu ubicacion
        console.log(position);
        // obtiene la latitud
        lat = position.coords.latitude;
        // obtiene la longitud
        long = position.coords.longitude;  
        L.Routing.control({
            waypoints:   [
            // Se traza la ruta entre tu ubicacion y el centro de salud seleccionado
            L.latLng(parseFloat(lat), parseFloat(long)),
            L.latLng(parseFloat(lat_centro_medico), parseFloat(long_centro_medico)),
            ]
         }).addTo(mymap);
    }
}, false);