let button=document.querySelector(".button")
let sidedrawer=document.querySelector(".sidedrawercontainer")

button.onclick=()=>{
    sidedrawer.classList.toggle("sidedrawercontainervisible");
}

let viewbutton=document.querySelector(".viewbutton")
viewbutton.onclick=async (e)=>{
    console.log("view button clicked")
    sidedrawer.classList.toggle("sidedrawercontainervisible");
    //here we make an api call to the server and we view the video in the right side
    let url=e.target.getAttribute("url")
    console.log(url)
    let response= await fetch("/feed", {
        method:'POST',
        headers:{
            'Content-Type':'application/json'
        },
        body:JSON.stringify({'url':url})
    })
    let data=await response.json()
    console.log(data)

}