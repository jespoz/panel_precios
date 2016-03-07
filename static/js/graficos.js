$('#container').highcharts({

        chart: {
            type: 'gauge',
            margin: 10,
            backgroundColor: 'transparent'
        },

        title: null,

        pane: {
            center: ['50%', '85%'],
            size: '120%',
            startAngle: -90,
            endAngle: 90,
            background: null
        },

        tooltip: {
            enabled: false
        },
        
        yAxis: {
            tickPositions: [0, 15, 20, 25],
            tickmarkPlacement: 'on',
            tickLength: 54,
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

        credits: {
            enabled: false
        },

        series: [{
            name: 'Speed',
            data: [0]
        }]
});

setTimeout(function () {
    var chart = $('#container').highcharts(),
        point,
        newVal,
        inc;

    var valor = $('#container').data('value');
    valor = valor.replace(',', '.').replace('-', '');


    if (chart) {
        point = chart.series[0].points[0];
        newVal = point.y + parseFloat(valor);

        point.update(newVal);
    }
}, 1000);

// var options_sector = {
//     chart: {
//         renderTo: 'part_sector',
//         plotBackgroundColor: null,
//         plotBorderWidth: null,
//         plotShadow: false,
//         backgroundColor: 'transparent'
//     },
//     colors: [
//     	'#00669E', 
//     	'#F26013', 
//     	'#CCE0EC', 
//     	'#FFD400', 
//     	'#CC0000', 
//     	'#00C112', 
//     	'#9F9F9F'
//     ],
//     credits: {
//     	enabled: false
//     },
//     title: {
//         text: 'Participación Descuentos <br/>Netos'
//     },
//     tooltip: {
//         formatter: function() {
// 	        return this.point.name + '<br/><b>$ -' + this.y + ' MM</b>';
// 	    }
//     },
//     plotOptions: {
//         pie: {
//             allowPointSelect: true,
//             cursor: 'pointer',
//             dataLabels: {
//                 enabled: true,
//                 format: '{percentage:,.1f}%',
//                 distance: -30
//             },
//             showInLegend: true,
//             size: '100%'
//         }
//     },
//     legend: {
//     	layout: 'vertical',
//     	align: 'right',
//     	verticalAlign: 'middle'
//     },
//     series: [{
//         type: 'pie',
//         data: []
//     }]
// }

// var options_tc = {
//     chart: {
//         renderTo: 'part_tc',
//         plotBackgroundColor: null,
//         plotBorderWidth: null,
//         plotShadow: false,
//         backgroundColor: 'transparent'
//     },
//     colors: [
//     	'#00669E', 
//     	'#F26013', 
//     	'#CCE0EC', 
//     	'#FFD400', 
//     	'#CC0000', 
//     	'#00C112', 
//     	'#9F9F9F'
//     ],
//     credits: {
//     	enabled: false
//     },
//     title: {
//         text: 'Participación Descuentos <br/>Netos'
//     },
//     tooltip: {
//         formatter: function() {
// 	        return this.point.name + '<br/><b>$ -' + this.y + ' MM</b>';
// 	    }
//     },
//     plotOptions: {
//         pie: {
//             allowPointSelect: true,
//             cursor: 'pointer',
//             dataLabels: {
//                 enabled: true,
//                 format: '{percentage:,.1f}%',
//                 distance: -30
//             },
//             showInLegend: true,
//             size: '100%'
//         }
//     },
//     legend: {
//     	layout: 'vertical',
//     	align: 'right',
//     	verticalAlign: 'middle'
//     },
//     series: [{
//         type: 'pie',
//         data: []
//     }]
// }

// var options_zona = {
//     chart: {
//         renderTo: 'part_zona',
//         plotBackgroundColor: null,
//         plotBorderWidth: null,
//         plotShadow: false,
//         backgroundColor: 'transparent'
//     },
//     colors: [
//     	'#00669E', 
//     	'#F26013', 
//     	'#CCE0EC', 
//     	'#FFD400', 
//     	'#CC0000', 
//     	'#00C112', 
//     	'#9F9F9F'
//     ],
//     credits: {
//     	enabled: false
//     },
//     title: {
//         text: 'Participación Descuentos <br/>Netos'
//     },
//     tooltip: {
//         formatter: function() {
// 	        return this.point.name + '<br/><b>$ -' + this.y + ' MM</b>';
// 	    }
//     },
//     plotOptions: {
//         pie: {
//             allowPointSelect: true,
//             cursor: 'pointer',
//             dataLabels: {
//                 enabled: true,
//                 format: '{percentage:,.1f}%',
//                 distance: -30
//             },
//             showInLegend: true,
//             size: '100%'
//         }
//     },
//     legend: {
//     	layout: 'vertical',
//     	align: 'right',
//     	verticalAlign: 'middle'
//     },
//     series: [{
//         type: 'pie',
//         data: []
//     }]
// }

// $.getJSON('/participacion/', function(json) {
//     options_sector.series[0].data = json.participacion_sector;
//     chart_sector = new Highcharts.Chart(options_sector);
//     options_tc.series[0].data = json.participacion_tc;
//     chart_tc = new Highcharts.Chart(options_tc);
//     options_zona.series[0].data = json.participacion_zona;
//     chart_zona = new Highcharts.Chart(options_zona);
// });

chart_cumpl_sector = new Highcharts.Chart({
	chart: {
		type: 'column',
		renderTo: 'cumpl_sector',
		spacingLeft: 20,
		spacingRight: 30
	},
	title: {
		text: 'Cumplimiento Kilos'
	},
	credits: {
		enabled: false
	},
	yAxis: {
		title: {
			text: null
		},
		gridLineWidth: 0,
		plotLines: [{
            color: '#F26013',
            dashStyle: 'dash',
            width: 3,
            value: 100,
            label: {
                align: 'right',
                style: {
                    fontStyle: 'italic'
                },
                text: '100% Cumplimiento',
                x: -10
            },
            zIndex: 3
        },{
            color: 'white',
            dashStyle: 'solid',
            width: 2,
            value: 15,
            label: {
                align: 'right',
                style: {
                    fontStyle: 'italic'
                },
                text: null,
                x: -10
            },
            zIndex: 3
        }]
	},
	legend : {
    	enabled: true
    },
    plotOptions: {
	    series: {
	        pointWidth: 40
	    }
	},
	colors: [
    	'#00669E'
    ],
    tooltip: {
    	pointFormat: '{point.y}%'
    }
});

chart_cumpl_tc = new Highcharts.Chart({
	chart: {
		type: 'column',
		renderTo: 'cumpl_tc',
		spacingLeft: 20,
		spacingRight: 30
	},
	title: {
		text: 'Cumplimiento Kilos'
	},
	credits: {
		enabled: false
	},
	yAxis: {
		title: {
			text: null
		},
		gridLineWidth: 0,
		plotLines: [{
            color: '#F26013',
            dashStyle: 'dash',
            width: 3,
            value: 100,
            label: {
                align: 'right',
                style: {
                    fontStyle: 'italic'
                },
                text: '100% Cumplimiento',
                x: -10
            },
            zIndex: 3
        },{
            color: 'white',
            dashStyle: 'solid',
            width: 2,
            value: 15,
            label: {
                align: 'right',
                style: {
                    fontStyle: 'italic'
                },
                text: null,
                x: -10
            },
            zIndex: 3
        }]
	},
	legend : {
    	enabled: true
    },
    plotOptions: {
	    series: {
	        pointWidth: 40
	    }
	},
	colors: [
    	'#00669E'
    ],
    tooltip: {
    	pointFormat: '{point.y}%'
    }
});

chart_cumpl_zona = new Highcharts.Chart({
	chart: {
		type: 'column',
		renderTo: 'cumpl_zona',
		spacingLeft: 20,
		spacingRight: 30
	},
	title: {
		text: 'Cumplimiento Kilos'
	},
	credits: {
		enabled: false
	},
	yAxis: {
		title: {
			text: null
		},
		gridLineWidth: 0,
		plotLines: [{
            color: '#F26013',
            dashStyle: 'dash',
            width: 3,
            value: 100,
            label: {
                align: 'right',
                style: {
                    fontStyle: 'italic'
                },
                text: '100% Cumplimiento',
                x: -10
            },
            zIndex: 3
        },{
            color: 'white',
            dashStyle: 'solid',
            width: 2,
            value: 15,
            label: {
                align: 'right',
                style: {
                    fontStyle: 'italic'
                },
                text: null,
                x: -10
            },
            zIndex: 3
        }]
	},
	legend : {
    	enabled: true
    },
    plotOptions: {
	    series: {
	        pointWidth: 40
	    }
	},
	colors: [
    	'#00669E'
    ],
    tooltip: {
    	pointFormat: '{point.y}%'
    }
});

var cumplimientos_sector = [];
var descuentos_sector = [];
var sectores = [];
var cumplimientos_tc = [];
var descuentos_tc = [];
var tiposclientes = [];
var cumplimientos_zona = [];
var descuentos_zona = [];
var zonas = [];

var $periodo = $("#periodo").val();
var $url = '/cumplimiento/' + $periodo + '/';

$.getJSON($url, function(json) {

	$.each(json.cumplimiento_sector, function(key, val){
		cumplimientos_sector.push(val.cumpl_kilos);
        descuentos_sector.push(val.descuento);
		sectores.push(val.sector);
	});
	chart_cumpl_sector.xAxis[0].setCategories(sectores);
	var series = {data: cumplimientos_sector, name: '% Cumpl. Ppto.'};
	chart_cumpl_sector.addSeries(series);
    chart_cumpl_sector.addAxis({
        title: {
            text: null
        },
        opposite: true
    });
    chart_cumpl_sector.addSeries({
        type: 'line',
        color: 'yellow',
        data: descuentos_sector,
        name: '% Descuento',
        dataLabels: {
            enabled: true,
            format: '-{point.y}%',
            color: 'white',
            style: {
                'color': 'white',
                'textShadow': '0'
            }
        }
    });

	$.each(json.cumplimiento_tipocliente, function(key, val){
		cumplimientos_tc.push(val.cumpl_kilos);
		tiposclientes.push(val.tipo);
        descuentos_tc.push(val.descuento);
	});
	chart_cumpl_tc.xAxis[0].setCategories(tiposclientes);
	series = {data: cumplimientos_tc, name: '% Cumpl. Ppto.'};
	chart_cumpl_tc.addSeries(series);
        chart_cumpl_sector.addAxis({
        title: {
            text: null
        },
        opposite: true
    });
    chart_cumpl_tc.addSeries({
        type: 'line',
        color: 'yellow',
        data: descuentos_tc,
        name: '% Descuento',
        dataLabels: {
            enabled: true,
            format: '-{point.y}%',
            color: 'white',
            style: {
                'color': 'white',
                'textShadow': '0'
            }
        }
    });

	$.each(json.cumplimiento_zona, function(key, val){
		cumplimientos_zona.push(val.cumpl_kilos);
		zonas.push(val.zona);
        descuentos_zona.push(val.descuento);
	});
	chart_cumpl_zona.xAxis[0].setCategories(zonas);
	series = {data: cumplimientos_zona, name: '% Cumpl. Ppto.'};
	chart_cumpl_zona.addSeries(series);
    chart_cumpl_zona.addAxis({
        title: {
            text: null
        },
        opposite: true
    });
    chart_cumpl_zona.addSeries({
        type: 'line',
        color: 'yellow',
        data: descuentos_zona,
        name: '% Descuento',
        dataLabels: {
            enabled: true,
            format: '-{point.y}%',
            color: 'white',
            style: {
                'color': 'white',
                'textShadow': '0'
            }
        }
    });
});

$("#tendencia").highcharts({
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

var fechas = [];
var descuentos = [];

var $periodo2 = $("#periodo").val();
var $url2 = '/tendencias/' + $periodo + '/';

$.getJSON($url2, function(json) {
    $.each(json.tendencia_general, function(key, value){
        descuentos.push(value.descuento);
        fechas.push(value.fecha.substring(0, 5));
    });
    var series = {data: descuentos, color: '#F26013'};
    var chart = $("#tendencia").highcharts(),
        point,
        newval,
        inc;
    chart.xAxis[0].setCategories(fechas);
    chart.addSeries(series);
    descuentos = [];
    fechas = [];
});