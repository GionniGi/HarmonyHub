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
            
            if (data.status === "success") {
                window.location.href = '/login';
            }
        })
    });