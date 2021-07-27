google.charts.load('current', {packages: ['corechart', 'controls']});
google.charts.setOnLoadCallback(drawChart);

var menu = document.getElementById('menu');
var tipo;
menu.addEventListener('change',drawChart, false);
function drawChart() {
    tipo = document.getElementById('menu').value;
    
    $.ajax({
        //url: "/cuidades.json",
        url: "/static/json/enf_regiones.json",
        dataType: "JSON",
        success: function (jsonData) {

            var dataArray = [
                ['Enfermedades', 'Atendidos'],
            ];
            for (var i = parseInt(tipo)*10; (parseInt(tipo)-1)*10 < i; i--) {
                    var row = [jsonData[i].Enfermedad, parseInt(jsonData[i].Atendidos)];
                    console.log(row);                  
                    dataArray.push(row);
                    //console.log(i);         
            }
            var options = {
                title: 'Casos de enfermedades mentales registrados por departamento',
                'width':1000,
                'height':600,
                series: {0: {"color": '#57c8f2'}}
            };
            var data = google.visualization.arrayToDataTable(dataArray);
            console.log(tipo);
            var chart = new google.visualization.BarChart(document.getElementById('chart_div'));
                chart.draw(data, options);
        }
    });
}