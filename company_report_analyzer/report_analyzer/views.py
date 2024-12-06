from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UploadFileForm
import pandas as pd
from .generate_pdf import generate_pdf
from io import BytesIO



def process_file(uploaded_file, selected_reports):
    
    
    # Move to the beginning before it convert in df
    uploaded_file.seek(0)
    
    
    # Read the uploaded CSV file
    df = pd.read_csv(uploaded_file)

    df = df[:20]
    
    # Generate the PDF using the selected reports
    pdf_output = generate_pdf(df, selected_reports)

    # Return PDF file
    return pdf_output

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            form.save()

            # We receive the selected reports
            selected_reports = request.POST.getlist('reports')
            
            #Processing a file with selected reports
            pdf_output = process_file(uploaded_file, selected_reports)

            # Return the PDF as a response
            response = HttpResponse(pdf_output, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="report.pdf"'
            return redirect('success')
        else:
            # Form is invalid, return empty form to display errors
            return render(request, 'upload.html', {'form': form})
    else:
        form = UploadFileForm()
        return render(request, 'upload.html', {'form': form})
    
