from django.shortcuts import render, redirect
from django.utils import timezone
from datetime import timedelta
from .models import IntelligentLink
from django.contrib.auth.decorators import login_required

@login_required
def generate_lia(request):
    if request.method == 'POST':
        service_name = request.POST.get('service_name')
        level = request.POST.get('level')

        # For now, we don't check if the user has the required info

        expires_at = timezone.now() + timedelta(days=1)

        lia = IntelligentLink.objects.create(
            user=request.user,
            service_name=service_name,
            level=level,
            expires_at=expires_at
        )

        return redirect('lia_list')

    return render(request, 'lia/generate.html')

@login_required
def lia_list(request):
    lias = IntelligentLink.objects.filter(user=request.user)
    return render(request, 'lia/list.html', {'lias': lias})
