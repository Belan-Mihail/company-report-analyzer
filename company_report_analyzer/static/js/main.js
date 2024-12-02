document.addEventListener('DOMContentLoaded', () => {
    const fileInput = document.getElementById('input_field')
    const inputLabel = document.getElementById('inputLabel')
    const reportsButton = document.getElementById('select-reports_button')
    const cancelButton = document.getElementById('cancel_button')
    const modalWindow = document.getElementById('modal')
    const cancelProcessButton = document.getElementById('cancel-processing-button')
    const realinput = document.getElementById('id_file')
    const customUploadButton = document.getElementById('confirm-processing-button')

    // const customUploadButton = document.getElementById('confirm-processing-button');

    customUploadButton.addEventListener('click', () => {
        realinput.click();  // При клике на кастомную кнопку, вызываем стандартный инпут
    });

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
        cancelProcessButton.style.display = 'block'  
        modalWindow.style.display = 'block'      
        reportsButton.style.display = 'none' 
        cancelButton.style.display = 'none'

    })

    cancelProcessButton.addEventListener('click', () => {
        modalWindow.style.display = 'none'    
        cancelProcessButton.style.display = 'none'  
        fileInput.value = ''
        inputLabel.textContent = 'Choose file'
    })
})