$("#login-button").click(function(event){
    event.preventDefault();

    $('form').fadeOut(500);
    $('.wrapper').addClass('form-success');
    $('h1').text('Registering...');
    setTimeout(function(){
        window.location.href = '/process/';
    }, 1500);
});