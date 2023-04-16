function checkSignUpForm() {
    var name = document.getElementById("search");
// name validation
    if (name.value === ""||name.value===null) {
        alert("Name can not be blank");
        document.getElementById("search").focus();
        return false;
    }
    x =/[0-9]/;
    if(x.test(name.value)){
        alert("a valid name does not contain numbers");
        document.getElementById("Name").focus();
        return false ;
    }
}