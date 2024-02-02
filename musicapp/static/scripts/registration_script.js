function showLoginForm() {
    window.location.href = 'login.html';
}
function onGoogleSignIn(googleUser) {
    console.log('Google user information:', googleUser.getBasicProfile());
}

document.getElementById('registrationForm').addEventListener('submit', function (event) {
    event.preventDefault();
    window.location.href = 'home.html';
});