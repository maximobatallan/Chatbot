from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from mysite.models import formulario
from django.core.mail import send_mail
from django.http import HttpResponseForbidden
import requests
from django.http import HttpResponse
# - Homepage



def send_user_data_email(user_data):
    subject = 'Nuevo usuario registrado'
    message = f'Se ha registrado un nuevo usuario con los siguientes datos:\n\n{user_data}'
    
    print(message)
    from_email = 'notificaciondepaginaweb@gmail.com'
    recipient_list = ['maximobatallan@gmail.com']
    send_mail(subject, message, from_email, recipient_list)


@csrf_exempt






def my_csrf_failure_view(request, reason=""):
    return HttpResponseForbidden('CSRF verification failed. Reason: {}'.format(reason))

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def save_formulario(request):
    

    nombre = request.POST.get('nombre')

    telefono = request.POST.get('telefono')
    email = request.POST.get('email')
    texto = request.POST.get('texto')

    formulario1 = formulario(nombre=nombre, telefono=telefono, mail=email, texto=texto)
    formulario1.save()
    user_data = f"nombre: {nombre} telefono: {telefono} texto: {texto}"
    send_user_data_email(user_data)
    
    
    
    return render(request, 'formulario.html')




# myapp/views.py

from django.http import JsonResponse


def webhook_whatsapp(request):
    
    
    #SI HAY DATOS RECIBIDOS VIA GET
    if request.method == "GET":
        #SI EL TOKEN ES IGUAL AL QUE RECIBIMOS
        if request.args.get('hub.verify_token') == "retobot":
            #ESCRIBIMOS EN EL NAVEGADOR EL VALOR DEL RETO RECIBIDO DESDE FACEBOOK
            return request.args.get('hub.challenge')
        else:
            #SI NO SON IGUALES RETORNAMOS UN MENSAJE DE ERROR
          return "Error de autentificacion."
    #RECIBIMOS TODOS LOS DATOS ENVIADO VIA JSON
    data=request.get_json()
    #EXTRAEMOS EL NUMERO DE TELEFONO Y EL MANSAJE
    telefonoCliente=data['entry'][0]['changes'][0]['value']['messages'][0]['from']
    #EXTRAEMOS EL TELEFONO DEL CLIENTE
    mensaje=data['entry'][0]['changes'][0]['value']['messages'][0]['text']['body']
    #EXTRAEMOS EL ID DE WHATSAPP DEL ARRAY
    idWA=data['entry'][0]['changes'][0]['value']['messages'][0]['id']
    #EXTRAEMOS EL TIEMPO DE WHATSAPP DEL ARRAY
    timestamp=data['entry'][0]['changes'][0]['value']['messages'][0]['timestamp']
    #ESCRIBIMOS EL NUMERO DE TELEFONO Y EL MENSAJE EN EL ARCHIVO TEXTO
    #SI HAY UN MENSAJE
    if mensaje is not None:
      f = open("texto.txt", "w")
      f.write(mensaje)
      f.close()
    
    
    
    
    
    response_data = {"status": "success", "message": "Hola webhook ejecutada correctamente"}
    return JsonResponse(response_data)

