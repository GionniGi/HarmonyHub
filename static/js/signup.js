document.getElementById('signup-form').addEventListener('submit', function(event) {
    event.preventDefault();

    // Raccogliere i valori dai campi del form
    var username = document.getElementById('username').value;
    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;
    var confirmPassword = document.getElementById('confirm_password').value;
    var firstName = document.getElementById('first_name').value;
    var lastName = document.getElementById('last_name').value;
    var birthDate = document.getElementById('birth_date').value;
    var description = document.getElementById('description').value;
    var extroversion = document.getElementById('extroversion').value;
    var friendliness = document.getElementById('friendliness').value;
    var emotionalStability = document.getElementById('emotional_stability').value;
    var openness = document.getElementById('openness').value;
    var conscientiousness = document.getElementById('conscientiousness').value;

    // Creare l'oggetto con i dati da inviare
    var signupData = {
        username: username,
        email: email,
        password: password,
        confirmPassword: confirmPassword,
        firstName: firstName,
        lastName: lastName,
        birthDate: birthDate,
        description: description,
        extroversion: extroversion,
        friendliness: friendliness,
        emotionalStability: emotionalStability,
        openness: openness,
        conscientiousness: conscientiousness
    };

    // Invia i dati al server tramite una richiesta POST
    fetch('/user/signup/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(signupData)
    })
    .then(response => response.json())
    .then(data => {
        if (data.errors) {
            // Show the errors
            console.error('Errors:', data.errors);
            alert('Errori nella registrazione: ' + data.errors.join('\n'));
        } else {
            // Show success message
            console.log('Success:', data);
            alert('Registrazione avvenuta con successo!');
            // Redirect to login page
            window.location.href = '/user/login/';
        }
    })
    .catch(error => console.error('Error:', error));
});

