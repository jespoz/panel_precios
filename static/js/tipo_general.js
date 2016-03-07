var id = [10, 20, 40, 50, 70];

$.each(id, function(key, val){
    $("#gauge_desc_" + val).highcharts({
        chart: {
            type: 'gauge',
            margin: 0,
            backgroundColor: 'transparent'
        },
        credits: {
            enabled: false
        },
        title: {
            text: null
        },
        pane : {
            center: ['50%', '85%'],
            size: '120%',
            startAngle: -90,
            endAngle: 90,
            background: null
        },
        tooltip: {
            enabled: true,
            pointFormat: "<span style=color:{point.color}>\u25CF</span> {series.name}: <b>{point.y}%</b><br/>"
        },
        yAxis: {
            tickPositions: [0, 15, 20, 25],
            tickmarkPlacement: 'on',
            tickLength: 30,
            minorTickLength: 1,
            min: 0,
            max: 25,
            labels: {
              distance: 20,
              format: '{value}%'
            },
            plotBands: [{
              from: 0,
              to: 15,
              color: '#00669E',
              thickness: '50%'
            }, {
              from: 15,
              to: 20,
              color: '#F26013',
              thickness: '50%'
            }, {
              from: 20,
              to: 25,
              color: '#CC0000',
              thickness: '50%'
            }]        
        },
        plotOptions: {
            gauge: {
              dataLabels: {
                enabled: false
              },
              dial: {
                baseLength: '0%',
                baseWidth: 10,
                radius: '100%',
                rearLength: '0%',
                topWidth: 1
              }
            }
        },
        series: [{
            name: 'Descuento',
            data: [0]
        }]
    });
});

setTimeout(function(){
    $.each(id, function(key, val){
        var chart = $("#gauge_desc_" + val).highcharts(),
            point,
            newval,
            inc;
        var valor = $("#gauge_desc_" + val).data('value');
        if (parseInt(valor) > 25) {
            valor = 25;
        };
        if (chart) {
            point = chart.series[0].points[0];
            newVal = point.y + parseFloat(valor);
            point.update(newVal);
        }
    }, 1000);
}); 

$.each(id, function(key, val){
    $("#pie_cumpl_" + val).highcharts({
        chart: {
            type: 'solidgauge',
            margin: 0,
            backgroundColor: 'transparent',
            spacingLeft: 0
        },
        credits: {
            enabled: false
        },
        title: {
            text: null
        },
        pane: {
            center: ['50%', '50%'],
            startAngle: 0,
            endAngle: 360,
            background: {
                backgroundColor: '#CCC',
                innerRadius: '60%',
                outerRadius: '100%',
                borderWidth: 0
            }
        },
        yAxis: {
            min: 0,
            max: 100,
            labels: {
                enabled: false
            },
            lineWidth: 0,
            minorTickInterval: null,
            tickPixelInterval: 400,
            tickWidth: 0,
            stops: [
                [0.7, '#CC0000'],
                [0.8, '#F26013'],
                [0.9, '#00669E']
            ],
        },
        plotOptions :{
            solidgauge: {
                innerRadius: '60%',
                dataLabels: {
                    y: -15,
                    borderWidth: 0,
                    useHTML: true,
                    format: '<span style="font-size:1.3em; color: #9F9F9F;">{y}%</span>'
                }
            }
        },
        tooltip: {
            enabled: false
        },
        series: [{
          data: [0]
        }]
    });
});

setTimeout(function(){
    $.each(id, function(key, val){
        var chart = $("#pie_cumpl_" + val).highcharts(),
            point,
            newval,
            inc;
        var valor = $("#pie_cumpl_" + val).data('value');
        if (chart) {
            point = chart.series[0].points[0];
            newVal = point.y + parseFloat(valor);
            point.update(newVal);
        }
    }, 1000);
});

$.each(id, function(key, val){
    $("#tendencia_" + val).highcharts({
        chart: {
            type: 'area'
        },
        title: {
            text: '% Descuento Diario',
            style: {
                color: '#00669E',
                fontSize: '1.2em'
            }
        },
        legend: {
            enabled: false
        },
        credits: {
            enabled: false
        },
        xAxis: {
            categories: [],
            title: {
                enabled: false
            }
        },
        yAxis: {
            title: {
                text: null
            },
            labels: {
                formatter: function () {
                    return this.value;
                }
            }
        },
        tooltip: {
            pointFormat: "<b>{point.y}%</b>"
        },
        plotOptions: {
            area: {
                stacking: 'normal',
                lineColor: '#F26013',
                lineWidth: 1,
                marker: {
                    lineWidth: 1,
                    lineColor: '#F26013',
                    fillColor: '#F26013',
                    symbol: 'circle'
                }
            },
            series: {
                fillOpacity: 0.2
            }
        },
        series: [{
            name: '% Descuento',
            data: [0]
        }]
    });
});

var fechas = [];
var descuentos = [];

var $periodo = $("#periodo").val();
var $url = '/tendencias/' + $periodo + '/';

$.getJSON($url, function(json) {
    $.each(id, function(key, val){
        $.each(json.tendencia_tipo, function(key, value){
            if (value.tipo_id == val) {
                descuentos.push(value.descuento);
                fechas.push(value.fecha.substring(0, 5));
            };
        });
        var series = {data: descuentos, color: '#F26013'};
        var chart = $("#tendencia_" + val).highcharts(),
            point,
            newval,
            inc;
        chart.xAxis[0].setCategories(fechas);
        chart.addSeries(series);
        descuentos = [];
        fechas = [];
    });
});