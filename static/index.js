
function loadDoc() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        document.getElementById("suggestions").innerHTML = this.responseText;
      }
    };
    user_value = document.getElementById("query").value
    console.log("loadDoc")
    xhttp.open("GET", "/suggestions?query=" + user_value);
    xhttp.send();
  }
