from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UploadFileForm
import pandas as pd
from .generate_pdf import generate_pdf
from io import BytesIO



def process_file(uploaded_file, selected_reports):
    

     # Преобразуем файл в BytesIO для работы с ним в памяти
    file_bytes = uploaded_file.read()
    file_stream = BytesIO(file_bytes)
    
    # Move to the beginning before it convert in df
    file_stream.seek(0)
    
    
    # Read the uploaded CSV file
    df = pd.read_csv(file_stream)

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

            # Сохраняем PDF в сессии
            request.session['pdf_output'] = pdf_output.getvalue()

            return redirect('success')
        else:
            # Form is invalid, return empty form to display errors
            return render(request, 'upload.html', {'form': form})
    else:
        form = UploadFileForm()
        return render(request, 'upload.html', {'form': form})
    

def success_page(request):
    # Successful processing page
    # Извлекаем PDF данные из сессии и подготавливаем ответ
    pdf_output = request.session.get('pdf_output')
    
    if pdf_output:
        # Создаем ответ с содержимым PDF
        response = HttpResponse(pdf_output, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="report.pdf"'

        # Очищаем PDF данные из сессии после отправки ответа
        del request.session['pdf_output']

        return response
    else:
        # Если PDF не найден, просто отображаем страницу успеха
        return render(request, 'success.html', {
            'success_message': 'Запрос успешно обработан.',
            'show_back_button': True
        })