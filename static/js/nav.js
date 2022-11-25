function menuButtonToggle(x) {
  if( document.getElementById("options").style.display == 'none'){
      document.getElementById("options").style.display = 'block';
      x.classList.toggle("change");
  }
  else if(document.getElementById("options").style.display == 'block'){
      document.getElementById("options").style.display = 'none';
    x.classList.toggle("change");
  }
  else{
    document.getElementById("options").style.display = 'block';
    x.classList.toggle("change");
  }
}
