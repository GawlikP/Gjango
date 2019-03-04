var delete_character_aproved = function(button){

  if(confirm("Are u sure ?")){
    window.location.href = "/delete_character/"+button.name;
  }


}
