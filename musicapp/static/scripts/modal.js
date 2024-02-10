function openModal() {
    document.getElementById('myModal').style.display = 'flex';
}

function closeModal() {
    document.getElementById('myModal').style.display = 'none';
}

window.onclick = function(event) {
    if (event.target === document.getElementById('myModal')) {
        closeModal();
    }
};

document.getElementById('fileInput').addEventListener('change', function (e) {
    e.preventDefault()
    document.getElementById('fileName').innerText = this.value.split('\\').pop();
});
