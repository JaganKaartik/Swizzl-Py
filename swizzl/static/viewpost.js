// Function to check Sentiment Value and return which div to print

function sentimentFn() 
{
  var checkBox = document.getElementById("sentiment");
  var text = document.getElementById("text");
  if(checkBox.checked == true)
  {
    text.style.display = "block";
  } 
  else 
  {
    text.style.display = "none";
  }
}