import os

from django.core.exceptions import ValidationError
from django.core.files.storage import FileSystemStorage
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def process_get_view(request: HttpRequest) -> HttpResponse:
    a = request.GET.get('a', '')
    b = request.GET.get('b', '')
    result = a + b
    context = {
        'a': a,
        'b': b,
        'result': result,
    }
    return render(request, 'requestdataapp/request-query-params.html', context=context)


def user_form(request: HttpRequest) -> HttpResponse:
    return render(request, 'requestdataapp/user-bio-form.html')


def handle_file_upload(request: HttpRequest) -> HttpResponse:
    size_limit = 1000
    if request.method == 'POST' and request.FILES.get('myfile'):
        myfile = request.FILES['myfile']
        if myfile.size < size_limit:
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            print('saved file', filename)
        else:
            return render(request, 'requestdataapp/error-file-size.html')

    return render(request, 'requestdataapp/file-upload.html')
