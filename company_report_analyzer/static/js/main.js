document.addEventListener('DOMContentLoaded', () => {
    const fileInput = document.getElementById('id_file')
    const reportsButton = document.getElementById('select-reports_button')
    const cancelButton = document.getElementById('cancel_button')
    const modalWindow = document.getElementById('modal')
    const cancelProcessButton = document.getElementById('cancel-processing-button')
    const form = document.querySelector('form')
    

    if (fileInput.files.length == 0) {     
        reportsButton.style.display = 'none' 
        cancelButton.style.display = 'none'
        
    } 
    
    
    fileInput.addEventListener('change', () => {
        
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

    form.addEventListener('submit', (event) => {
        // select all checkboxes
        const checkboxes = modalWindow.querySelectorAll('input[type="checkbox"]')

        //make array of checked checboxes
        const checkedCheckboxes = Array.from(checkboxes).filter(checkbox => checkbox.checked)

        // check checked checkbox
        if (checkedCheckboxes.length === 0) {
            event.preventDefault();
            alert('Please select at least one report.')
        }            
    })
})