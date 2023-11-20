document.getElementById('login-form').addEventListener('submit', function(event) {
    event.preventDefault();

    var usernameEmail = document.getElementById('username_email').value;
    var password = document.getElementById('password').value;

    fetch('/login/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ usernameEmail: usernameEmail, password: password })
    })
    .then(response => {
        if (response.ok) {
            return response.json();
        }
        throw new Error('Network response was not ok.');
    })
    .then(data => {
        console.log('Success:', data);
        // Gestire qui la risposta positiva, come il reindirizzamento alla dashboard
    })
    .catch(error => console.error('Error:', error));
});
