function myFunction() {
  let x = document.getElementById("name").value;
  // If x is Not a Number or less than one or greater than 10
  let text;
  if (x === "") {
    text = "Input not valid";
  } else {
    text = "Input OK";
  }
  document.getElementById("demo").innerHTML = text;
}

function validateForm() {
  let x = document.forms["myForm"]["fname"].value;
  if (x == "") {
    alert("Name must be filled out");
    return false;
  } else {
    document.getElementById("demo").innerHTML = x;
    return false;
  }
}
