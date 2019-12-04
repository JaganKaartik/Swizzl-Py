function myFunction() 
{
    var element = document.getElementById("nav");
    if(element.classList.contains("light-blue"))
    {
        element.classList.remove("light-blue");
        element.classList.add("blue-grey");
    }
    else if(element.classList.contains("blue-grey"))
    {
        element.classList.remove("blue-grey");
        element.classList.add("light-blue");
    }
}