var url = '';

function numberWithCommas(x) {
	return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".");
}

$("#table_1 tbody tr").on('click', function(){
	$("#table_2 tbody").html('');
	$("#table_2").hide();
	$("#table_2_reset button").hide();
	$("#table_3 tbody").html('');
	$("#table_3").hide();
	$("#table_3_reset button").hide();
	$("#table_4 tbody").html('');
	$("#table_4").hide();
	$("#table_4_reset button").hide();
	$("#table_5 tbody").html('');
	$("#table_5").hide();
	$("#dispersion").hide();
	var apertura = $("#table_1").data('apertura');
	var nivel_ops = "" + $("#table_1").data('nivel');
	$("#table_2 tbody").html('');
	$(this).siblings().hide();
	$("#table_1_reset button").css('display', 'block');
	if (apertura=='Zona de Ventas' && nivel_ops.length != 2) {
		$("#apertura_table_2").text('Oficina de Ventas');
		url = '/aperturamas/' + $("#periodo").val() + '/nivel2zona/' + $("#table_1").data('nivel') + '/' + $(this).data('filtro') + '/';
		$.getJSON(url, function(data){
			$.each(data.tabla, function(key, val){
				if (val.descuento < -15) {
					var color = "color_naranjo";
				}else{
					var color = "color_azul";
				};
				$("#table_2 tbody").append('<tr data-filtro=' + val.oficina__codigo + ' class=' + color + '><td>' + val.oficina + '</td><td>' + numberWithCommas(val.kilos) + '</td><td>' + numberWithCommas(val.netos) + '</td><td>' + numberWithCommas(val.netos_esperados) + '</td><td>' + numberWithCommas(val.facturado) + '</td><td>' + numberWithCommas(val.lista) + '</td><td>' + val.descuento.toString().replace('.', ',') + '%</td><td>' + numberWithCommas(val.diferencia) + '</td></tr>');
			});
			aperturaTabla2();
			$("#table_2").attr('data-apertura', 'Oficina de Ventas');
		});
	};
	if (apertura=='Zona de Ventas' && nivel_ops.length == 2) {
		$("#apertura_table_2").text('Oficina de Ventas');
		url = '/aperturamas/' + $("#periodo").val() + '/cadenazona/' + $("#table_1").data('nivel') + '/' + $(this).data('filtro') + '/';
		$.getJSON(url, function(data){
			$.each(data.tabla, function(key, val){
				if (val.descuento < -15) {
					var color = "color_naranjo";
				}else{
					var color = "color_azul";
				};
				$("#table_2 tbody").append('<tr data-filtro=' + val.oficina__codigo + ' class=' + color + '><td>' + val.oficina + '</td><td>' + numberWithCommas(val.kilos) + '</td><td>' + numberWithCommas(val.netos) + '</td><td>' + numberWithCommas(val.netos_esperados) + '</td><td>' + numberWithCommas(val.facturado) + '</td><td>' + numberWithCommas(val.lista) + '</td><td>' + val.descuento.toString().replace('.', ',') + '%</td><td>' + numberWithCommas(val.diferencia) + '</td></tr>');
			});
			aperturaTabla2();
			$("#table_2").attr('data-apertura', 'Oficina de Ventas');
		});
	};
	if (apertura == 'Tipo de Cliente') {
		if ($(this).data('filtro') == 20) {
			$("#apertura_table_2").text('Cadena');
			$("#table_2").attr('data-apertura', 'Cadena');
		}else{
			$("#apertura_table_2").text('Categoría Cliente');
			$("#table_2").attr('data-apertura', 'Categoría Cliente');
		};
		url = '/aperturamas/' + $("#periodo").val() + '/zonatipo/' + $("#table_1").data('nivel') + '/' + $(this).data('filtro') + '/';
		$.getJSON(url, function(data){
			$.each(data.tabla, function(key, val){
				if (val.descuento < -15) {
					var color = "color_naranjo";
				}else{
					var color = "color_azul";
				};
				$("#table_2 tbody").append('<tr data-filtro=' + val.id_tipo + ' class=' + color + '><td>' + val.tipo + '</td><td>' + numberWithCommas(val.kilos) + '</td><td>' + numberWithCommas(val.netos) + '</td><td>' + numberWithCommas(val.netos_esperados) + '</td><td>' + numberWithCommas(val.facturado) + '</td><td>' + numberWithCommas(val.lista) + '</td><td>' + val.descuento.toString().replace('.', ',') + '%</td><td>' + numberWithCommas(val.diferencia) + '</td></tr>');
			});
			aperturaTabla2();
		});
	};
	$("#table_2").show();
});

$("#table_1_reset button").on('click', function(){
	$("#table_1 tr").show();
	$("#table_2 tbody").html('');
	$("#table_2").hide();
	$("#table_2_reset button").hide();
	$("#table_3 tbody").html('');
	$("#table_3").hide();
	$("#table_3_reset button").hide();
	$("#table_4 tbody").html('');
	$("#table_4").hide();
	$("#table_4_reset button").hide();
	$("#table_5 tbody").html('');
	$("#table_5").hide();
	$("#dispersion").hide();
	$(this).hide();
});

function aperturaTabla2(){
	$("#table_2 tbody tr").on('click', function(){
		$("#table_3 tbody").html('');
		$("#table_3").hide();
		$("#table_3_reset button").hide();
		$("#table_4 tbody").html('');
		$("#table_4").hide();
		$("#table_4_reset button").hide();
		$("#table_5 tbody").html('');
		$("#table_5").hide();
		$("#dispersion").hide();
		var apertura = $("#table_2").data('apertura');
		var nivel_ops = "" + $("#table_2").data('nivel');
		$("#table_3 tbody").html('');
		$(this).siblings().hide();
		$("#table_2_reset button").css('display', 'block');
		if (apertura=='Oficina de Ventas' && nivel_ops.length != 2) {
			$("#apertura_table_3").text('Tipo de Cliente');
			url = '/aperturamas/' + $("#periodo").val() + '/nivel2oficina/' + $("#table_2").data('nivel') + '/' + $(this).data('filtro') + '/';
			$.getJSON(url, function(data){
				$.each(data.tabla, function(key, val){
					if (val.descuento < -15) {
						var color = "color_naranjo";
					}else{
						var color = "color_azul";
					};
					$("#table_3 tbody").append('<tr data-filtro=' + val.oficina__codigo + val.tipo_id +' class=' + color + '><td>' + val.tipo + '</td><td>' + numberWithCommas(val.kilos) + '</td><td>' + numberWithCommas(val.netos) + '</td><td>' + numberWithCommas(val.netos_esperados) + '</td><td>' + numberWithCommas(val.facturado) + '</td><td>' + numberWithCommas(val.lista) + '</td><td>' + val.descuento.toString().replace('.', ',') + '%</td><td>' + numberWithCommas(val.diferencia) + '</td></tr>');
				});
				aperturaTabla3();
				$("#table_3").attr('data-apertura', 'Tipo de Cliente');
			});
		};
		if (apertura=='Oficina de Ventas' && nivel_ops.length == 2) {
			$("#apertura_table_3").text('Sector');
			url = '/aperturamas/' + $("#periodo").val() + '/cadenaoficina/' + $("#table_2").data('nivel') + '/' + $(this).data('filtro') + '/';
			$.getJSON(url, function(data){
				$.each(data.tabla, function(key, val){
					if (val.descuento < -15) {
						var color = "color_naranjo";
					}else{
						var color = "color_azul";
					};
					$("#table_3 tbody").append('<tr data-filtro=' + val.oficina__codigo + val.tipo_id +' class=' + color + '><td>' + val.tipo + '</td><td>' + numberWithCommas(val.kilos) + '</td><td>' + numberWithCommas(val.netos) + '</td><td>' + numberWithCommas(val.netos_esperados) + '</td><td>' + numberWithCommas(val.facturado) + '</td><td>' + numberWithCommas(val.lista) + '</td><td>' + val.descuento.toString().replace('.', ',') + '%</td><td>' + numberWithCommas(val.diferencia) + '</td></tr>');
				});
				aperturaTabla3();
				$("#table_3").attr('data-apertura', 'Sector');
			});
		};
		if (apertura == 'Categoría Cliente' || apertura == 'Cadena') {
			$("#apertura_table_3").text('Sector');
			url = '/aperturamas/' + $("#periodo").val() + '/zonatipocadena/' + $("#table_2").data('nivel') + '/' + $(this).data('filtro') + '/';
			$.getJSON(url, function(data){
				$.each(data.tabla, function(key, val){
					if (val.descuento < -15) {
						var color = "color_naranjo";
					}else{
						var color = "color_azul";
					};
					$("#table_3 tbody").append('<tr data-filtro=' + n(val.sector_id) + val.tipo +' class=' + color + '><td>' + val.sector + '</td><td>' + numberWithCommas(val.kilos) + '</td><td>' + numberWithCommas(val.netos) + '</td><td>' + numberWithCommas(val.netos_esperados) + '</td><td>' + numberWithCommas(val.facturado) + '</td><td>' + numberWithCommas(val.lista) + '</td><td>' + val.descuento.toString().replace('.', ',') + '%</td><td>' + numberWithCommas(val.diferencia) + '</td></tr>');
				});
				aperturaTabla3();
				$("#table_3").attr('data-apertura', 'Sector');
			});
		};
		$("#table_3").show();
	});
}

$("#table_2_reset button").on('click', function(){
	$("#table_2 tr").show();
	$("#table_3 tbody").html('');
	$("#table_3").hide();
	$("#table_3_reset button").hide();
	$("#table_4 tbody").html('');
	$("#table_4").hide();
	$("#table_4_reset button").hide();
	$("#table_5 tbody").html('');
	$("#table_5").hide();
	$("#dispersion").hide();
	$(this).hide();
});

function aperturaTabla3(){
	$("#table_3 tbody tr").on('click', function(){
		data_nivel = "" + $("#table_3").data('nivel');
		$("#table_4 tbody").html('');
		$("#table_4").hide();
		$("#table_4_reset button").hide();
		$("#table_5 tbody").html('');
		$("#table_5").hide();
		$("#dispersion").hide();
		var apertura = $("#table_3").data('apertura');
		$("#table_4 tbody").html('');
		$(this).siblings().hide();
		$("#table_3_reset button").css('display', 'block');
		if (apertura=='Tipo de Cliente') {
			if ($(this).data('filtro').substr(4, 2) == '20') {
				$("#apertura_table_4").text('Cadena');
				$("#table_4").attr('data-apertura', 'Cadena');
			}else{
				$("#apertura_table_4").text('Categoría Cliente');
				$("#table_4").attr('data-apertura', 'Categoría Cliente');
			};
			url = '/aperturamas/' + $("#periodo").val() + '/nivel2oficinatipo/' + $("#table_3").data('nivel') + '/' + $(this).data('filtro') + '/';
			$.getJSON(url, function(data){
				$.each(data.tabla, function(key, val){
					if (val.descuento < -15) {
						var color = "color_naranjo";
					}else{
						var color = "color_azul";
					};
					$("#table_4 tbody").append('<tr data-filtro=' + val.oficina__codigo + val.tc + val.id_tipo + ' class=' + color + '><td>' + val.tipo + '</td><td>' + numberWithCommas(val.kilos) + '</td><td>' + numberWithCommas(val.netos) + '</td><td>' + numberWithCommas(val.netos_esperados) + '</td><td>' + numberWithCommas(val.facturado) + '</td><td>' + numberWithCommas(val.lista) + '</td><td>' + val.descuento.toString().replace('.', ',') + '%</td><td>' + numberWithCommas(val.diferencia) + '</td></tr>');
				});
				aperturaTabla4();
			});
		};
		if (apertura == 'Sector' && (data_nivel.substr(0, 1) != 'T' && data_nivel.substr(0, 1) != 'V')) {
			$("#apertura_table_4").text('Nivel 2');
			url = '/aperturamas/' + $("#periodo").val() + '/cadenaoficinasector/' + $("#table_3").data('nivel') + '/' + $(this).data('filtro') + '/';
			$.getJSON(url, function(data){
				$.each(data.tabla, function(key, val){
					if (val.descuento < -15) {
						var color = "color_naranjo";
					}else{
						var color = "color_azul";
					};
					$("#table_4 tbody").append('<tr data-filtro=' + val.oficina__codigo + val.id_nivel2 + ' class=' + color + '><td>' + val.tipo + '</td><td>' + numberWithCommas(val.kilos) + '</td><td>' + numberWithCommas(val.netos) + '</td><td>' + numberWithCommas(val.netos_esperados) + '</td><td>' + numberWithCommas(val.facturado) + '</td><td>' + numberWithCommas(val.lista) + '</td><td>' + val.descuento.toString().replace('.', ',') + '%</td><td>' + numberWithCommas(val.diferencia) + '</td></tr>');
				});
				aperturaTabla4();
				$("#table_4").attr('data-apertura', 'Nivel 2');
			});
		};
		if (apertura == 'Sector' && (data_nivel.substr(0, 1) == 'T' || data_nivel.substr(0, 1) == 'V')) {
			$("#apertura_table_4").text('Nivel 2');
			url = '/aperturamas/' + $("#periodo").val() + '/zonatipocadenasector/' + $("#table_3").data('nivel') + '/' + $(this).data('filtro') + '/';
			$.getJSON(url, function(data){
				$.each(data.tabla, function(key, val){
					if (val.descuento < -15) {
						var color = "color_naranjo";
					}else{
						var color = "color_azul";
					};
					$("#table_4 tbody").append('<tr data-filtro=' + n(val.sector_id) + val.tipo_id + val.id_nivel2 + ' class=' + color + '><td>' + val.nivel2 + '</td><td>' + numberWithCommas(val.kilos) + '</td><td>' + numberWithCommas(val.netos) + '</td><td>' + numberWithCommas(val.netos_esperados) + '</td><td>' + numberWithCommas(val.facturado) + '</td><td>' + numberWithCommas(val.lista) + '</td><td>' + val.descuento.toString().replace('.', ',') + '%</td><td>' + numberWithCommas(val.diferencia) + '</td></tr>');
				});
				aperturaTabla4();
				$("#table_4").attr('data-apertura', 'Nivel 2');
			});
		};
		$("#table_4").show();
	});
}

$("#table_3_reset button").on('click', function(){
	$("#table_3 tr").show();
	$("#table_4 tbody").html('');
	$("#table_4").hide();
	$("#table_4_reset button").hide();
	$("#table_5 tbody").html('');
	$("#table_5").hide();
	$("#dispersion").hide();
	$(this).hide();
});

function aperturaTabla4(){
	$("#table_4 tbody tr").on('click', function(){
		$("#table_5 tbody").html('');
		$("#table_5").hide();
		$("#dispersion").hide();
		var apertura = $("#table_4").data('apertura');
		$("#table_5 tbody").html('');
		$(this).siblings().hide();
		$("#table_4_reset button").css('display', 'block');
		if (apertura=='Categoría Cliente' || apertura=='Cadena') {
			$("#apertura_table_5").text('Material');
			url = '/aperturamas/' + $("#periodo").val() + '/nivel2oficinatipomaterial/' + $("#table_4").data('nivel') + '/' + $(this).data('filtro') + '/';
			$.getJSON(url, function(data){
				$.each(data.tabla, function(key, val){
					if (val.descuento < -15) {
						var color = "color_naranjo";
					}else{
						var color = "color_azul";
					};
					$("#table_5 tbody").append('<tr data-filtro=' + val.dispersion + ' class=' + color + '><td>' + val.material + '</td><td>' + numberWithCommas(val.kilos) + '</td><td>' + numberWithCommas(val.netos) + '</td><td>' + numberWithCommas(val.netos_esperados) + '</td><td>' + numberWithCommas(val.facturado) + '</td><td>' + numberWithCommas(val.lista) + '</td><td>' + val.descuento.toString().replace('.', ',') + '%</td><td>' + numberWithCommas(val.diferencia) + '</td></tr>');
				});
				aperturaTabla5();
			});
		};
		data_nivel = "" + $("#table_4").data('nivel');
		if(apertura == 'Nivel 2' && (data_nivel.substr(0, 1) != 'T' && data_nivel.substr(0, 1) != 'V')){
			$("#apertura_table_5").text('Material');
			url = '/aperturamas/' + $("#periodo").val() + '/cadenaoficinatipomaterial/' + $("#table_4").data('nivel') + '/' + $(this).data('filtro') + '/';
			$.getJSON(url, function(data){
				$.each(data.tabla, function(key, val){
					if (val.descuento < -15) {
						var color = "color_naranjo";
					}else{
						var color = "color_azul";
					};
					$("#table_5 tbody").append('<tr data-filtro=' + val.dispersion + ' class=' + color + '><td>' + val.material + '</td><td>' + numberWithCommas(val.kilos) + '</td><td>' + numberWithCommas(val.netos) + '</td><td>' + numberWithCommas(val.netos_esperados) + '</td><td>' + numberWithCommas(val.facturado) + '</td><td>' + numberWithCommas(val.lista) + '</td><td>' + val.descuento.toString().replace('.', ',') + '%</td><td>' + numberWithCommas(val.diferencia) + '</td></tr>');
				});
				aperturaTabla5();
			});
		};
		if (apertura == 'Nivel 2' && (data_nivel.substr(0, 1) == 'T' || data_nivel.substr(0, 1) == 'V')) {
			$("#apertura_table_5").text('Material');
			url = '/aperturamas/' + $("#periodo").val() + '/zonatipocadenasectormaterial/' + $("#table_4").data('nivel') + '/' + $(this).data('filtro') + '/';
			$.getJSON(url, function(data){
				$.each(data.tabla, function(key, val){
					if (val.descuento < -15) {
						var color = "color_naranjo";
					}else{
						var color = "color_azul";
					};
					$("#table_5 tbody").append('<tr data-filtro=' + val.dispersion + ' class=' + color + '><td>' + val.material + '</td><td>' + numberWithCommas(val.kilos) + '</td><td>' + numberWithCommas(val.netos) + '</td><td>' + numberWithCommas(val.netos_esperados) + '</td><td>' + numberWithCommas(val.facturado) + '</td><td>' + numberWithCommas(val.lista) + '</td><td>' + val.descuento.toString().replace('.', ',') + '%</td><td>' + numberWithCommas(val.diferencia) + '</td></tr>');
				});
				aperturaTabla5();
			});
		};
		$("#table_5").attr('data-apertura', 'Material');
		$("#table_5").show();
	});
}

$("#table_4_reset button").on('click', function(){
	$("#table_4 tr").show();
	$("#table_5 tbody").html('');
	$("#table_5").hide();
	$("#dispersion").hide();
	$(this).hide();
});

function aperturaTabla5(){
	$("#table_5 tbody tr").on('click', function(){
		$(".loader_background").css('display', 'flex');
		title = $(this).find("td:first").html();
		url = '/dispersion/' + $("#periodo").val() + '/' + $(this).data('filtro') + '/';
		$.getJSON(url, function(data){
			$("#dispersion").show();
			$("#dispersion").css('display', 'flex');
			build_chart();
			var series = {data: data.tabla, marker:{symbol: "circle"}, name: '% Desc. - Cliente Local', color: '#F26013'};
			chart_dispersion.addSeries(series);
			chart_dispersion.setTitle({text: title});
			$('html, body').animate({scrollTop:$(document).height()}, 'slow');
			$(".loader_background").css('display', 'none');
		});
	});
}

function n(n){
	return n > 9 ? "" + n: "0" + n;
}

function build_chart(){
	chart_dispersion = new Highcharts.Chart({
		chart: {
			type: 'scatter',
			renderTo: 'graph-disp',
			zoomType: 'xy'
        },
        credits:{
            enabled: false
        },
        title: {
            text: ''
        },
        subtitle: {
            text: ''
        },
        xAxis: {
        	allowDecimals: false,
            title: {
                enabled: true,
                text: 'Kilos Venta'
            },
            min: 0
        },
        yAxis: {
            title: {
                text: '% Descuento'
            },
            labels: {
                format: '{value}%'
            },
        },
        legend: {
            layout: 'horizontal',
            align: 'center',
            verticalAlign: 'bottom',
            floating: false,
            backgroundColor: (Highcharts.theme && Highcharts.theme.legendBackgroundColor) || '#FFFFFF'
        },
        plotOptions: {
            scatter: {
                marker: {
                    radius: 5,
                    states: {
                        hover: {
                            enabled: true,
                            lineColor: 'rgb(100,100,100)'
                        }
                    }
                },
                states: {
                    hover: {
                        marker: {
                            enabled: false
                        }
                    }
                },
                tooltip: {
                    headerFormat: '<b>{point.y:,.0f}% Descuento</b><br>',
                    pointFormat: '{point.dataLabels}'
                },
                turboThreshold: 0
            }
        }
	});
}