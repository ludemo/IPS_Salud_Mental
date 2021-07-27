google.charts.load('current', {packages: ['corechart', 'controls']});
google.charts.setOnLoadCallback(drawChart1);
google.charts.setOnLoadCallback(drawChart2);
google.charts.setOnLoadCallback(drawChart3);
var menu = document.getElementById('menu');
var tipo;
menu.addEventListener('change',drawChart1, false);
function drawChart1() {
    tipo = document.getElementById('menu').value;
    
    $.ajax({
        url: "/static/json/enf_regiones.json",
        dataType: "JSON",
        success: function (jsonData) {

            var dataArray = [
                ['Enfermedades', 'Atendidos', 'Atenciones'],
            ];
            for (var i = parseInt(tipo)*10-1; (parseInt(tipo)-1)*10-1 < i; i--) {
                    var row = [jsonData[i].Enfermedad, parseInt(jsonData[i].Atendidos), parseInt(jsonData[i].Atenciones)];
                    console.log(row);   
                    console.log(i);               
                    dataArray.push(row);        
            }
            var options = {
                title: 'Casos de enfermedades mentales registrados por departamento',
                'width':1000,
                'height':600,
                aAxis : { 
                    textStyle : {
                        fontSize: 12
                    }
                },
                vAxis : { 
                    textStyle : {
                        fontSize: 10
                    }
                },
                series: {0: {"color": '#A2D9D8'},
                            1: {"color": '#3BAFBF'},
                }
            };
            var data = google.visualization.arrayToDataTable(dataArray);
            console.log(tipo);
            var chart = new google.visualization.BarChart(document.getElementById('chart_div'));
                chart.draw(data, options);
        }
    });
}
var etapa = document.getElementById('etapa');
var numeroEtapa;
etapa.addEventListener('change',drawChart2, false);
function drawChart2() {
    numeroEtapa = parseInt(document.getElementById('etapa').value);
    $.ajax({
        url: "/static/json/Etapa.json",
        dataType: "JSON",
        success: function (jsonData) {

            var dataArray = [ 
                ['Etapa', 'Masculino', 'Femenino '],
            ];/*
            for (var i = parseInt(numeroEtapa)*3-1; (parseInt(numeroEtapa)-1)*3-1 < i; i--) {
                    var row = [jsonData[i].Etapa, parseInt(jsonData[i].Masculino), parseInt(jsonData[i].Femenino)];                  
                    dataArray.push(row);        
            }*/
            var row = [jsonData[numeroEtapa].Etapa, parseInt(jsonData[numeroEtapa].Masculino), parseInt(jsonData[numeroEtapa].Femenino)];
            dataArray.push(row);
            var options = {
                title: 'Casos de enfermedades mentales registrados por departamento',
                'width':1000,
                'height':600,
                series: {0: {"color": '#A2D9D8'},
                            1: {"color": '#3BAFBF'},
                }
            };
            var data = google.visualization.arrayToDataTable(dataArray);
            console.log(etapa);
            var chart = new google.visualization.BarChart(document.getElementById('chart_div'));
                chart.draw(data, options);
        }
    });
}
var genero = document.getElementById('genero');
var claseGenero;
genero.addEventListener('change',drawChart3, false);

function drawChart3() {
    claseGenero = document.getElementById('genero').value;
    console.log(claseGenero);
    $.ajax({
        url: "/static/json/Genero.json",
        dataType: "JSON",
        success: function (jsonData) {

            var dataArray = [
                ['Genero', 'Atendidos', 'Atenciones'],
            ];
                if (claseGenero == 0) {
                    var row = [jsonData[0].Sexo, parseInt(jsonData[0].Atendidos), parseInt(jsonData[0].Atenciones)];                  
                    dataArray.push(row);  
                }else if (claseGenero == 1) {
                    var row = [jsonData[1].Sexo, parseInt(jsonData[1].Atendidos), parseInt(jsonData[1].Atenciones)];                  
                    dataArray.push(row); 
                }
      
            
            var options = {
                title: 'Casos de enfermedades mentales registrados por departamento',
                'width':1000,
                'height':600,
                series: {0: {"color": '#A2D9D8'},
                            1: {"color": '#3BAFBF'},
                }
            };
            var data = google.visualization.arrayToDataTable(dataArray);
            var chart = new google.visualization.BarChart(document.getElementById('chart_div'));
                chart.draw(data, options);
        }
    });
}