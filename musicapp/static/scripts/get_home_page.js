function createCard(artistName) {
    let cardDiv = document.createElement("div");
    cardDiv.className = "card";

    let playIcon = document.createElement("i");
    playIcon.className = "fa-solid fa-play";
    playIcon.id = "icon";

    let textDiv = document.createElement("div");
    textDiv.className = "text";

    let artistNameHeading = document.createElement("h3");
    artistNameHeading.className = "artist_name";
    artistNameHeading.textContent = artistName

    textDiv.appendChild(artistNameHeading);

    cardDiv.appendChild(playIcon);
    cardDiv.appendChild(textDiv);

    return cardDiv;
}

let playlistsDiv = document.querySelector(".playlists");


document.addEventListener('DOMContentLoaded', function () {
    fetch('http://127.0.0.1:5000')
        .then(response => response.json())
        .then(data => {
            for (let i = 0; i < data.length; i++) {
                playlistsDiv.appendChild(createCard(data[i].artist_name))
            }
        })
        .catch(error => console.error('Error fetching data:', error));
});
