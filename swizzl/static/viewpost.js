// Function to check Sentiment Value and return which div to print

function sentimentFn() 
{
  var x = document.getElementById("0");
  if(x.style.display === "none") 
  {
    x.style.display = "block";
  } 
  else 
  {
    x.style.display = "none";
  }
}