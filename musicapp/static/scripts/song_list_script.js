let progressBars = document.querySelectorAll('.range');
let allIcons = document.querySelectorAll('i');
const musicList = document.querySelectorAll(".control-music");
let currentlyPlayingMusic = null;


function isPlaying(status) {
    return status;
}

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

function nextMusicPlayer() {
    let musicId = currentlyPlayingMusic.getAttribute('data-song-id')
    let nextMusicId = parseInt(musicId) + 1;

    music = enablePlayMusic(nextMusicId);
    PlayMusic(music);
}

function getMusicId(id) {
    let musicId = document.getElementById(id).dataset.musicId;
    let music = enablePlayMusic(musicId);
    let progressBar = document.getElementById('range-' + musicId);

    
    if (/^play-\d+$/.test(id) || /^pause-\d+$/.test(id)) {
        if (/^play-\d+$/.test(id)) {
            let play = document.getElementById(id);
            let idChange = 'pause-' + musicId;
            let pause = document.getElementById(idChange);

            play.style.display = "none";
            pause.style.display = "inline-block";
            PlayMusic(music);
        } else if (/^pause-\d+$/.test(id)) {
            let pause = document.getElementById(id);
            let idChange = 'play-' + musicId;
            let play = document.getElementById(idChange);

            pause.style.display = "none";
            play.style.display = "inline-block";
            PauseMusic(music);
        }
        music.addEventListener('timeupdate', () => {
            currentlyPlayingMusic = music;
            let value = (music.currentTime / music.duration) * 100;
            let play = document.getElementById(id);
            let idChange = 'pause-' + musicId;
            let pause = document.getElementById(idChange);
            progressBar.value = value;
            if (music.ended) {
                let musicId = currentlyPlayingMusic.getAttribute('data-song-id')
                let nextMusicId = parseInt(musicId) + 1;


                play.style.display = "inline-block";
                pause.style.display = "none"
                console.log(nextMusicId)
                progressBar.value = 0;
                music = enablePlayMusic(nextMusicId);
                PlayMusic(music);
            }
        });
    }
    if (/^repeat-\d+$/.test(id)) {
        music.loop = true;
        let norepeat = document.getElementById(id);
        norepeat.style.color = "green"
        norepeat.addEventListener("click", () => {
            music.loop = !music.loop;
            if (music.loop) {
                norepeat.style.color = "green"
            } else {
                norepeat.style.color = "white"
            }
        })
    }
}

function PlayMusic(music) {
    if (currentlyPlayingMusic) {
        console.log("yes")
        let musicId = currentlyPlayingMusic.getAttribute('data-song-id')
        let idPlay = 'play-' + musicId;
        let idPause = 'pause-' + musicId;
        let play = document.getElementById(idPlay);
        let pause = document.getElementById(idPause);

        play.style.display = "inline-block"
        pause.style.display = "none"

        currentlyPlayingMusic.pause();
    }
    music.play();
}

function PauseMusic(music) {
    music.pause();
}

allIcons.forEach(icon => {
    icon.addEventListener("click", () => {
        getMusicId(icon.id);
    });
});

progressBars.forEach(progressBar => {
    let musicId = progressBar.dataset.rangeId;
    let music = enablePlayMusic(musicId);
    
    progressBar.addEventListener('click', function (e) {
        let clickX = e.pageX - this.offsetLeft;
        let percent = clickX / this.offsetWidth;
        music.currentTime = percent * music.duration;
    });
});
