from django.shortcuts import render,redirect
from EpiceneApp.models import Officer,TransUser,Event,Shelters,Job,Institution,Med_booking,Legal_booking,Event_participation,Job_apply
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,"dashboard.html")

def adminLogin(request):
    return render(request,'dashboard.html')

def addMedicalOfficer(request):
    return render(request,'Add-officers.html')


def Addshelter(request):
    return render(request,'shelter-add.html')

def Viewshelter(request):
    data = Shelters.objects.all()
    return render(request,'shelters-view.html',{'data':data})


def submitShelter(request):
    if request.method == 'POST':
        name= request.POST.get('name') 
        email= request.POST.get('email') 
        registration_number= request.POST.get('registration_number') 
        street= request.POST.get('street') 
        district= request.POST.get('district') 
        state= request.POST.get('state') 
        pin= request.POST.get('pin') 
        contact_number= request.POST.get('contact_number') 
        status= request.POST.get('status') 
         
        data = Shelters( Name=name,Registration_number=registration_number,location=street,Location_pin=pin,Location_district=district,Location_state=state,Contact_number=contact_number,Email=email,status=status)
        data.save()
    return redirect('Viewshelter')





def deleteShelter(request,cr_id):
     item =Shelters.objects.get(id=cr_id) 
     item.delete()
     messages.info(request,'Rejected')
     return redirect('Viewshelter')  


def deleteJobVacancy(request,cr_id):
     item =Job.objects.get(id=cr_id) 
     item.delete()
     messages.info(request,'Rejected')
     return redirect('ViewJobVacancy')  


def AddJobVacancy(request):
    return render(request,'job-add.html')

def ViewJobVacancy(request):
    data = Job.objects.all()
    return render(request,'job-view.html',{'data':data})

def AddEducation(request):
    return render(request,'admin-add-edu.html')

def ViewEducation(request):
    data = Institution.objects.all()
    return render(request,'view-edu-details.html',{'data':data})

def submitJobVacancy(request):
    if request.method == 'POST':
        name= request.POST.get('name') 
        description= request.POST.get('description') 
        qualification= request.POST.get('qualification') 
        experience= request.POST.get('experience') 
        address= request.POST.get('address') 
        district= request.POST.get('district') 
        state= request.POST.get('state') 
        pin= request.POST.get('pin') 
        salary= request.POST.get('salary') 
        email= request.POST.get('email') 
        contact_number= request.POST.get('contact_number') 
        start_date= request.POST.get('start_date') 
        start_end= request.POST.get('start_end') 
        how_to_apply= request.POST.get('how_to_apply') 
         
         
        data = Job(Job_title=name, qualification=qualification,description=description,location=address,Location_pin=pin,Location_state=state,Location_district=district,salary=salary,Contact_number=contact_number,How_to_apply=how_to_apply,Applications_starts=start_date,Application_end=start_end,email=email,Experience=experience)
        data.save()
    return redirect('ViewJobVacancy')


def submitEducation(request):
    if request.method == 'POST':
        name= request.POST.get('name') 
        qualification= request.POST.get('qualification') 
        duration= request.POST.get('duration') 
        ins_name= request.POST.get('ins_name') 
        ins_number= request.POST.get('ins_number') 
        ins_state= request.POST.get('ins_state') 
        ins_district= request.POST.get('ins_district') 
        ins_pin= request.POST.get('ins_pin') 
        ins_reservation= request.POST.get('ins_reservation') 
        scholarship= request.POST.get('scholarship') 
        start= request.POST.get('start') 
        end= request.POST.get('end') 
        how_to_apply= request.POST.get('how_to_apply') 
        
         
         
        data = Institution(course=name,qualification=qualification,duration=duration,Institution_name=ins_name,Institution_number=ins_number,Institution_state=ins_state,Institution_district=ins_district,Institution_pin=ins_pin,reservation=ins_reservation,scholarship=scholarship,How_to_apply=how_to_apply,Applications_starts=start,Application_end=end)
        data.save()
    return redirect('ViewEducation')


def deleteInstitution(request,cr_id):
     item =Institution.objects.get(id=cr_id) 
     item.delete()
     messages.info(request,'Rejected')
     return redirect('ViewEducation')  



def Addevent(request):
    return render(request,'admn-event-add.html')


def Viewevent(request):
    data = Event.objects.all()
    return render(request,'admn-events.html',{'data':data})


def editEvent(request,cr_id):
     data =Event.objects.get(id=cr_id) 
     return render(request,'admn-event-edit.html',{'data':data})
 
def deleteEvent(request,cr_id):
     item =Event.objects.get(id=cr_id) 
     item.delete()
     messages.info(request,'Rejected')
     return redirect('Viewevent')  


def submitEvent(request):
    if request.method == 'POST':
        event_name= request.POST.get('event_name') 
        description= request.POST.get('description') 
        venue= request.POST.get('venue') 
        location= request.POST.get('location') 
        district= request.POST.get('district') 
        state= request.POST.get('state') 
        pin= request.POST.get('pin') 
        date= request.POST.get('date') 
        time= request.POST.get('time') 
        contact_number= request.POST.get('contact_number') 
        participation= request.POST.get('participation') 
        how_to_apply= request.POST.get('how_to_apply') 
        data = Event(Name=event_name,
                     Description=description,
                     Venue=venue,
                     Participation=participation,
                     Location=location,
                     State=state,
                     District=district,
                     pin=pin,
                     Apply_via=how_to_apply,
                     Date=date,
                     Time=time
                     )
        data.save()
    return redirect('Viewevent')

def submitEditedEvent(request,cr_id):
    if request.method=="POST":
        eve=Event.objects.get(id=cr_id)
        eve.Name=request.POST["event_name"]
        eve.Description=request.POST["description"]
        eve.Venue=request.POST["venue"]
        eve.Participation=request.POST["participation"]
        eve.Location=request.POST["location"]
        eve.State=request.POST["state"]
        eve.District=request.POST["district"]
        eve.pin=request.POST["pin"]
        eve.Apply_via=request.POST["Apply_via"]
        eve.Date=request.POST["date"]
        eve.Time=request.POST["time"]
        eve.save()
        return redirect('Viewevent')
    


def ViewBoardMembers(request):
    data =TransUser.objects.all()
    return render(request,'view-board-members.html',{'data':data})


def acceptBoardMember(request, cr_id):     
    cr = TransUser.objects.get(id=cr_id)
    cr.Userstatus =  1  
    cr.save()
    return redirect('ViewBoardMembers')

def AcceptBoardmemberWithReason(request, cr_id):     
    cr = TransUser.objects.get(id=cr_id)
    acceptreason= request.POST.get('acceptreason') 
    accept_date= request.POST.get('accept_date') 
    cr.Userstatus =  1  
    cr.accept_reason = acceptreason
    cr.accept_date = accept_date
    cr.save()
    return redirect('ViewBoardMembers')

def RejectBoardmemberWithReason(request, cr_id):     
    cr = TransUser.objects.get(id=cr_id)
    rejectreason= request.POST.get('rejectreason') 
    reject_date= request.POST.get('reject_date') 
    cr.Userstatus =  2  
    cr.reject_reason = rejectreason
    cr.reject_date = reject_date
    cr.save()
    return redirect('ViewBoardMembers')

def RejectBoardMember(request, cr_id):     
    cr = TransUser.objects.get(id=cr_id)
    cr.delete()
    messages.info(request,'Rejected')
    return redirect('ViewBoardMembers')


def ViewUsers(request):
    data =TransUser.objects.all()
    return render(request,'view-users.html',{'data':data})

def ViewRejectedUsers(request):
    data =TransUser.objects.all()
    return render(request,'Rejected-users.html',{'data':data})

def ViewRejectedBoardMembers(request):
    data =TransUser.objects.all()
    return render(request,'view_reject_board_mem.html',{'data':data})

def ViewAcceptedBoardMembers(request):
    data =TransUser.objects.all()
    return render(request,'accepted-board-member.html',{'data':data})

def ViewAcceptedUsers(request):
    data =TransUser.objects.all()
    return render(request,'accepted-users.html',{'data':data})

def acceptUser(request, cr_id):     
    cr = TransUser.objects.get(id=cr_id)
    cr.Userstatus =  1  
    cr.save()
    return redirect('ViewUsers')

def RejectUserWithReason(request, cr_id):     
    cr = TransUser.objects.get(id=cr_id)
    rejectreason= request.POST.get('rejectreason') 
    reject_date= request.POST.get('reject_date') 
    cr.Userstatus =  2  
    cr.reject_reason = rejectreason
    cr.reject_date = reject_date
    cr.save()
    return redirect('ViewUsers')


def AcceptUserWithReason(request, cr_id):     
    cr = TransUser.objects.get(id=cr_id)
    acceptreason= request.POST.get('acceptreason') 
    accept_date= request.POST.get('accept_date') 
    cr.Userstatus =  1  
    cr.accept_reason = acceptreason
    cr.accept_date = accept_date
    cr.save()
    return redirect('ViewUsers')


def RejectUser(request, cr_id):     
    cr = TransUser.objects.get(id=cr_id)
    cr.Userstatus =  2  
    cr.save()
    return redirect('ViewRejectedUsers')


def ViewMedicalOfficer(request):
    data =Officer.objects.all()
    return render(request,'view-med-officers.html',{'data':data})

def ViewLegalOfficer(request):
    data =Officer.objects.all()
    return render(request,'view-legal-officers.html',{'data':data})

def deleteMedOfficer(request,cr_id):
     item =Officer.objects.get(id=cr_id) 
     item.delete()
     messages.info(request,'Rejected')
     return redirect('ViewMedicalOfficer')   

def deleteLegalOfficer(request,cr_id):
     item =Officer.objects.get(id=cr_id) 
     item.delete()
     messages.info(request,'Rejected')
     return redirect('ViewLegalOfficer')   

def submitLegalOfficerReject(request,cr_id):
    rejectReason= request.POST.get('rejectReason') 
    reject_date= request.POST.get('reject_date') 

    cr = Officer.objects.get(id=cr_id)
    print("cr=============>",cr)
    cr.Officer_status = 2
    cr.reject_reason = rejectReason
    cr.reject_date = reject_date
    cr.save()
    return redirect('ViewLegalOfficer')

def submitLegalOfficerAccept(request,cr_id):
    acceptReason= request.POST.get('acceptReason') 
    accept_date= request.POST.get('accept_date') 

    cr = Officer.objects.get(id=cr_id)
    print("cr=============>",cr)
    cr.Officer_status = 2
    cr.accept_reason = acceptReason
    cr.accept_date = accept_date
    cr.save()
    return redirect('ViewLegalOfficer')

def submitMedicalOfficerReject(request,cr_id):
    rejectReason= request.POST.get('rejectReason') 
    reject_date= request.POST.get('reject_date') 

    cr = Officer.objects.get(id=cr_id)
    print("cr=============>",cr)
    cr.Officer_status = 2
    cr.reject_reason = rejectReason
    cr.reject_date = reject_date
    cr.save()
    return redirect('ViewMedicalOfficer')


def submitMedicalOfficerAccept(request,cr_id):
    acceptReason= request.POST.get('acceptReason') 
    accept_date= request.POST.get('accept_date') 

    cr = Officer.objects.get(id=cr_id)
    print("cr=============>",cr)
    cr.Officer_status = 2
    cr.accept_reason = acceptReason
    cr.accept_date = accept_date
    cr.save()
    return redirect('ViewMedicalOfficer')


def submitEventReject(request,cr_id):
    rejectReason= request.POST.get('rejectReason') 

    cr = Event.objects.get(id=cr_id)
    print("cr=============>",cr)
    cr.EventStatus = 2
    cr.Reason = rejectReason
    cr.save()
    return redirect('Viewevent')

def postponeEvent(request,cr_id): 
    cr = Event.objects.get(id=cr_id)
    cr.Date = request.POST.get('postpone_date') 
    cr.save()
    return redirect('Viewevent')

def submitMedicalOfficer(request):
    if request.method == 'POST':
        name= request.POST.get('name') 
        email= request.POST.get('email') 
        password= request.POST.get('password') 
        Contact_number= request.POST.get('Contact_number') 
        type= request.POST.get('type')
        image = request.POST.get('image')
        gender= request.POST.get('gender')
        house_name= request.POST.get('house_name')
        street= request.POST.get('street')
        district= request.POST.get('district')
        state= request.POST.get('state')
        pin= request.POST.get('pin')
        register_number= request.POST.get('register_number')
        specialisation= request.POST.get('specialisation')
        qualification1= request.POST.get('qualification1')
        qualification2= request.POST.get('qualification2')
        qualification3= request.POST.get('qualification3')
        other_qualification= request.POST.get('other_qualification')
        office_name= request.POST.get('office_name')
        office_place= request.POST.get('office_place')
        office_number= request.POST.get('office_number')
        office_pin= request.POST.get('office_pin')
        office_state= request.POST.get('office_state')
        office_district= request.POST.get('office_district')

        data = Officer(Name=name,
                       Username=email,
                       Password=password,
                       Gender=gender,
                       Email=email,
                       Contact_number=Contact_number,
                       House_name=house_name,
                       State=state,
                       District=district,
                       Street=street,
                       Pin=pin,
                       Registration_number=register_number,
                       Type=type,
                       Specialisation=specialisation,
                       Qualification_1=qualification1,
                       Qualification_2=qualification2,
                       Qualification_3=qualification3,
                       Other_qualification=other_qualification,
                       office_name=office_name,
                       office_place=office_place,
                       office_number=office_number,
                       office_pin=office_pin,
                       office_state=office_state,
                       office_district=office_district,
                       Officer_status=0,
                       photo=image
                       )
        data.save()

        return redirect('addMedicalOfficer')
    

def viewMedicalBooking(request):
    data =Med_booking.objects.all().values()
    return render(request,'view-medical.html',{'data':data})

def viewLegalbooking(request):
    data =Legal_booking.objects.all().values()
    return render(request,'view-legal-boooking-slot.html',{'data':data})

def viewRejectedLegalOfficer(request):
    data =Legal_booking.objects.all().values()
    return render(request,'rejected-legal-officer.html',{'data':data})

def viewAcceptedLegalOfficer(request):
    data =Legal_booking.objects.all().values()
    return render(request,'accepted-legal-officer.html',{'data':data})

def viewRejectedMedicalOfficer(request):
    data =Med_booking.objects.all().values()
    return render(request,'View_medi_rejcted_officer.html',{'data':data})

def viewAcceptedMedicalOfficer(request):
    data =Med_booking.objects.all().values()
    return render(request,'accepted-med-officer.html',{'data':data})


def searchUsers(request):
    if request.method == 'POST':
        from_date= request.POST.get('from_date') 
        to_date= request.POST.get('to_date') 
        data =TransUser.objects.filter(accept_date__range=(from_date, to_date))
        return render(request,'searched-users.html',{'data':data})  
    
def searchBoardmember(request):
    if request.method == 'POST':
        from_date= request.POST.get('from_date') 
        to_date= request.POST.get('to_date') 
        data =TransUser.objects.filter(accept_date__range=(from_date, to_date))
        return render(request,'searched-board-members.html',{'data':data})  
    
def searchMedicalOfficers(request):
    if request.method == 'POST':
        from_date= request.POST.get('from_date') 
        to_date= request.POST.get('to_date') 
        data = Officer.objects.filter(accept_date__range=(from_date, to_date))
        return render(request,'searched-medical-officers.html',{'data':data})  
    
def searchLegalOfficers(request):
    if request.method == 'POST':
        from_date= request.POST.get('from_date') 
        to_date= request.POST.get('to_date') 
        data =Officer.objects.filter(accept_date__range=(from_date, to_date))
        return render(request,'searched-legal-officers.html',{'data':data})  
    
def searchCourse(request):
    if request.method == 'POST':
        from_date= request.POST.get('from_date') 
        to_date= request.POST.get('to_date') 
        data =Institution.objects.filter(Applications_starts__range=(from_date, to_date))
        return render(request,'searched-course.html',{'data':data})  
        

def ViewBoardMemberEvents(request):
    data = Event.objects.all().values()
    return render (request,'view-board-member-events.html',{'data':data})

def ListMemberEvents(request,cr_id):
     data = Event.objects.get(member_id=cr_id)
     return render (request,'view-board-member-events.html',{'data':data})
