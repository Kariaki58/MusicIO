function showLoginForm() {
    window.location.href = 'login.html';
}
function onGoogleSignIn(googleUser) {
    // Handle Google sign-in, you can send the user's information to your server for further processing.
    console.log('Google user information:', googleUser.getBasicProfile());
}