from django.shortcuts import render, redirect
import base64
from django.http import HttpResponse
from .forms import UploadFileForm
import pandas as pd
from .generate_pdf import generate_pdf
from io import BytesIO

def process_file(uploaded_file, selected_reports):
    # Move the pointer to the beginning of the file before reading
    uploaded_file.seek(0)
    
    # Reading the downloaded CSV file
    df = pd.read_csv(uploaded_file)

    df = df[:20]
    
    # Generate PDF using selected reports
    pdf_output = generate_pdf(df, selected_reports)

    # Get bytes from BytesIO object
    return pdf_output.getvalue()

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            form.save()

            # Get the selected reports
            selected_reports = request.POST.getlist('reports')
            
            # Process the file with the selected reports
            pdf_output = process_file(uploaded_file, selected_reports)

            # Convert PDF to base64 string
            pdf_base64 = base64.b64encode(pdf_output).decode('utf-8')

            # Save base64 string in session
            request.session['pdf_report_base64'] = pdf_base64

            return redirect('success')

        else:
            # If the form is invalid, return it with errors
            return render(request, 'upload.html', {'form': form})
    else:
        form = UploadFileForm()
        return render(request, 'upload.html', {'form': form})

def success(request):
    pdf_base64 = request.session.get('pdf_report_base64', None)

    if pdf_base64:
        context = {'pdf_available': True}
    else:
        context = {'pdf_available': False}

    return render(request, 'success.html', context)