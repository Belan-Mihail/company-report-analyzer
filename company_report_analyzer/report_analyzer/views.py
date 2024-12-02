from django.shortcuts import render
from django.http import HttpResponse
from .forms import UploadFileForm


def process_file(uploaded_file, reports):
    print("Reports selected:", reports)
    
    if uploaded_file:
        print("File received:", uploaded_file.name)

        if uploaded_file.size > 0:
            print("File size:", uploaded_file.size)

        else:
            print("Uploaded file is empty")
    else:
        print("No file uploaded")

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            form.save()

            # We receive the selected reports
            selected_reports = request.POST.getlist('reports')
            print("Selected reports:", selected_reports)
            #Processing a file with selected reports
            process_file(uploaded_file, selected_reports)

            # here can added logic
            return HttpResponse('File uploaded successfully')
        else:
        # Форма невалидна, вернуть пустую форму для отображения ошибок
            form = UploadFileForm()
    else:
        form = UploadFileForm()
        return render(request, 'upload.html', {'form': form})
    
