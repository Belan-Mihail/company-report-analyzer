document.addEventListener('DOMContentLoaded', () => {
    const fileInput = document.getElementById('input_field')
    const fileInputSpan = document.getElementById('input_field_span')
    const subButton = document.getElementById('submit_button')

    fileInput.addEventListener('change', () => {
        if (fileInput.files.lenght > 0) {
            fileInputSpan.textContent = fileInput.files[0].name
            subButton.disabled = false 
        } else {
            fileInputSpan.textContent = '(File no chhosen)'
            subButton.disabled = true
        }
    })
})