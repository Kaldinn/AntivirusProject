document.addEventListener("DOMContentLoaded", (event) => {

})

async function getData() {
    const fileInput = document.getElementById('file');
    const formData = new FormData();
    formData.append('file', fileInput.files[0]);

    const response = await fetch('/scan', {
        method: 'POST',
        body: formData
    });

    const data = await response.json();
    console.log(data)
    document.getElementById('file-content').innerText = data.file_content;
}