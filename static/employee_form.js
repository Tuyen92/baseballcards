/* When the user clicks on the button,
toggle between hiding and showing the dropdown content */
function showOptions(options) {
  document.getElementById(options).classList.toggle("show");
}

function showHardSearch() {
    document.getElementById("hard_options").classList.toggle("show");
}

function showSoftSearch() {
    document.getElementById("soft_options").classList.toggle("show");
}

function showLanguage() {
  document.getElementById("language_options").classList.toggle("show");
}

function filterSearch(input_id, options) {
  var input, filter, ul, li, a, i;
  input = document.getElementById(input_id);
  filter = input.value.toUpperCase();
  div = document.getElementById(options);
  a = div.getElementsByTagName("a");
  for (i = 0; i < a.length; i++) {
    txtValue = a[i].textContent || a[i].innerText;
    if (txtValue.toUpperCase().indexOf(filter) > -1) {
      a[i].style.display = "";
    } else {
      a[i].style.display = "none";
    }
  }
}
  
function filterSoftskills() {
  var input, filter, ul, li, a, i;
  input = document.getElementById("skill");
  filter = input.value.toUpperCase();
  div = document.getElementById("soft_options");
  a = div.getElementsByTagName("a");
  for (i = 0; i < a.length; i++) {
    txtValue = a[i].textContent || a[i].innerText;
    if (txtValue.toUpperCase().indexOf(filter) > -1) {
      a[i].style.display = "";
    } else {
      a[i].style.display = "none";
    }
  }
}

function filterHardskills() {
  var input, filter, ul, li, a, i;
  input = document.getElementById("skill");
  filter = input.value.toUpperCase();
  div = document.getElementById("hard_options");
  a = div.getElementsByTagName("a");
  for (i = 0; i < a.length; i++) {
    txtValue = a[i].textContent || a[i].innerText;
    if (txtValue.toUpperCase().indexOf(filter) > -1) {
      a[i].style.display = "";
    } else {
      a[i].style.display = "none";
    }
  }
}

function filterLanguages() {
  var input, filter, ul, li, a, i;
  input = document.getElementById("language");
  filter = input.value.toUpperCase();
  div = document.getElementById("language_options");
  a = div.getElementsByTagName("a");
  for (i = 0; i < a.length; i++) {
    txtValue = a[i].textContent || a[i].innerText;
    if (txtValue.toUpperCase().indexOf(filter) > -1) {
      a[i].style.display = "";
    } else {
      a[i].style.display = "none";
    }
  }
}

function choose(data, input_id, options) {
  var input = document.getElementById(input_id)
  input.value = data
  showOptions(options)
}

$(document).ready(function() {
  $('#rateMe2').mdbRate();
});