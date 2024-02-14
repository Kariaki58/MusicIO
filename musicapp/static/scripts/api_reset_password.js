let submitBtn = document.getElementById('submit')


submitBtn.addEventListener('click', (e) => {
    e.preventDefault()
    let email = document.getElementById('email').value
    
    let formData = new FormData()

    formData.append('reset_email', email)

    fetch('http://127.0.0.1:5000/reset_password', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => alert(data.message))
        .catch(err => alert("An error occurred: " + err));
})
