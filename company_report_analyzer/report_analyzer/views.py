from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UploadFileForm
import pandas as pd
from .generate_pdf import generate_pdf
from io import BytesIO

def process_file(uploaded_file, selected_reports):
    # Перемещаем указатель в начало файла перед чтением
    uploaded_file.seek(0)
    
    # Чтение загруженного CSV файла
    df = pd.read_csv(uploaded_file)

    df = df[:20]
    
    # Генерация PDF с использованием выбранных отчетов
    pdf_output = generate_pdf(df, selected_reports)

    # Возвращаем PDF
    return pdf_output

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            form.save()

            # Получаем выбранные отчеты
            selected_reports = request.POST.getlist('reports')
            
            # Обрабатываем файл с выбранными отчетами
            pdf_output = process_file(uploaded_file, selected_reports)

            # Возвращаем PDF как ответ
            response = HttpResponse(pdf_output, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="report.pdf"'

            # Сохраняем PDF в сессию
            request.session['pdf_report'] = pdf_output
            
            # Перенаправляем сразу на скачивание PDF
            return redirect('success')

            return response
        else:
            # Если форма невалидна, возвращаем ее с ошибками
            return render(request, 'upload.html', {'form': form})
    else:
        form = UploadFileForm()
        return render(request, 'upload.html', {'form': form})