let current_user_fav = JSON.parse(localStorage.getItem('current_user'));


function addToFav(id) {
    const starBtn = document.getElementById(`add-${id}`)
    let song_name = document.getElementById(`title-${id}`)
    const formData = new FormData()

    formData.append('current_user', current_user_fav.id)
    formData.append('song_name', song_name.innerHTML)

    fetch(`http://127.0.0.1:5000/favourite/${id}`, {
        method: 'POST',
        body: formData
    })
    .then(res => res.json())
    .then(data => {
        console.log(data)
        if (data["starred"]) {
            starBtn.className = 'fa-solid fa-star'
        } else {
            starBtn.className = 'fa-regular fa-star'
        }
    })
}
