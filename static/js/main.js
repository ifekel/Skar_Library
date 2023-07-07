const mobile_nav_toggler = document.querySelector("#mobile-nav-toggle");
const navbar = document.querySelector(".navmenu");
const account_options = document.querySelector(".account-options");
const toggle_account = document.querySelector("#account-toggle-setting");

mobile_nav_toggler.addEventListener('click', showNavBar);
mobile_nav_toggler.addEventListener('dblclick', removeNavBar);
toggle_account.addEventListener('mouseenter', showAccountSetting);
account_options.addEventListener('mouseleave', removeAccountSettings);


function showNavBar(e) {
    navbar.style.display = "block"
}

function removeNavBar(e) {
    navbar.style.display = "none"
}

function showAccountSetting(e) {
    account_options.style.marginLeft = "0";
}

function removeAccountSettings(e) {
    account_options.style.marginLeft = "6%";
}

// Shelf And Library
const bookLinks = document.querySelectorAll('.book');
bookLinks.forEach(link => {
    link.addEventListener('click', function (event) {
        event.preventDefault();
        const bookId = this.getAttribute('data-id');
        const shelfId = 1;
        const xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function () {
            if (this.readyState === 4 && this.status === 200) {
                console.log('Book added to shelf')
            }
        }
        xhr.open('GET', `/add-book-to-shelf?book_id=${bookId}&shelf_id=${shelfId}`)
        xhr.send();
    });
});