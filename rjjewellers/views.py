from django.http import HttpResponseRedirect
from django.shortcuts import redirect , render
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from core.models import Subscriber, GoldImage
from core.forms import SubscriberForm
import random

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html' )

def gemstones(request):
    return render(request, "gemstones.html")

def jewellery(request):
    return render(request,"jewellery.html")

def gold(request):
    return render(request,"gold.html")

def diamond(request):
    return render(request,"diamond.html")

def platinum(request):
    return render(request,"platinum.html")

def coins(request):
    return render(request,"coins.html")

def gifts(request):
    return render(request,'coins2.html')

def random_digits():
    return "%0.12d" % random.randint(0,999999999999)

@csrf_exempt
def new(request):
    if request.method == 'POST':
        sub = Subscriber(email=request.POST['email'], conf_num=random_digits())
        sub.save()
        message = Mail(
            from_email=settings.FROM_EMAIL,
            to_emails=sub.email,
            subject='Newsletter Confirmation',
            html_content='Thank you for signing up for my email newsletter! \
                Please complete the process by \
                <a href="{}/confirm/?email={}&conf_num={}"> clicking here to \
                confirm your registration</a>.'.format(request.build_absolute_uri('/confirm/'),
                                                    sub.email,
                                                    sub.conf_num))
        sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
        response = sg.send(message)
        return render(request, 'index.html', {'email': sub.email, 'action': 'added', 'form': SubscriberForm()})
    else:
        return render(request, 'index.html', {'form': SubscriberForm()})

def confirm(request):
    sub = Subscriber.objects.get(email=request.GET['email'])
    if sub.conf_num == request.GET['conf_num']:
        sub.confirmed = True
        sub.save()
        return render(request, 'index.html', {'email': sub.email, 'action': 'confirmed'})
    else:
        return render(request, 'index.html', {'email': sub.email, 'action': 'denied'})

