function skillTab(evt, typeSkill, tabcontent, tablinks) {
  console.log("here")
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName(tabcontent);
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName(tablinks);
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(typeSkill).style.display = "block";
    evt.currentTarget.className += " active";
  }

  function loadImage(strImage, imgId) {
    var base64ImageString = strImage;
    var imgElement = document.getElementById(imgId)
    // Set the src attribute to the Base64 string
    imgElement.src = 'data:image/png;base64,' + base64ImageString;
    console.log(imgElement.src)
    return imgElement.src

    // Append the Image element to the HTML document
}