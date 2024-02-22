let inputSubmit = document.getElementById("submit")
let current_user = JSON.parse(localStorage.getItem('current_user'));
let playlistName = document.getElementById('playlist_name')


if (current_user) {
    let localData = localStorage.getItem(`playlist ${current_user['id']}`)

    if (localData) {
        if (localData.split(' ')[1] == current_user['id']) {
            playlistName.style.display = 'none'
        }
    }
}


function RenderPlaylist(playlistName, element) {
    let cardDiv = document.createElement("div");
    cardDiv.classList.add("card");

    let iconElement = document.createElement("i");
    iconElement.classList.add("fa-solid", "fa-play");
    iconElement.id = "icon";

    let textDiv = document.createElement("div");
    textDiv.classList.add("text");

    let headingElement = document.createElement("h4");
    headingElement.textContent = playlistName;

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
        RenderPlaylist(element.playlist_name, element)
    });
})
.catch(err => alert("error occured"))

inputSubmit.addEventListener('click', (e) => {
    e.preventDefault();
    let localData = localStorage.getItem(`playlist ${current_user['id']}`)


    let fileInput = document.getElementById('fileInput').files[0];
    let title = document.getElementById('title').value;
    let playlistName = document.getElementById('playlist_name').value;
    let artistName = document.getElementById("artist_name").value;
    let formData = new FormData();

    if (fileInput === undefined) {
        alert('no file selected')
    } else if (title === "") {
        alert('add a song title')
    } else if (playlistName === "" && localData === `playlist ${current_user['id']}`) {
        alert('add a playlist name')
    } else if (artistName === "") {
        alert('artist name is empty')
    }
    if (fileInput != undefined && title != "" && (playlistName != "" || localData == `playlist ${current_user['id']}`) && artistName != ""){
        formData.append('fileInput', fileInput);
        formData.append('title', title);
        formData.append('playlistName', playlistName);
        formData.append('artistName', artistName);

        if (current_user != null) {
            formData.append('user', current_user['id']);
            fetch('http://127.0.0.1:5000/playlist', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                localStorage.setItem(`playlist ${current_user['id']}`, `playlist ${current_user['id']}`)
                alert(data['message'])
            })
            .catch(err => alert("An error occurred: " + err));
        } else {
            window.location.href = window.location.origin + '/musicapp/templates/api_login.html';
        }
    }
});
