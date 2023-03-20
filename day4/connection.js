console.log("Whats up");

function studentdb() {
  var name1 = document.getElementById("name").value;
  var age1 = document.getElementById("age").value;
  var srn1 = document.getElementById("srn").value;
  var comments1 = document.getElementById("comments").value;
  axios({
    method: "post",
    url: "http://localhost:8000/student",
    data: {
      name: name1,
      age: age1,
      srn: srn1,
      comments: comments1,
    },
  }).then((response) => {
    var store = response.data;
    console.log(response.data);
    var firstdiv = document.getElementById("empty-space");
    firstdiv.innerHTML = store;
  });
}
