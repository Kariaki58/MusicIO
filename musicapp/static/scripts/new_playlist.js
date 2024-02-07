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
    if (/^heart-\d+$/.test(id)) {
        let likeId = document.getElementById(id);
        let idChange = 'heart-x-' + musicId
        let heartSolid = document.getElementById(idChange)
        likeId.style.display = 'none'
        heartSolid.style.display = 'inline-block'
    } else if (/^heart-x-\d+$/.test(id)) {
        let likeId = document.getElementById(id);
        let idChange = 'heart-' + musicId
        let heartSolid = document.getElementById(idChange)
        likeId.style.display = 'none'
        heartSolid.style.display = 'inline-block'
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

window.onload = function() {
    let retrievedJsonString = localStorage.getItem('key');
    let retrievedDictionary = JSON.parse(retrievedJsonString);

    if (retrievedDictionary["songUl"]) {
        songUl.style.display = "block"
    }
    music = enablePlayMusic(retrievedDictionary["currentlyPlayingMusic"])
    music.currentTime = retrievedDictionary['songrangepos']
}

window.onbeforeunload = function() {
    let block = 0;
    let repeatIcon = false;
    if (songUl.style.display == "block") {
        block = 1
    }
    if (repeat.style.color == "green") {
        repeatIcon = true;
    }
    let dictionary = {"songUl": block, "currSong": 1, "songrangepos": music.currentTime, repeat: repeatIcon, "currentlyPlayingMusic": music.getAttribute('data-song-id')}
    localStorage.setItem("key", JSON.stringify(dictionary))
}
