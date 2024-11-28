document.addEventListener('DOMContentLoaded', () => {
    const fileInput = document.getElementById('input_field')
    const fileInputSpan = document.getElementById('input_field_span')
    const subButton = document.getElementById('submit_button')

    if (fileInput.files.length == 0) {
        fileInputSpan.textContent = '(File no chhosen)'
        subButton.disabled = true 
    }

    console.log(fileInput.files.length)
    fileInput.addEventListener('change', () => {
        console.log("Hello", fileInput.files.length)
        if (fileInput.files.length > 0) {
            fileInputSpan.textContent = fileInput.files[0].name
            subButton.disabled = false 
        } 
    })
})