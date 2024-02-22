let btn = document.getElementById('change-name')
let currentUser = JSON.parse(localStorage.getItem('current_user'))['id']

btn.addEventListener('click', (e) => {
    e.preventDefault()
    let playlistName = document.getElementById('playlist-name').value
    let formData = new FormData()
    formData.append('current_user', currentUser)
    if (playlistName === '') {
        alert('empty playlist name');
    } else {
        
        formData.append('playlist_name', playlistName)

        fetch('http://127.0.0.1:5000/update_playlist_name', {
            method: 'POST',
            body: formData
        })
        .then(res => res.json())
        .then(data => {
            console.log(data)
            alert(data['message'])
        })
        .catch(err => alert('no playlist created'))
    }
})
