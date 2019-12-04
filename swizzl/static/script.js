function myFunction() 
{
    var element = document.getElementById("nav");
    var card = document.getElementsByClassName("card");
    var cardchildren = document.getElementsByClassName("card").children;
    var i,j;
    if(element.classList.contains("light-blue"))
    {
        element.classList.remove("light-blue");
        element.classList.add("blue-grey");
        for(i=0;i<card.length;++i)
        {
            card[i].classList.add("blue-grey");
            for (i = 0; i < c.length; i++) 
            {
                txt = txt + c[i].tagName + "<br>";
            }
            card[i].classList.add("white-text");
        }
    }
    else if(element.classList.contains("blue-grey"))
    {
        element.classList.remove("blue-grey");
        element.classList.add("light-blue");
        for(i=0;i<card.length;++i)
        {
            card[i].classList.remove("blue-grey");
            card[i].classList.remove("white-text");
        }
    }
}