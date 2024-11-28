document.addEventListener('DOMContentLoaded', () => {
    const fileInput = document.getElementById('input_field')
    const inputLabel = document.getElementById('inputLabel')
    const subButton = document.getElementById('submit_button')

    if (fileInput.files.length == 0) {     
        subButton.disabled = true 
        inputLabel.textContent = 'Choose file'
    }

    console.log(fileInput.files.length)
    fileInput.addEventListener('change', () => {

        if (fileInput.files.length > 0) {
            inputLabel.textContent = fileInput.files[0].name
            subButton.disabled = false 
        } 
    })
})