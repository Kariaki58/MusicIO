document.addEventListener('DOMContentLoaded', function () {
    fetch('http://127.0.0.1:5000')
        .then(response => response.json())
        .then(data => {
            const allArtistName = document.querySelectorAll('.artist_name');
            const allArtistTitle = document.querySelectorAll('.artist_title')
            console.log(data)
            for (let i = 0; i < data.length; i++) {
                allArtistName.forEach((name) => {
                    console.log(name)
                    console.log(data[i].artist_name)
                    name.innerHTML = data[i].artist_name;
                })
            }
            allArtistTitle.forEach((name) => {
                for (let i = 0; i < data.length; i++) {
                    name.innerHTML = data[i].title;
                }
            })
        })
        .catch(error => console.error('Error fetching data:', error));
});
