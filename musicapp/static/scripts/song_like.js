let current_user = JSON.parse(localStorage.getItem('current_user'));
let likedSongs = [];


function updateLikeState(songId) {
    let likeButton = document.getElementById(`heart-${songId}`);
    if (likedSongs.includes(songId)) {
        likeButton.className = "fa-solid fa-heart";
    } else {
        likeButton.className = "fa-regular fa-heart";
    }
}

// song_list.forEach(song => {
//     updateLikeState(song.id);
// });

function likeSong(id) {
    let formData = new FormData();
    formData.append('user', current_user.id);

    fetch(`http://127.0.0.1:5000/like/${id}`, {
        method: 'POST',
        body: formData
    })
    .then(res => res.json())
    .then(data => {
        if (data['liked']) {
            likedSongs.push(id);
        } else {
            likedSongs = likedSongs.filter(songId => songId !== id);
        }
        updateLikeState(id);
    })
    .catch(err => {
        alert("Could not like song");
    });
}
