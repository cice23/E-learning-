from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404, render
from lia.models import IntelligentLink
from .models import Message
import json

@csrf_exempt
def email_webhook(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            lia_token = data.get('lia_token')
            sender = data.get('sender')
            subject = data.get('subject')
            body = data.get('body')

            lia = get_object_or_404(IntelligentLink, token=lia_token)

            Message.objects.create(
                lia=lia,
                sender=sender,
                subject=subject,
                body=body
            )

            return JsonResponse({'status': 'success'}, status=201)
        except (json.JSONDecodeError, KeyError):
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)
        except IntelligentLink.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'LIA not found'}, status=404)

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

def inbox(request):
    messages = Message.objects.filter(lia__user=request.user).order_by('-received_at')
    return render(request, 'communications/inbox.html', {'messages': messages})
