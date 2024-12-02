document.addEventListener('DOMContentLoaded', () => {
    const fileInput = document.getElementById('id_file')
    const reportsButton = document.getElementById('select-reports_button')
    const cancelButton = document.getElementById('cancel_button')
    const modalWindow = document.getElementById('modal')
    const cancelProcessButton = document.getElementById('cancel-processing-button')
    

    if (fileInput.files.length == 0) {     
        reportsButton.style.display = 'none' 
        cancelButton.style.display = 'none'
        
    } 
    console.log(fileInput.files.length)
    
    fileInput.addEventListener('change', () => {
        console.log(fileInput.files.length)
        if (fileInput.files.length > 0) {
            
            reportsButton.style.display = 'inline-block' 
            cancelButton.style.display = 'inline-block'
        } 
    })

    cancelButton.addEventListener('click', () => {
        fileInput.value = ''
        reportsButton.style.display = 'none' 
        cancelButton.style.display = 'none'
        
       
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

        // Reset the state of all checkboxes
        const checkboxes = modalWindow.querySelectorAll('input[type="checkbox"]');
        checkboxes.forEach(checkbox => {
            checkbox.checked = false;
        })    
    })
})