function goHome() {
    window.location.href = window.location.origin + '/musicapp/templates/render_api_playlist.html';
}

let localStorageData = JSON.parse(localStorage.getItem('current_user'))
const ul = document.getElementById("base_ul");


const menuItems = [
    { label: "login", url: "api_login.html", id: "login" },
    { label: "register", url: "api_register.html", id: "register" },
    { label: "Logout", url: "", id: "logout" }
];


menuItems.forEach(item => {
    const li = document.createElement("li");
    const a = document.createElement("a");

    a.href = item.url;
    a.textContent = item.label;
    a.id = item.id;
    li.appendChild(a);
    ul.appendChild(li);
});


if (localStorageData === null) {
    let logoutElement = document.getElementById('logout')

    logoutElement.style.display = 'none'
} else {
    let loginElement = document.getElementById('login');
    let registerElement = document.getElementById('register')
    let logoutElement = document.getElementById('logout')


    registerElement.style.display = 'none'
    loginElement.style.display = 'none'
    logoutElement.addEventListener('click', () => {
        localStorage.removeItem('current_user')
    })
}