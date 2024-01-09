document.addEventListener("DOMContentLoaded", (event) => {


  });

  function scanComputer() {
    const directoryInput = document.getElementById('directory');
    const directory = directoryInput.value;

    fetch('/scan', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ directory }),
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
    })
    .catch(error => {
        console.error('Błąd podczas skanowania:', error);
    });
}