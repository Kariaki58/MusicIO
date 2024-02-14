let submit = document.getElementById('submit');

function validateUser(data) {
    if (data.message === "Registration successful") {
        const songListUrl = window.location.origin + '/musicapp/templates/api_login.html';
        window.location.href = songListUrl
    } else if (data.message === "username already exist") {
        alert(data.message)
    } else {
        alert(data.message)
    }
}

submit.addEventListener('click', (e) => {
    e.preventDefault()
    let email = document.getElementById('email').value;
    let username = document.getElementById('username').value
    let password = document.getElementById('password').value;
    let comfirm_password = document.getElementById('comfirm_password').value;
    
    if (password === comfirm_password) {
        let formData = {}

        formData['email'] = email
        formData['username'] = username
        formData['password'] = password

        fetch('http://127.0.0.1:5000/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData)
        })
        .then(res => res.json())
        .then(data => {
            validateUser(data)
        })
        .catch(err => console(err))
    } else {
        alert('password don\'t match')
    }
})