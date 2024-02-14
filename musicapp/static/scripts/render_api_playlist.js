let inputSubmit = document.getElementById("submit")
let UploadPermit = false


function RenderPlaylist(data, element) {
    let cardDiv = document.createElement("div");
    cardDiv.classList.add("card");

    let iconElement = document.createElement("i");

    iconElement.classList.add("fa-solid", "fa-play");
    iconElement.id = "icon";

    let textDiv = document.createElement("div");
    textDiv.classList.add("text");

    let headingElement = document.createElement("h4");
    headingElement.textContent = data;

    textDiv.appendChild(headingElement);

    cardDiv.appendChild(iconElement);
    cardDiv.appendChild(textDiv);

    let playlistsDiv = document.querySelector(".playlists");
    playlistsDiv.appendChild(cardDiv);

    cardDiv.addEventListener('click', () => {
        let playlistId = element.id
        window.location.href = `api_show_song.html?playlistId=${playlistId}`;
    })
}

fetch('http://127.0.0.1:5000/playlist', {
    method: 'GET'
})
.then(response => response.json())
.then(data => {
    data.forEach(element => {
        RenderPlaylist(element.artist_name, element)
    });
})
.catch(err => alert("error occured"))

inputSubmit.addEventListener('click', (e) => {
    e.preventDefault();
    let fileInput = document.getElementById('fileInput').files[0];
    let title = document.getElementById('title').value;
    let artistName = document.getElementById("artist_name").value;
    let formData = new FormData();
    let current_user = JSON.parse(localStorage.getItem('current_user'));

    formData.append('fileInput', fileInput);
    formData.append('title', title);
    formData.append('artistName', artistName);

    if (current_user != null) {
        formData.append('user', current_user['id']);
        fetch('http://127.0.0.1:5000/playlist', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => console.log(data))
        .catch(err => alert("An error occurred: " + err));
    } else {
        window.location.href = window.location.origin + '/musicapp/templates/api_login.html';
    }
});

