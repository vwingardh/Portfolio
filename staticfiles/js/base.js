function bump() {
    var element = document.getElementById("bumpy");
    
    element.className = "bumpit";
}
  
  function erase() {
    var e = document.getElementById("bumpy");
      
    if (e.className == "bumpit"); {
    e.className = "done";
    }
}