
$('#copy-alert-message').hide();

function alertMessage(eName){
    $(eName).show();

    $(eName).slideUp(1000, function(){

    });
    
    
}

$(document).ready(function(){

    $('#copy-btn').click(function(){
        
        var clipboard = new Clipboard('#copy-btn');

        alertMessage('#copy-alert-message');
    });
});