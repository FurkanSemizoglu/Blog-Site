
 let articlesNames = document.querySelectorAll(".blog_articles_list .container .articles a ") 



function classChanger(event){
    console.log(event);
    console.log(event.target);
    let clickedElement = event.target;

    if(clickedElement.classList != "active" ){
        clickedElement.classList.toggle("active")
    }

    console.log(articlesNames.classList)
     
     articlesNames.forEach((element) => {
        element.classList.remove("active")
        console.log("its working");
    }) 
}