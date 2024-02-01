// function onSubmit(e) {
//     const errorElement = document.getElementById('error');
//     e.preventDefault();
//     const formData = new FormData(document.getElementById('form-id'));

//     fetch('http://127.0.0.1:5000/', {
//         method: "POST",
//         body: formData,
//     })
//     .then((res) => {
//         if (!res.ok) {
//             throw new Error('Network response was not ok');
//         }
//         return res.json();
//     })
//     .then((data) => {
//         errorElement.innerHTML = data.error;
//     })
//     .catch((error) => {
//         console.error('Error during fetch:', error);
//         alert("Failed to fetch data");
//     });
// }

// document.getElementById('form-id').addEventListener('submit', onSubmit);
