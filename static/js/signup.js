document.getElementById('signup-form').addEventListener('submit', function(event) {
    event.preventDefault();

    var formData = new FormData(this);
    var object = {};
    formData.forEach(function(value, key){
        object[key] = value;
    });

    fetch('/user/signup/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(object)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        if (data.error) {
            alert(data.error);
        } else {
            alert(data.message);
            window.location.href = '/login.html';
        }
    })
    .catch((error) => {
        console.error('Error:', error);
        alert('An error occurred: ' + error.message);
    });
});
