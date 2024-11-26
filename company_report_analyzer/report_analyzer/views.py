from django.shortcuts import render
from django.http import HttpResponse
from .forms import UploadFileForm

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            # here can added logic
            return HttpResponse('File uploaded successfully')

        else:
            form = UploadFileForm()
        return render(request, 'upload.html', {'form': form})
        
