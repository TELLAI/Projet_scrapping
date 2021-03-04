let buttEquipe = document.getElementById("equipe");
let buttDate = document.getElementById("date");
let buttf1 = document.querySelector("#f1");
let buttf2 = document.querySelector("#f2");

buttEquipe.addEventListener("click", function () {
  buttf2.style.display = "flex";
  console.log("f1");
});
buttDate.addEventListener("click", function () {
  buttf1.style.display = "flex";
  console.log("f2");
});
