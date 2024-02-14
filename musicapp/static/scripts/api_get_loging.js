let submit = document.getElementById('submit')

function StoreInLocalStorage(userState) {
    localStorage.setItem('current_user', userState)
}

submit.addEventListener('click', (e) => {
    e.preventDefault()
    let email = document.getElementById('email').value;
    let password = document.getElementById('loginPassword').value;
    let formData = {}

    formData['email'] = email
    formData['password'] = password

    fetch('http://127.0.0.1:5000/login', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify(formData)
    })
    .then(res => res.json())
    .then(data => {
        if (data.length === undefined) {
            alert(data.message)
        } else {
            if (data[0].message === "login sucessful") {
                StoreInLocalStorage(JSON.stringify(data[1]))
                const songListUrl = window.location.origin + '/musicapp/templates/render_api_playlist.html';
                window.location.href = songListUrl
            } else if (data[0].message === "invalid email") {
                alert(data[0].message)
            } else {
                alert(data[0].message)
            }
        }
    })
    .catch(err => {
        alert("error occured, check your internet")
    })
})
