from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def email(request):
    send_mail(
        'Hello from DjangoDev',
        'Here goes email text',
        '79200711112@yandex.ru',
        ['Sergei_Vinokurov@rambler.ru'],
        fail_silently=False
    )
    return render(request, 'email/email.html')

# def sendPlainMail (request):
#     message=request.POST.get('message', '')
#     subject=request.POST.get('subject', '')
#     mail_id=request.POST.get('email', '')
#     email=EmailMessage(
#         subject,
#         message,
#         EMAIL_HOST_USER,
#         [mail_id]
#     )
#     email.content_subtype='html'
#     email.send()
#     return HttpResponse ('Sent')

# def send_plain_email(request):
#     message=request.POST.get('message', '')
#     subject=request.POST.get('subject', '')
#     mail_id=request.POST.get('email', '')
#     email=EmailMessage(
#         subject,
#         message,
#         EMAIL_HOST_USER,
#         [mail_id]
#     )
    email.content_subtype='html'
    file=open('readme.md', 'r')
    email.attach('readme.md', file.read(), 'text/plain')
    email.send()

def send_file(request):
  send_mail(
        'Hello from DjangoDev',
        'Here goes email text',
        '79200711112@yandex.ru',
        ['Sergei_Vinokurov@rambler.ru'],
        fail_silently=False
    )
#     message=request.POST.get('message', '')
#     subject=request.POST.get('subject', '')
#     mail_id=request.POST.get('email', '')
#     email=EmailMessage(
#         subject,
#         message,
#         EMAIL_HOST_USER,
#         [mail_id]
#     )
#     email.content_subtype='html'
#     file=request.POST.FILES['file']
#     email.attach('file.name', file.read(), file.content_type)
#     email.send()
