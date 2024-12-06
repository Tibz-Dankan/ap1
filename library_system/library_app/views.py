from django.shortcuts import render, redirect
from .models import Book, TestResult
from .forms import BookForm, TestResultForm
import matplotlib.pyplot as plt
import io
import base64

def login_page(request):
    return render(request, 'library_app/login.html')

def book_input(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_input')
    else:
        form = BookForm()
    return render(request, 'library_app/book_input.html', {'form': form})

def test_input(request):
    if request.method == 'POST':
        form = TestResultForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('test_input')
    else:
        form = TestResultForm()
    return render(request, 'library_app/test_input.html', {'form': form})

def visualization(request):
    results = TestResult.objects.all()
    test_names = [result.test_name for result in results]
    scores = [result.score for result in results]

    plt.bar(test_names, scores, color='blue')
    plt.xlabel('Test Name')
    plt.ylabel('Score')
    plt.title('Test Results')

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    graphic = base64.b64encode(image_png).decode('utf-8')
    plt.close()

    return render(request, 'library_app/visualization.html', {'graphic': graphic})
