from rest_framework import generics
from rest_framework.response import Response
from preinscription.models import Preinscription
from .serializers import PreinscriptionSerializer
from django.core.mail import send_mail
from django.conf import settings

from django.template.loader import render_to_string

class PreinscriptionListCreate(generics.ListCreateAPIView):
    queryset = Preinscription.objects.all()
    serializer_class = PreinscriptionSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 201:  # Si la preinscripción se creó con éxito
            # Enviar correo electrónico a la dirección de correo electrónico del usuario
            preinscription_data = request.data
            email = preinscription_data.get('email')
            if email:
                subject = 'Confirmación de Preinscripción'
                message = render_to_string('email.html', {'name': preinscription_data.get('name')})
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [email]
                send_mail(subject, message, email_from, recipient_list, fail_silently=False, html_message=message)
        return response

class PreinscriptionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Preinscription.objects.all()
    serializer_class = PreinscriptionSerializer