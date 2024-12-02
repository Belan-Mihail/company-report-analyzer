document.addEventListener('DOMContentLoaded', () => {
    const fileInput = document.getElementById('input_field')
    const inputLabel = document.getElementById('inputLabel')
    const subButton = document.getElementById('submit_button')
    const cancelButton = document.getElementById('cancel_button')
    

    if (fileInput.files.length == 0) {     
        subButton.style.display = 'none' 
        cancelButton.style.display = 'none'
        inputLabel.textContent = 'Choose file'
    } 

    
    fileInput.addEventListener('change', () => {
        
        if (fileInput.files.length > 0) {
            inputLabel.textContent = fileInput.files[0].name
            subButton.style.display = 'inline-block' 
            cancelButton.style.display = 'inline-block'
        } 
    })

    cancelButton.addEventListener('click', () => {
        fileInput.value = ''
        subButton.style.display = 'none' 
        cancelButton.style.display = 'none'
        inputLabel.textContent = 'Choose file'
       
    })
})