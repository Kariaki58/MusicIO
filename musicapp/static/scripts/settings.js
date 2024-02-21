let btn = document.getElementById('change-name')
console.log("settings")

btn.addEventListener('click', () => {
    let playlistName = document.getElementById('playlist-name').value
    let formData = new FormData()

    if (playlistName === '') {
        alert('empty playlist name');
    } else {
        
        formData.append('playlist_name', playlistName)

        fetch('http://127.0.0.1:5000/update_playlist_name', {
            method: 'POST',
            body: formData
        })
        .then(res => res.json())
        .then(data => alert(data['message']))
        .catch(err => alert("error occured"))
    }
})