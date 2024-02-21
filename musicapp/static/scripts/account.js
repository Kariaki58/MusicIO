const cards = document.querySelectorAll('.element')


cards.forEach(card => {
    card.addEventListener('click', () => {
        if (card.id === "favourites") {
            window.location.href = window.location.origin + '/musicapp/templates/favourites.html'
        } else if (card.id === "settings") {
            window.location.href = window.location.origin + '/musicapp/templates/settings.html'
        } else if (card.id === "comments") {
            window.location.href = window.location.origin + '/musicapp/templates/comments.html'
        } else {
            window.location.href = window.location.origin + '/musicapp/templates/likes.html'
        }
    })
})
