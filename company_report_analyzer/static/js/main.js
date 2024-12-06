document.addEventListener('DOMContentLoaded', () => {
    const fileInput = document.getElementById('id_file')
    const reportsButton = document.getElementById('select-reports_button')
    const cancelButton = document.getElementById('cancel_button')
    const modalWindow = document.getElementById('modal')
    const cancelProcessButton = document.getElementById('cancel-processing-button')
    const form = document.querySelector('form')
    
    // Hide buttons when loading a page if there is no file selected
    if (fileInput.files.length == 0) {     
        reportsButton.classList.add('hidden') 
        cancelButton.classList.add('hidden')
    } 
    
    // File change handler
    fileInput.addEventListener('change', () => {
        if (fileInput.files.length > 0) {
            reportsButton.classList.remove('hidden') 
            cancelButton.classList.remove('hidden') 
            reportsButton.classList.add('visible') 
            cancelButton.classList.add('visible') 
        } 
    })

    // Cancel button handler
    cancelButton.addEventListener('click', () => {
        fileInput.value = ''
        reportsButton.classList.remove('visible') 
        cancelButton.classList.remove('visible') 
        reportsButton.classList.add('hidden') 
        cancelButton.classList.add('hidden') 
        
       
    })

    // Reports button handler
    reportsButton.addEventListener('click', (event) => {
        event.preventDefault()
        cancelProcessButton.classList.remove('hidden');
        modalWindow.classList.remove('hidden');
        cancelProcessButton.classList.add('visible');
        modalWindow.classList.add('visible');
        reportsButton.classList.remove('visible');
        cancelButton.classList.remove('visible');
        reportsButton.classList.add('hidden');
        cancelButton.classList.add('hidden');
    })

    // Handler for the cancel-processing button
    cancelProcessButton.addEventListener('click', () => {
        modalWindow.classList.remove('visible');
        cancelProcessButton.classList.remove('visible');
        modalWindow.classList.add('hidden');
        cancelProcessButton.classList.add('hidden');
        fileInput.value = ''

        // Reset the state of all checkboxes
        const checkboxes = modalWindow.querySelectorAll('input[type="checkbox"]');
        checkboxes.forEach(checkbox => {
            checkbox.checked = false;
        })    
    })

    // Form submit handler
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