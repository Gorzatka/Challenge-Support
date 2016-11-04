from django.shortcuts import render

def main(request):
    return render(request, 'challange_support_app/main.html', {})
