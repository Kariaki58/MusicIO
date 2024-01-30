document.addEventListener('DOMContentLoaded', function () {
    fetch('http://127.0.0.1:5000')
        .then(response => response.json())
        .then(data => {
            const allArtistName = document.querySelectorAll('.artist_name');
            const allArtistTitle = document.querySelectorAll('.artist_title');
            for (let i = 0; i < data.length; i++) {
                if (allArtistName[i]) {
                    allArtistName[i].innerHTML = data[i].artist_name;
                }
                if (allArtistTitle[i]) {
                    allArtistTitle[i].innerHTML = data[i].title;
                }
            }
        })
        .catch(error => console.error('Error fetching data:', error));
});
