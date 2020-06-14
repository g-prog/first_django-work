from django.shortcuts import render
from . models import Destination

# Create your views here.
def index(request):
    dest1 = Destination()
    dest1.name = 'Port-Harcourt'
    dest1.desc = 'A very lovely place with diverse cultures'
    dest1.img = 'destination_2.jpg'
    dest1.price = '20,000'
    dest1.offer = False
     
    dest2 = Destination()
    dest2.name = 'Lagos'
    dest2.desc = 'A hub for business opportunities'
    dest2.price = '50,000'
    dest2.img = 'destination_3.jpg'
    dest2.offer = True

    dest3 = Destination()
    dest3.name = 'Abuja FCT'
    dest3.desc = 'The administrative head of Nigeria'
    dest3.price = '60,000'
    dest3.img = 'destination_3.jpg'
    dest3.offer = True

    dests = [dest1, dest2, dest3]

    return render(request,'index.html', {'dests' : dests })

