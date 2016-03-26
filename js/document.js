//nav to show options regarding about us 	
    
    function display(param){
        document.getElementById(param).style.visibility= "visible";
    }
    function hide(param){
        document.getElementById(param).style.visibility= "hidden";
    }

$(document).ready(function(){
    $('#cepcode').keyup(function(event){
            if(isNaN(String.fromCharCode(event.which))){
            var value = $(this).val();

            $(this).val(value.substr(0,value.length-1));
        }
      });
});

$(document).ready(function(){
    $(".vertical-line, .right-line").on({
    focusin: function(){
        $(this).css("background-color", "#fff");
    },
    focusout: function(){
        $(this).css("background-color", "#e6e6e6")
    }
  });
});
/*function carousel*/

