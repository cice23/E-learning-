from django.shortcuts import render, redirect
from django.utils import timezone
from datetime import timedelta
from .models import IntelligentLink
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import LiaValidationSerializer

from django.contrib import messages

@login_required
def generate_lia(request):
    if request.method == 'POST':
        service_name = request.POST.get('service_name')
        level = request.POST.get('level')
        user = request.user

        if level == 'MEDIUM' and not user.selfie:
            messages.error(request, 'Please upload a selfie to generate a Medium level link.')
            return redirect('profile')

        if level == 'STRONG' and (not user.id_card or not user.passport):
            messages.error(request, 'Please upload an ID card and passport to generate a Strong level link.')
            return redirect('profile')

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

@api_view(['POST'])
def verify_lia(request):
    serializer = LiaValidationSerializer(data=request.data)
    if serializer.is_valid():
        token = serializer.validated_data['token']
        # domain = serializer.validated_data['domain']
        # level_required = serializer.validated_data['level_required']

        try:
            lia = IntelligentLink.objects.get(token=token, status=IntelligentLink.LinkStatus.GENERATED)

            # Here you would add the logic to check the domain and the level

            # Mark the LIA as used
            lia.status = IntelligentLink.LinkStatus.USED
            lia.save()

            anonymous_id = f"gid_user_{lia.user.id}"

            return Response({'status': 'verified', 'anonymous_id': anonymous_id}, status=status.HTTP_200_OK)
        except IntelligentLink.DoesNotExist:
            return Response({'status': 'error', 'message': 'Invalid or used token'}, status=status.HTTP_404_NOT_FOUND)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
