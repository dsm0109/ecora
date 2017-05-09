$( document ).ready(function(){

	//Inicializacion de componentes de materialize
	$(".button-collapse").sideNav();
	$('.collapsible').collapsible();

	//Animación entrada
	$('#moneda').addClass('animated bounceIn');
	$('#agregar-amigo').addClass('animated bounceInUp');
	$('#pic_perfil').addClass('animated bounceIn');
	for(i=1; i<=14;i++){
		var txt = "#in-" + i
		$(txt).addClass('animated bounceIn');
	}

	//Inicializar monedas animacion
	$("#popUp").fadeOut(0);
	$("#malla").fadeOut(0);
	$("#moneda-1").fadeOut(0);
	$("#moneda-2").fadeOut(0);
	$("#moneda-3").fadeOut(0);
	$("#moneda-4").fadeOut(0);
	$("#moneda-5").fadeOut(0);
	$("#moneda-6").fadeOut(0);
	$("#moneda-7").fadeOut(0);
	$("#moneda-8").fadeOut(0);
	$("#moneda-9").fadeOut(0);
	$("#moneda-10").fadeOut(0);

	

	$('#moneda').one('webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend', doSomething);
	$( "#moneda" ).on( "click", function() {
		$('#moneda').addClass('animated rubberBand');
		$('#moneda').one('webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend', doSomething2);
		setTimeout(function()
		{
			$("#malla").fadeIn(3000);

		}, 1500);

		setTimeout(function()
		{
			$("#popUp").fadeIn(3000);

		}, 2000);

		setTimeout(function()
		{
			$("#moneda-1").fadeIn(2000);
			$("#moneda-2").fadeIn(2500);
			$("#moneda-3").fadeIn(1700);
			$("#moneda-4").fadeIn(2100);
			$("#moneda-5").fadeIn(2200);
			$("#moneda-6").fadeIn(2700);
			$("#moneda-7").fadeIn(1800);
			$("#moneda-8").fadeIn(2050);
			$("#moneda-9").fadeIn(2100);
			$("#moneda-10").fadeIn(1790);

		}, 4000);

		setTimeout(function()
		{
			$("#moneda-1").fadeOut(2000);
			$("#moneda-2").fadeOut(2000);
			$("#moneda-3").fadeOut(2000);
			$("#moneda-4").fadeOut(2000);
			$("#moneda-5").fadeOut(2000);
			$("#moneda-6").fadeOut(2000);
			$("#moneda-7").fadeOut(2000);
			$("#moneda-8").fadeOut(2000);
			$("#moneda-9").fadeOut(2000);
			$("#moneda-10").fadeOut(2000);
			$("#malla").fadeOut(3000);
			$("#popUp").fadeOut(3000);

		}, 8000);
	});

function doSomething(){
	$('#moneda').removeClass('animated bounceIn');
}

function doSomething2(){
	$('#moneda').removeClass('animated rubberBand');
}


});

