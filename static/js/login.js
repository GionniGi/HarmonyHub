document.getElementById('login-form').addEventListener('submit', function(event) {
    event.preventDefault();

    // Getting login data
    var username_email = document.getElementById('username_email').value;
    var password = document.getElementById('password').value;

    // Sending login data
    fetch('/user/login/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ usernameEmail: username_email, password: password })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            rdocument.getElementById('feedback-message').innerText = data.success;
            document.getElementById('feedback-message').style.color = 'green';
            setTimeout(function() {
                window.location.href = '/dashboard/';
            }, 1000);
        } else if (data.error) {
            document.getElementById('feedback-message').innerText = data.error;
            document.getElementById('feedback-message').style.color = 'red';
        }
    })
    .catch((error) => {
        console.error('Error:', error);
        document.getElementById('feedback-message').innerText = "Errore di comunicazione con il server.";
        document.getElementById('feedback-message').style.color = 'red';
    });
});
