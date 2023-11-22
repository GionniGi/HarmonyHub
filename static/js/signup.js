document.getElementById('signup-form').addEventListener('submit', function (event) {
    event.preventDefault();

    const formData = new FormData(this);
    const object = {};
    formData.forEach((value, key) => {
        object[key] = value;
    });

    // Check if form fields are empty
    const isEmpty = Object.values(object).some(value => value === '');
    if (isEmpty) {
        alert('Please fill in all the fields');
        return;
    }

    fetch('/user/signup/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(object),
    })
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to sign up');
            }
            return response.json();
        })
        .then(data => {
            if (data.error) {
                alert('Sign up failed: ' + data.error);
            } else {
                alert(data.message);
                window.location.href = '/user/login';
            }
        })
        .catch((error) => {
            console.error('Error:', error);
            alert('An error occurred while signing up');
        });
});
  
