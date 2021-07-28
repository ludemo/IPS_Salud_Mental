google.charts.load('current', {packages: ['corechart', 'controls']});
google.charts.setOnLoadCallback(drawChart1);
google.charts.setOnLoadCallback(drawChart2);
google.charts.setOnLoadCallback(drawChart3);
google.charts.setOnLoadCallback(drawChart4);

var departamento = document.getElementById('departamento');
var departamentoNum;
departamento.addEventListener('change',drawChart1, false);
function drawChart1() {
    departamentoNum = document.getElementById('departamento').value;
    
    $.ajax({
        url: "/static/json/enf_regiones.json",
        dataType: "JSON",
        success: function (jsonData) {

            var dataArray = [
                ['Enfermedades', 'Atendidos', 'Atenciones'],
            ];
            for (var i = parseInt(departamentoNum)*10-1; (parseInt(departamentoNum)-1)*10-1 < i; i--) {
                    var row = [jsonData[i].Enfermedad, parseInt(jsonData[i].Atendidos), parseInt(jsonData[i].Atenciones)];              
                    document.getElementById('desGrafica').innerHTML = jsonData[i].Departamento;
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
            ];
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
            document.getElementById('desGrafica').innerHTML = jsonData[numeroEtapa].Etapa;
        }
    });
}
var genero = document.getElementById('genero');
var claseGenero;
genero.addEventListener('change',drawChart3, false);
function drawChart3() {
    claseGenero = parseInt(document.getElementById('genero').value);
    $.ajax({
        url: "/static/json/Genero.json",
        dataType: "JSON",
        success: function (jsonData) {

            var dataArray = [
                ['Genero', 'Atendidos', 'Atenciones'],
            ];
            var row = [jsonData[claseGenero].Sexo, parseInt(jsonData[claseGenero].Atendidos), parseInt(jsonData[0].Atenciones)];                  
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
            var chart = new google.visualization.BarChart(document.getElementById('chart_div'));
            chart.draw(data, options);
            document.getElementById('desGrafica').innerHTML = jsonData[claseGenero].Sexo;
        }
    });
}
function drawChart4(enfermedad) {
    console.log(enfermedad);
    var enfermedadNum = parseInt(enfermedad)
    $.ajax({
        url: "/static/json/enfermedades.json",
        dataType: "JSON",
        success: function (jsonData) {

            var dataArray = [
                ['Enfermedad', 'Atendidos', 'Atenciones'],
            ];
            var row = [jsonData[enfermedadNum].Enfermedad, parseInt(jsonData[enfermedadNum].Atenciones), parseInt(jsonData[enfermedadNum].Atendidos)];
            dataArray.push(row);
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
            var chart = new google.visualization.BarChart(document.getElementById('chart_div'));
            chart.draw(data, options);
            document.getElementById('desGrafica').innerHTML = jsonData[enfermedadNum].Enfermedad;
        }
    });
}