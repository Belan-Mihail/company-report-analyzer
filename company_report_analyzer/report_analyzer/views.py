from django.shortcuts import render, redirect
import base64
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UploadFileForm
import pandas as pd
from .generate_pdf import generate_pdf
from io import BytesIO
import os
from django.urls import reverse

def process_file(uploaded_file, selected_reports):
    # Move the pointer to the beginning of the file before reading
    uploaded_file.seek(0)
    
    # Reading the downloaded CSV file
    df = pd.read_csv(uploaded_file)

    # Expected headers
    expected_headers = ['Date', 'Sales', 'Region', 'Name', 'Company']

    # Check that all expected headers are present in the file
    if not all(header in df.columns for header in expected_headers):
        return None  # Return None if the headers do not match

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

            # Get the file extension
            file_extension = os.path.splitext(uploaded_file.name)[1].lower()
            # Checking the file extension
            if file_extension != '.csv':
                # redirect to error page with message
                error_message = 'Please upload a CSV file'
                return HttpResponseRedirect(reverse('error') + f'?error_message={error_message}')

            form.save()

            # Get the selected reports
            selected_reports = request.POST.getlist('reports')
            
            # Process the file with the selected reports
            pdf_output = process_file(uploaded_file, selected_reports)

            if pdf_output is None:
                # If file headers do not match, redirect to error page
                return redirect('error')

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
        return render(request, 'success.html', context)
    else:
        return redirect('error')
    

def download_pdf(request):
    # Get base64 string from session
    pdf_base64 = request.session.get('pdf_report_base64', None)

    if pdf_base64:
        # Decode base64 into bytes
        pdf_output = base64.b64decode(pdf_base64)

        # Return PDF as response
        response = HttpResponse(pdf_output, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="report.pdf"'

        # Clear session data after download
        del request.session['pdf_report_base64']
        return response
    else:
        return redirect('upload_file')

def error(request):
    # Extract the error message from the GET parameters if there is one
    error_message = request.GET.get('error_message', None)

    # Render error page when headers do not match
    return render(request, 'error.html', {'error_message': error_message})