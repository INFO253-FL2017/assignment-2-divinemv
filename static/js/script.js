function myFunction() {
    var firstname = document.getElementById('firstname').value;
    var lastname = document.getElementById('lastname').value;
    var messageSub = document.getElementById('subject').value;
    var message = document.getElementById('message').value;
    var mes = "Please fill in";
    var missingFields = 0;
    if (firstname == "") {
        mes = mes + " First Name";
        missingFields = missingFields + 1;
    } 
    if (lastname == "") {
        if (missingFields > 0) {
            mes = mes + ","
        }
        mes = mes + " Last Name";
        missingFields = missingFields + 1;
    }
    if (messageSub == "") {
        if (missingFields > 0) {
            mes = mes + ","
        }
        mes = mes + " Subject";
        missingFields = missingFields + 1;
    }
    if (message == "") {
        if (missingFields > 0) {
            mes = mes + ","
        }
        mes = mes + " Message";
        missingFields = missingFields + 1;
    }
    if (missingFields == 0) {
        sucsess();
        return;
    } else {
        document.getElementById("oops").style.display ='block';
        document.getElementById("confirmation").style.display ='none'; 
        document.getElementById("formValidation").innerHTML = mes + "."; 
    return false;
    }
} 


function sucsess() {
    var firstname = document.getElementById('firstname').value;
    document.getElementById("Otherconfirmation").innerHTML = "Hi " + firstname + "!"; 
    document.getElementById("oops").style.display ='none';
    document.getElementById("confirmation").style.display ='block'; 
}