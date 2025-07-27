from django.shortcuts import render

def sandbox_view(request):
    url = request.GET.get('url')
    return render(request, 'sandbox/view.html', {'url': url})
