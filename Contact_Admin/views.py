from django.shortcuts import render
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail

def Sent_downloadable_link(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            Name = request.POST['Movie_Name']
            message_email = request.POST['email']
            message = request.POST['message']
            send_mail(
                f'{Name} Request Fullfilled',
                f'Hi you requested a { Name } Movie or T.V Show is succesfully completed, Here is your Download links. \n { message } \n Thank You.',
                settings.EMAIL_HOST_USER,
                [message_email]
                )
            return render(request, 'Contact_Admin/index.html', {'Name':Name})
        else :
            return render(request, 'Contact_Admin/index.html')
    else :
        return render(request, 'Contact_us/index.html')