function deleteSong(id) {
    let intId = parseInt(id)
    fetch(`http://127.0.0.1:5000/playlists/songs/${intId}`, {
        method: 'POST',
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        alert(data.message)
        location.reload()
    })
    .catch(error => {
        console.error('Error deleting song:', error);
    });
}
