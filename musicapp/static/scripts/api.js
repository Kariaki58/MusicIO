function deleteSong(id) {
    fetch(`http://127.0.0.1:5000/api/2/songs/${id}`, {
        method: 'DELETE',
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        location.reload()
        alert("deleted successfully")

    })
    .catch(error => {
        console.error('Error deleting song:', error);
    });
}
