let progressBars = document.querySelectorAll('.range');
let allIcons = document.querySelectorAll('i');
const musicList = document.querySelectorAll(".control-music");
let currentlyPlayingMusic = null;


function isPlaying(music) {
    console.log(music);
    if (music) {
        return true;
    }
    return false;
}

function enablePlayMusic(id) {
    let musicElement = null;
    musicList.forEach(musicItem => {
        const musicId = musicItem.getAttribute("data-song-id");
        if (musicId == id) {
            musicElement = musicItem;
        }
    });
    return musicElement;
}

function getMusicId(id) {
    let musicId = document.getElementById(id).dataset.musicId;
    let music = enablePlayMusic(musicId);

    if (/^play-\d+$/.test(id) || /^pause-\d+$/.test(id))
    {
        if (/^play-\d+$/.test(id)) {
            let play = document.getElementById(id);
            let idChange = 'pause-' + musicId;
            let pause = document.getElementById(idChange);
            play.style.display = "none";
            pause.style.display = "inline-block";
            console.log(idChange)
            PlayMusic(music);
        } else if (/^pause-\d+$/.test(id)) {
            let pause = document.getElementById(id);
            let idChange = 'play-' + musicId;
            let play = document.getElementById(idChange);
            console.log(idChange)
            pause.style.display = "none";
            play.style.display = "inline-block";
            PauseMusic(music);
        }
        music.addEventListener('timeupdate', () => {
            currentlyPlayingMusic = music;
            let value = (music.currentTime / music.duration) * 100;
            let progressBar = document.getElementById('range-' + musicId);
            progressBar.value = value;
        });
    }
}

function PlayMusic(music) {
    if (currentlyPlayingMusic) {
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


// for (let i = 0; i < musicList.length; i++) {
//     musicList[i].addEventListener('timeupdate', () => {
//         currentlyPlayingMusic = musicList[i];
//         let value = (musicList[i].currentTime / musicList[i].duration) * 100;
//         let progressBar = document.getElementById('range-' + musicList[i].getAttribute("data-song-id"));
//         progressBar.value = value;
//     });
// }
