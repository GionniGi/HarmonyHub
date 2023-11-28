document.getElementById('signup-form').addEventListener('submit', function(event){
    event.preventDefault();

    // Raccogliere i dati dal form
    var userData = {
        username: document.getElementById('username').value,
        email: document.getElementById('email').value,
        password: document.getElementById('password').value,
        confirm_password: document.getElementById('confirm_password').value,
        first_name: document.getElementById('first_name').value,
        last_name: document.getElementById('last_name').value,
        birth_date: document.getElementById('birth_date').value,
        description: document.getElementById('description').value,
    };

    // Invio dei dati al server tramite una richiesta POST
    fetch('/user/signup/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(userData),
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            document.getElementById('feedback-message').innerText = data.success;
            document.getElementById('feedback-message').style.color = 'green';
            setTimeout(function() {
                window.location.href = '/user/login/';
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
