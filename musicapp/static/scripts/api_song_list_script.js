const urlParams = new URLSearchParams(window.location.search);
const playlistId = urlParams.get('playlistId');

let currentUser = JSON.parse(localStorage.getItem('current_user'))
let formData = new FormData()
let url = ''

if (currentUser) {
    formData.append('user', currentUser.id)    
}

if (playlistId === null) {
    url = 'http://127.0.0.1:5000/favourite'
} else {
    url = `http://127.0.0.1:5000/${playlistId}/songs`
}

formData.append('playlist_id', playlistId);

fetch(url, {
    method: 'POST',
    body: formData
})
.then(res => res.json())
.then(data => {
    data.forEach(element => {
        if (playlistId === null && currentUser !== null) {
            createElement(element.song_id, element.song_path, element.artist_name, 'none', element.liked, element.fav)
        } else {
            if (currentUser !== null) {
                if (currentUser['id'] == element.user_id) {
                    createElement(element.id, element.song_path, element.title, 'inline-block', element.liked, element.fav)
                } else {
                    createElement(element.id, element.song_path, element.title, 'none', element.liked, element.fav)
                }
            } else {
                createElement(element.id, element.song_path, element.title, 'none', element.liked, element.fav)
            }
        }
    });
    let progressBar = document.getElementById("range")
    let shuffle_song = document.getElementById("shuffle_song")
    let repeat = document.getElementById('repeat')
    let forward = document.getElementById('forward')
    let play = document.getElementById('play')
    let pause = document.getElementById('pause')
    let back = document.getElementById('back')
    let like = document.getElementById('heart')
    let download = document.getElementById('donwload')
    let title = document.getElementById('title')
    let songUl = document.getElementById('song')
    let allIcons = document.querySelectorAll('.i');
    const musicList = document.querySelectorAll(".control-music");
    let currentlyPlayingMusic = null;
    let audioElement = null;
    let music = null;

    function enablePlayMusic(id) {
        let musicElement = null;
        for (let i = 0; i < musicList.length; i++) {
            if (i > musicList.length) {
                i = 0;
            }
            const musicId = musicList[i].getAttribute("data-song-id");
            if (musicId == id) {
                musicElement = musicList[i];
            }
        }
        return musicElement;
    }

    function PlayForward() {
        nextMusicPlayer(1)
    }

    function PlayBack() {
        nextMusicPlayer(-1)
    }

    function nextMusicPlayer(next=1) {
        if (currentlyPlayingMusic) {
            let musicId = currentlyPlayingMusic.getAttribute('data-song-id');
            let nextMusicId = parseInt(musicId) + next;
            let music = enablePlayMusic(nextMusicId);

            if (music) {
                let playButton = document.getElementById('play-' + nextMusicId);
                if (playButton) {
                    playButton.click();
                    currentlyPlayingMusic.pause()
                }
            }
        }
    }

    function getMusicAttributeId() {
        let musicId = music.getAttribute('data-song-id');
        return musicId;    
    }

    function onClickPlay() {
        if (music) {
            let musicId = getMusicAttributeId();
            let id = 'play-' + musicId;
            getMusicId(id);
        }
    }

    function onClickPause() {
        if (music) {
            let musicId = getMusicAttributeId();
            let id = 'pause-' + musicId;
            getMusicId(id);
        }
    }

    function repeatPlay() {
        if (music) {
            music.loop = true;
            repeat.style.color = "green"
            repeat.addEventListener("click", () => {
                music.loop = !music.loop;
                if (music.loop) {
                    repeat.style.color = "green"
                } else {
                    repeat.style.color = "white"
                }
            })
        }
    }

    function getMusicId(id) {
        let musicId = document.getElementById(id).dataset.musicId;
        music = enablePlayMusic(musicId);
        if (/^play-\d+$/.test(id) || /^pause-\d+$/.test(id)) {
            if (/^play-\d+$/.test(id)) {
                let playId = document.getElementById(id);
                let idChange = 'pause-' + musicId;
                let pauseId = document.getElementById(idChange);

                songUl.style.display = 'block'
                playId.style.display = "none";
                play.style.display = "none";
                pauseId.style.display = "inline-block";
                pause.style.display = "inline-block";
                PlayMusic(music);
            } else if (/^pause-\d+$/.test(id)) {
                let pauseId = document.getElementById(id);
                let idChange = 'play-' + musicId;
                let playId = document.getElementById(idChange);

                pauseId.style.display = "none";
                pause.style.display = "none"
                playId.style.display = "inline-block";
                play.style.display = "inline-block";
                PauseMusic(music);
            }
            music.addEventListener('timeupdate', () => {
                currentlyPlayingMusic = music;
                
                let play = document.getElementById(id);
                let idChange = 'pause-' + musicId;
                let pause = document.getElementById(idChange);
                let value = (music.currentTime / music.duration) * 100;
                
                progressBar.value = value;
                if (music.ended) {
                    play.style.display = "inline-block";
                    pause.style.display = "none"
                    progressBar.value = 0;
                    nextMusicPlayer();
                }
            });
        }
    }

    function PlayMusic(music) {
        let musicId = getMusicAttributeId(music);
        if (currentlyPlayingMusic) {
            let currentMusicId = currentlyPlayingMusic.getAttribute('data-song-id');
            if (musicId == currentMusicId) {
                music.play();
            } else {
                currentlyPlayingMusic.pause()
                let musicId = currentlyPlayingMusic.getAttribute('data-song-id')
                let idPlay = 'play-' + musicId;
                let idPause = 'pause-' + musicId;
                let play = document.getElementById(idPlay);
                let pause = document.getElementById(idPause);

                play.style.display = "inline-block"
                pause.style.display = "none"
                music.play()
            }
        } else {
            music.play();
        }
    }

    function PauseMusic(music) {
        music.pause();
    }

    allIcons.forEach(icon => {
        icon.addEventListener("click", () => {
            getMusicId(icon.id)
        });
    });

    progressBar.addEventListener('click', function (e) {
        let clickX = e.pageX - this.offsetLeft;
        let percent = clickX / this.offsetWidth;
        music.currentTime = percent * music.duration;
    });

    play.addEventListener('click', onClickPlay);
    pause.addEventListener('click', onClickPause)
    repeat.addEventListener('click', repeatPlay);
    forward.addEventListener('click', PlayBack);
    back.addEventListener('click', PlayForward);
})
.catch(err => {
    console.log(err)
})

function createElement(id, song_path, song_title, see, liked, fav) {
    let box = document.getElementById('box')

    let playlist = document.createElement('ul');
    playlist.classList.add('playlist')

    let audio = document.createElement('audio');
    audio.classList.add('control-music');
    audio.setAttribute('data-song-id', id)

    let source = document.createElement('source');
    let pathPrefix = '../static/' + song_path
    source.setAttribute('src', pathPrefix);
    source.setAttribute('id', 'audioSource');

    audio.appendChild(source);
    let listItem = document.createElement('li');

    let div1 = document.createElement('div');

    let title = document.createElement('p');
    title.classList.add('music');
    title.setAttribute('id', `title-${id}`)
    title.style.fontSize = '1.2rem'
    title.style.fontWeight = 'bold'
    title.textContent = song_title;

    div1.appendChild(title);

    let div2 = document.createElement('div');

    let playIcon = document.createElement('i');
    playIcon.classList.add('fa-solid', 'fa-play', 'i');
    playIcon.setAttribute('id', `play-${id}`);
    playIcon.setAttribute('data-music-id', id)

    let pauseIcon = document.createElement('i');
    pauseIcon.classList.add('fa-solid', 'fa-pause', 'i');
    pauseIcon.setAttribute('id', `pause-${id}`);
    pauseIcon.setAttribute('data-music-id', id)

    let span = document.createElement('span');
    span.classList.add(`like-count-${id}`);
    span.setAttribute('id', `like-count-${id}`)

    let heartIcon = document.createElement('i');
    heartIcon.classList.add(liked, 'fa-heart', 'i');
    heartIcon.setAttribute('id', `heart-${id}`);
    heartIcon.setAttribute('onClick', `likeSong(${id})`)
    heartIcon.setAttribute('data-music-id', id)


    let trashIcon = document.createElement('i');
    trashIcon.classList.add('fa-solid', 'fa-trash-can', 'i', 'show');

    trashIcon.setAttribute('id', `trash-${id}`);
    trashIcon.style.display = see
    trashIcon.setAttribute("onClick", `deleteSong(${id})`);

    let tooltip = document.createElement('span');
    tooltip.classList.add('tooltip');
    
    let starIcon = document.createElement('i');
    starIcon.classList.add(fav, 'fa-star', 'tooltip');
    starIcon.setAttribute('id', `add-${id}`)
    starIcon.setAttribute('onClick', `addToFav(${id})`)

    let tooltipText = document.createElement('span');
    tooltipText.classList.add('tooltiptext');
    tooltipText.textContent = 'add to favorite';

    starIcon.appendChild(tooltipText);

    tooltip.appendChild(starIcon);

    div2.appendChild(playIcon);
    div2.appendChild(pauseIcon);
    div2.appendChild(heartIcon);
    div2.appendChild(span)
    div2.appendChild(trashIcon);
    div2.appendChild(tooltip);

    listItem.appendChild(div1);
    listItem.appendChild(div2);

    playlist.appendChild(listItem);

    box.appendChild(audio)
    box.appendChild(playlist)
}
