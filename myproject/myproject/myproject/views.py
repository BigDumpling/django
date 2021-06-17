from django.shortcuts import render


def response_error_404_handler(request, exception=None):
    print(request)
    return render(request=request, template_name='404.html')
