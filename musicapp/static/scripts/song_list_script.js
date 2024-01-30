// Javascript code for the song lists
document.addEventListener("DOMContentLoaded", function() {
    const songs = [
        { title: "Confident", artist: "Alessia Cara" },
        { title: "Tonight", artist: "Glee Cast" },
        { title: "Best Friend", artist: "Nino" },
        { title: "", artist: "" },
        { title: "", artist: "" },
    ];

    function renderSongs() {
        const songListContainer = document.getElementById("songList");

        songs.forEach(song => {
            const songDiv = document.createElement("div");
            songDiv.classList.add("song");

            const titleDiv = document.createElement("div");
            titleDiv.classList.add("song-title");
            titleDiv.textContent = song.artist;

            const artistDiv = document.createElement("div");
            artistDiv.classList.add("song-artist");
            artistDiv.textContent = song.artist;

            songDiv.appendChild(titleDiv);
            songDiv.appendChild(artistDiv);
            songListContainer.appendChild(songDiv);
        });
    }
    renderSongs();
});