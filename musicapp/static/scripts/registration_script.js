function showLoginForm() {
    window.location.href = 'login.html';
}
function onGoogleSignIn(googleUser) {
    console.log('Google user information:', googleUser.getBasicProfile());
}