$(document).ready(function(){
    $('.page_link').on("click", function(){
        if($(this).is("untoggled")){
            $(this).removeClass("untoggled").addClass("toggled");
        }
        else{
            $(this).removeClass("toggled").addClass("untoggled");
        }
	});
});
