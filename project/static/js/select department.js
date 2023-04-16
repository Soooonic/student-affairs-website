function seletDepartment() {
    var department = document.getElementById("depart");
    if(department.value == "selet department"){
        alert("Department is required!\nYou must choose your departmetn");
       
        return false;
    }
}