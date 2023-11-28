document.getElementById('signup-form').addEventListener('submit', function (event) {
    event.preventDefault();

    const formData = new FormData(this);
    const object = {};
    formData.forEach((value, key) => {
        object[key] = value;
    });

    fetch('/user/signup/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(object),
    })
        .then(response => response.json())
        .then(data => {
            const messageElement = document.getElementById('message');
            messageElement.innerText = data.message;
            
            if (data.status === "success") {
                window.location.href = '/login';
            }
        })
        .catch(error => {
            console.error('Error:', error);
            const messageElement = document.getElementById('message');
            messageElement.innerText = 'Si è verificato un errore durante la registrazione.';
        });
    });