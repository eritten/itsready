window.addEventListener("load", ()=>{
    // menu and search button functionality 
    const menuBtn = document.querySelector(".menu-btn")
    const searchBtn = document.querySelector(".search-btn")
    const searchBar = document.querySelector(".search-form")
    const menuList = document.querySelector(".nav-list")
    
    menuBtn.addEventListener("click", toggleNav)
    searchBtn.addEventListener("click", toggleSearch)

    function toggleNav() {
        menuList.classList.toggle("active")
        removeSearch()
        if (menuList.classList.contains("active")){
            menuBtn.innerHTML = `<i class="fas fa-times"></i>`
        }else {
            menuBtn.innerHTML = `<i class="fas fa-bars"></i>`
        }
    }
    function toggleSearch() {
        searchBar.classList.toggle("active")
        removeNav()
        menuBtn.innerHTML = `<i class="fas fa-bars"></i>`
    }
    function removeSearch() {
        searchBar.classList.remove("active")
    }
    function removeNav() {
        menuList.classList.remove("active")
    }
    // disappear on scroll
    window.addEventListener("scroll", ()=>{
        menuList.classList.remove("active", screenY > 0)
        menuBtn.innerHTML = `<i class="fas fa-bars"></i>`
        removeSearch()
    })


})