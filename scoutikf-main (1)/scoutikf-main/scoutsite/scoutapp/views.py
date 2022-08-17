from django.shortcuts import render
from django.http import HttpResponse
from .models import Scout

def scout(request):
    if request.method=='POST':
        id = request.POST.get('id')
        email = request.POST.get('email')
        age = request.POST.get('agecriteria')
        dob = request.POST.get('dob')
        contact = request.POST.get('contact')
        s_contact = request.POST.get('secondary_contact')
        country = request.POST.get('country')
        city = request.POST.get('city')
        reffral = request.POST.get('referal')
        experienced = request.POST.get('experience')
        work_status = request.POST.get('worked')
        associated_clubs = request.POST.get('past_club')
        course = request.POST.get('course')

        #Inserting Data into Database!
        scout_details = Scout(email=email,age=age,dob=dob,contact=contact,s_contact=s_contact,country=country,city=city,reffral=reffral,experienced=experienced,work_status=work_status,associated_clubs=associated_clubs,course=course)
        scout_details.save()
        return HttpResponse('<h1 style="font-family:sans serif;">Record Submitted.</h1>')
    else:    
        return render(request, 'scoutform.html')

def land(request):
    return render(request, 'landpage.html')        