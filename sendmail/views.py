from django.core.mail import send_mail
from django.http import HttpResponse


# Create your views here.
def test_send_email(request):
    message = """
    Prezados!

    Informamos que este é um teste de envio de e-mail com o framework django!

    Atenciosamente,
    Wesley Paulo Gonçalves
    +55 12 98804-2246
    """
    recipient_list = ['wesley.goncalves1984@gmail.com', 'wpgames84@gmail.com']

    send_mail('TESTE', message, '', recipient_list)

    return HttpResponse('<h1>Teste de envio de e-mail!</h1>')
