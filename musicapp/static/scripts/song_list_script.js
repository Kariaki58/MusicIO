document.addEventListener('DOMContentLoaded', function () {
    const playlist = document.getElementById('playlist');
    const audioPlayer = document.getElementById('audioPlayer');
  
    // Add songs to the playlist
    const songs = [
      { name: 'Final', src: '../static/musics/sarah final.mp3' },
      { name: 'Song 2', src: '../static/musics/Saweetie - Best Friend (Lyrics) FT. Doja Cat _ That_s my bestfriend she a real bad bitch (128  kbps) (1) 1.mp3' },
      { name: 'Song 3', src: '../static/musics/sarah final.mp3' },
      { name: 'Song 4', src: '../static/musics/sarah final.mp3' },
      { name: 'Song 5', src: '../static/musics/Saweetie - Best Friend (Lyrics) FT. Doja Cat _ That_s my bestfriend she a real bad bitch (128  kbps) (1) 1.mp3' },
      { name: 'Song 6', src: '../static/musics/sarah final.mp3' }
    ];
  
    songs.forEach((song) => {
      const listItem = document.createElement('li');
      listItem.textContent = song.name;
      listItem.setAttribute('data-src', song.src);
      playlist.appendChild(listItem);
    });

    // Add click event listener to the playlist
    playlist.addEventListener('click', (event) => {
      if (event.target.tagName === 'LI') {
        const audioSource = event.target.getAttribute('data-src');
        audioPlayer.src = audioSource;
        audioPlayer.play();
      }
    });
  });
  