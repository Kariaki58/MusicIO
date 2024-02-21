let playlistDel = document.getElementById('del-playlist')
let accountDel = document.getElementById('del-account')
let user_id = localStorage.getItem('current_user')['id']
let formData = new FormData()


formData.append('current_user', user_id)

playlistDel.addEventListener('click', (e) => {
    e.preventDefault()
    fetch('http://127.0.0.1:5000/playlists/del', {
        method: 'DELETE',
        body: user_id
    })
    .then(res => res.json())
    .then(data => {
        if (data['success'] == true) {
            alert(data['message'])
        }
    }
    )
    .catch(err => alert("an issue occured"))
})

accountDel.addEventListener('click', (e) => {
    e.preventDefault()
    fetch('http://127.0.0.1:5000/playlists/del', {
        method: 'DELETE',
        body: user_id
    })
    .then(res => res.json())
    .then(data => alert(data['message']))
    .catch(err => alert("an issue occured"))
})
