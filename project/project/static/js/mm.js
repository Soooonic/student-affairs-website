let elems = document.getElementById("confirm");
elems.onclick=function () {
    let confirmAction = confirm("Are you sure to Delete?");
        if (confirmAction) {
          alert("Delete successfully");
        } else {
          alert("Delete canceled");
        }
  };


  let sub = document.getElementById("save");
  sub.onclick = function(){
  let sav = true ;
  if (sav) {
    alert("Submit successfully");
  } 

  };



  let ser =document.getElementById("search")
  ser.onsubmit =function(e){
      let ID_valid = false ;
      let Name_valid = false ;
      if(ID_valid == false || Name_valid == false ){
          e.preventDefault();

      }
  };


