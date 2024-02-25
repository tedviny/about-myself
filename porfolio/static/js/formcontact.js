let contactform = document.getElementById('contactForm');
let messageform = document.getElementById('contactMessage');
 contactform.addEventListener( 'submit',function(e){
    let emailform = document.getElementById('contactEmail');
    if (emailform.value.trim()==""){
        let myerror = document.getElementById('error');
        myerror.innerHTML = "Veuillez renseigner votre Email";
        myerror.style.color='red';
        alert("Erreur");
        e.preventDefault();
    }
}