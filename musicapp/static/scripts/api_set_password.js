const urlParams = new URLSearchParams(window.location.search);
const token = urlParams.get('token');


fetch(`http://127.0.0.1:5000/confirm_password_reset/${token}`, {
    method: 'GET',
})
.then(response => {
    if (response.ok) {
        return response.json();
    }
    throw new Error('Network response was not ok.');
})
.then(data => {
    if (data.message === "token don\'t exist request a new one") {
        return new Error(data.message)
    }
})
.catch(error => {
    alert(error);
});

let submit = document.getElementById('submit');

submit.addEventListener('click', (e) => {
    e.preventDefault()
    let password = document.getElementById('loginPassword').value
    let comfirm_password = document.getElementById('loginPassword2').value
    let formData = new FormData()

    formData.append('new_password', password);
    formData.append('new_password_confirm', comfirm_password)
    formData.append('reset_token', token)

    fetch('http://127.0.0.1:5000/confirm_password', {
        method: 'POST',
        body: formData
    })
    .then(res => {
        if (res.ok) {
            return res.json()
        }
        throw new Error('Network response was not ok.');
    })
    .then(data => {
        if (data.message === "Your password has been reset successfully") {
            alert(data.message)
            window.location.href = window.location.origin + '/musicapp/templates/api_login.html';
        } else {
            alert(data.message)
        }
    })
    .catch(err => {
        console.log(err)
    })
})
