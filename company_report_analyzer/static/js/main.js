document.addEventListener('DOMContentLoaded', () => {
    const fileInput = document.getElementById('input_field')
    const inputLabel = document.getElementById('inputLabel')
    const reportsButton = document.getElementById('select-reports_button')
    const cancelButton = document.getElementById('cancel_button')
    const modalWindow = document.getElementById('modal')

    if (fileInput.files.length == 0) {     
        reportsButton.style.display = 'none' 
        cancelButton.style.display = 'none'
        inputLabel.textContent = 'Choose file'
    } 

    
    fileInput.addEventListener('change', () => {
        
        if (fileInput.files.length > 0) {
            inputLabel.textContent = fileInput.files[0].name
            reportsButton.style.display = 'inline-block' 
            cancelButton.style.display = 'inline-block'
        } 
    })

    cancelButton.addEventListener('click', () => {
        fileInput.value = ''
        reportsButton.style.display = 'none' 
        cancelButton.style.display = 'none'
        inputLabel.textContent = 'Choose file'
       
    })

    reportsButton.addEventListener('click', (event) => {
        event.preventDefault()

        modalWindow.style.display = 'block'      
        reportsButton.style.display = 'none' 
        cancelButton.style.display = 'none'

    })
})