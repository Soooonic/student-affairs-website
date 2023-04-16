function checkSignUpForm() {
    var name = document.getElementById("Name");
    var email = document.getElementById("Email");
    var id = document.getElementById("ID");
    var Gpa = document.getElementById("gpa");
    var gen = document.getElementById("gender");
    var phone = document.getElementById("phone");
// name validation
    if (name.value == ""||name.value==null) {
        alert("Name can not be blank");
        document.getElementById("Name").focus();
        return false;
    }
    x =/[0-9]/;
    if(x.test(name.value)){
        alert("a valid name does not contain numbers");
        document.getElementById("Name").focus();
        return false ;
    }
    

// email validation
    if (email.value==""||email.value==null) {
        alert("Email can not be blank");
        document.getElementById("Email").focus();
        return false;
    }
    var mailformat = /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/;
    if(!mailformat.test(email.value)){
        alert("Enter a valid Email like this (page123@fcai.com)");
        document.getElementById("Email").focus();
        return false;
    }

// id validation
    if(id.value.length<8||id.value.length>8){
     alert("the length of the id must contain exactly 8 numbers");
     document.getElementById("ID").focus();
     return false;
    }
    
    // gpa validation 
    if(Gpa.value<0||Gpa.value>4){
        alert("Gpa value must between 0 and 4 ");
        document.getElementById("gpa").focus();
        return false ;
    }

    // phone validation
    if(phone.value.length<11||phone.value.length<11){
        alert("the length of the phone number must contain exactly 11 numbers");
        document.getElementById("phone").focus();
        return false;
    }
    var validNum =/[a-z]/;
    if(validNum.test(phone.value)){
        alert("phone number must contain only numbers");
        document.getElementById("phone").focus();
        return false ;

    }






}