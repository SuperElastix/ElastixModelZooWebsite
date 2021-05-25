$(document).ready(function(){
  $('table tbody tr').click(function(){
    window.location = $(this).data('href');
    return false;
  });
});

$(document).ready(function(){

  var x = document.getElementById("albumList");
  var y = document.getElementById("dataTable");
  var album = localStorage.getItem('album')
  if (album === "true") {
    x.style.display = "none";
    y.style.display = "block";

  } else {
    x.style.display = "block";
    y.style.display = "none";

  }
});



function myFunction() {

  var x = document.getElementById("albumList");
  var y = document.getElementById("dataTable");

  if (x.style.display === "none") {
    localStorage.setItem('album', 'false'); //store state in localStorage
    x.style.display = "block";
    y.style.display = "none";

  } else {
    localStorage.setItem('album', 'true'); //store state in localStorage
    x.style.display = "none";
    y.style.display = "block";

  }
}

function sortTable(n) {
  var table,
    rows,
    switching,
    i,
    x,
    y,
    shouldSwitch,
    dir,
    switchcount = 0;
  table = document.getElementById("dataTable");
  switching = true;
  //Set the sorting direction to ascending:
  dir = "asc";
  /*Make a loop that will continue until
  no switching has been done:*/
  while (switching) {
    //start by saying: no switching is done:
    switching = false;
    rows = table.getElementsByTagName("tr");
    /*Loop through all table rows (except the
    first, which contains table headers):*/
    for (i = 1; i < rows.length - 1; i++) { //Change i=0 if you have the header th a separate table.
      //start by saying there should be no switching:
      shouldSwitch = false;
      /*Get the two elements you want to compare,
      one from current row and one from the next:*/
      x = rows[i].getElementsByTagName("td")[n];
      y = rows[i + 1].getElementsByTagName("td")[n];
      /*check if the two rows should switch place,
      based on the direction, asc or desc:*/
      if (dir == "asc") {
        if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
          //if so, mark as a switch and break the loop:
          shouldSwitch = true;
          break;
        }
      } else if (dir == "desc") {
        if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
          //if so, mark as a switch and break the loop:
          shouldSwitch = true;
          break;
        }
      }
    }
    if (shouldSwitch) {
      /*If a switch has been marked, make the switch
      and mark that a switch has been done:*/
      rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
      switching = true;
      //Each time a switch is done, increase this count by 1:
      switchcount++;
    } else {
      /*If no switching has been done AND the direction is "asc",
      set the direction to "desc" and run the while loop again.*/
      if (switchcount == 0 && dir == "asc") {
        dir = "desc";
        switching = true;
      }
    }
  }
}
