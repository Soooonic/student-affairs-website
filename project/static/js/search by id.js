function checkSignUpForm() {
    var name = document.getElementById("Name");
    var id = document.getElementById("ID");
// name validation
    x =/[0-9]/;
    if(x.test(name.value)){
        alert("a valid name does not contain numbers");
        document.getElementById("Name").focus();
        return false ;
    }
    
// id validation
     if(id.value =="" || id.value == null){
         alert("Id is required!");
         document.getElementById("ID").focus();
         return false;
     }
    if(id.value.length<8||id.value.length>8){
     alert("the length of the id must contain exactly 8 numbers");
     document.getElementById("ID").focus();
     return false;
    }

}