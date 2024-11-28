document.addEventListener('DOMContentLoaded', () => {
    const fileInput = document.getElementById('input_field')
    const fileInputSpan = document.getElementById('input_field_span')

    fileInput.addEventListener('change', () => {
        fileInputSpan.textContent = fileInput.files[0].name
        document.getElementById('submit_button').style.display = 'block'
    })
})