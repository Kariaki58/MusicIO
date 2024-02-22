let playlistDel = document.getElementById('del-playlist')
let accountDel = document.getElementById('del-account')
let user_id = JSON.parse(localStorage.getItem('current_user'))['id']
let formData = new FormData()


formData.append('current_user', user_id)


playlistDel.addEventListener('click', (e) => {
    e.preventDefault()
    fetch('http://127.0.0.1:5000/playlists/del', {
        method: 'DELETE',
        body: formData
    })
    .then(res => res.json())
    .then(data => {
        if (data['success'] == true) {
            alert(data['message'])
            localStorage.removeItem(`playlist ${user_id}`)
        } else {
            alert(data['message'])
        }
    }
    )
    .catch(err => alert("No available playlist"))
})

accountDel.addEventListener('click', (e) => {
    e.preventDefault()
    fetch('http://127.0.0.1:5000/users/del', {
        method: 'DELETE',
        body: formData
    })
    .then(res => res.json())
    .then(data => {
        if (data['success'] == true) {
            alert(data['message'])
            localStorage.removeItem('current_user')
            window.location.href = window.location.origin + '/musicapp/templates/api_register.html';
        } else {
            alert(data['message'])
        }
    }
    )
    .catch(err => alert("Account Deleted"))
})
