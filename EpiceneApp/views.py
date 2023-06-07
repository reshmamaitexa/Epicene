from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from .models import Login, TransUser,Course,Institution,Job,Shelters,Med_Slot,Officer,Legal_Slot,Med_booking,Legal_booking,Event,Event_participation,Job_apply
from EpiceneApp.serializers import LoginUsersSerializer, UserRegisterSerializer,BoardRegisterSerializer,CourseSerializer,InstitutionSerializer,JobSerializer,SheltersSerializer,MedSlotSerializer,OfficerSerializer,LegalSlotSerializer,MedBookingSerializer,LegalBookingSerializer,EventSerializer,EventParticipationBookingSerializer,JobApplySerializer
# Create your views here.


class getAllMedicalOfficers(GenericAPIView):
    serializer_class = OfficerSerializer 
    def get(self,request,type):
        queryset = Officer.objects.all().filter(Type=type).values()
        return Response({'data': queryset, 'message':'Fetched all medical officers', 'success':True}, status=status.HTTP_200_OK)
    
class getAllLegalOfficers(GenericAPIView):
    serializer_class = OfficerSerializer 
    def get(self,request,type):
        queryset = Officer.objects.all().filter(Type=type).values()
        return Response({'data': queryset, 'message':'Fetched all legal officers', 'success':True}, status=status.HTTP_200_OK)
    
class getAllEvents(GenericAPIView):
    serializer_class = EventSerializer 
    def get(self,request):
        queryset = Event.objects.all().values()
        return Response({'data': queryset, 'message':'Fetched all events', 'success':True}, status=status.HTTP_200_OK)
    
class getAllShelters(GenericAPIView):
    serializer_class = EventSerializer 
    def get(self,request):
        queryset = Shelters.objects.all().values()
        return Response({'data': queryset, 'message':'Fetched all Shelters', 'success':True}, status=status.HTTP_200_OK)
    

class getAllJobVacancy(GenericAPIView):
    serializer_class = JobSerializer 
    def get(self,request):
        queryset = Job.objects.all().values()
        return Response({'data': queryset, 'message':'Fetched all JOb Vacancies', 'success':True}, status=status.HTTP_200_OK)
    
class getAllInstitution(GenericAPIView):
    serializer_class = InstitutionSerializer 
    def get(self,request):
        queryset = Institution.objects.all().values()
        return Response({'data': queryset, 'message':'Fetched all Institutions', 'success':True}, status=status.HTTP_200_OK)
    
class GetSingleUserDetails(GenericAPIView):
    serializer_class = UserRegisterSerializer
    def get(self,request,id):
        query = TransUser.objects.get(login_id=id)
        print(query)
        serializer =UserRegisterSerializer(query)
        return Response({'data': serializer.data, 'message':'user details fetched successfully', 'success':True}, status=status.HTTP_200_OK)
    
class GetSingleOfficerDetails(GenericAPIView):
    serializer_class = OfficerSerializer
    def get(self,request,id):
        query = Officer.objects.get(login_id=id)
        print(query)
        serializer =OfficerSerializer(query)
        return Response({'data': serializer.data, 'message':'officer details fetched successfully', 'success':True}, status=status.HTTP_200_OK)
    
class UpdateUserDetails(GenericAPIView):
    serializer_class = UserRegisterSerializer
    def put(self, request, id):
        queryset = TransUser.objects.get(login_id=id)
        print(queryset)
        serializer = UserRegisterSerializer(instance=queryset, data=request.data, partial=True)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data, 'message':'user updated successfully', 'success':True}, status=status.HTTP_200_OK)
        else:
            return Response({'data':[],'message':'something went wrong', 'success':False}, status=status.HTTP_400_BAD_REQUEST)
        

class updateMedicalSlots(GenericAPIView):
    serializer_class = MedSlotSerializer
    def put(self, request, id):
        queryset = Med_Slot.objects.get(id=id)
        print(queryset)
        serializer = MedSlotSerializer(instance=queryset, data=request.data, partial=True)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data, 'message':'Medical slot updated successfully', 'success':True}, status=status.HTTP_200_OK)
        else:
            return Response({'data':[],'message':'something went wrong', 'success':False}, status=status.HTTP_400_BAD_REQUEST)
        

class updateLegalSlots(GenericAPIView):
    serializer_class = LegalSlotSerializer
    def put(self, request, id):
        queryset = Legal_Slot.objects.get(id=id)
        print(queryset)
        serializer = LegalSlotSerializer(instance=queryset, data=request.data, partial=True)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data, 'message':'Legal slot updated successfully', 'success':True}, status=status.HTTP_200_OK)
        else:
            return Response({'data':[],'message':'something went wrong', 'success':False}, status=status.HTTP_400_BAD_REQUEST)
        

class MedicalBooking(GenericAPIView):
    serializer_class = MedBookingSerializer 
    def post(self,request):
        Book_date = request.data.get('Book_date') 
        booking_note = request.data.get('booking_note') 
        Officer_id = request.data.get('Officer_id') 
        TransUser_id =request.data.get('TransUser_id') 
        name =request.data.get('name') 


        Med_book_status = '0'

        serializer = self.serializer_class(data ={'Book_date': Book_date,'name':name, 'booking_note':booking_note,'Med_book_status':Med_book_status,'Officer_id':Officer_id,'TransUser_id':TransUser_id})

        if serializer.is_valid():
             print("hi")
             serializer.save()
             return Response({'data': serializer.data, 'message': 'Booking added successfull', 'success': True}, status = status.HTTP_201_CREATED)

        return Response({'data':serializer.errors, 'message': 'Failed', 'success':False}, status=status.HTTP_400_BAD_REQUEST)
    

class LegalOfficerBooking(GenericAPIView):
    serializer_class = LegalBookingSerializer 
    def post(self,request):
        Book_date = request.data.get('Book_date') 
        booking_note = request.data.get('booking_note') 
        Officer_id = request.data.get('Officer_id') 
        TransUser_id =request.data.get('TransUser_id') 
        name =request.data.get('name') 

        Legal_book_status = '0'

        serializer = self.serializer_class(data ={'Book_date': Book_date,'name':name, 'booking_note':booking_note,'Legal_book_status':Legal_book_status,'Officer_id':Officer_id,'TransUser_id':TransUser_id})

        if serializer.is_valid():
            print("hi")
            serializer.save()
            return Response({'data': serializer.data, 'message': 'Booking successfull', 'success': True}, status = status.HTTP_201_CREATED)

        return Response({'data':serializer.errors, 'message': 'Failed', 'success':False}, status=status.HTTP_400_BAD_REQUEST)
    

class getAlllegalBooking(GenericAPIView):
    serializer_class = LegalBookingSerializer 
    def get(self,request):
        queryset = Legal_booking.objects.all().values()
        return Response({'data': queryset, 'message':'Fetched all legal bookings', 'success':True}, status=status.HTTP_200_OK)
    

class EventBooking(GenericAPIView):
    serializer_class = EventParticipationBookingSerializer 
    def post(self,request):
        Event_id = request.data.get('Event_id') 
        TransUser_id = request.data.get('TransUser_id') 
        Event_note = request.data.get('Event_note') 
        name = request.data.get('name') 

        Participation_status = '0'

        serializer = self.serializer_class(data ={'Event_id': Event_id,'name':name, 'Event_note':Event_note,'TransUser_id':TransUser_id,'Participation_status':Participation_status})

        if serializer.is_valid():
            print("hi")
            serializer.save()
            return Response({'data': serializer.data, 'message': 'Booking successfull', 'success': True}, status = status.HTTP_201_CREATED)

        return Response({'data':serializer.errors, 'message': 'Failed', 'success':False}, status=status.HTTP_400_BAD_REQUEST)
    

class getAllEventsBooking(GenericAPIView):
    serializer_class = EventParticipationBookingSerializer 
    def get(self,request):
        queryset = Event_participation.objects.all().values()
        return Response({'data': queryset, 'message':'Fetched all events', 'success':True}, status=status.HTTP_200_OK)
    

class JobApplyAPI(GenericAPIView):
    serializer_class = JobApplySerializer 
    def post(self,request):
        job_id = request.data.get('job_id') 
        TransUser_id = request.data.get('TransUser_id') 
        job_note = request.data.get('job_note')  
        name = request.data.get('name')  


        application_status = '0'

        serializer = self.serializer_class(data ={'job_id': job_id,'name':name, 'Event_note':job_note,'TransUser_id':TransUser_id,'application_status':application_status})

        if serializer.is_valid():
            print("hi")
            serializer.save()
            return Response({'data': serializer.data, 'message': 'Booking successfull', 'success': True}, status = status.HTTP_201_CREATED)

        return Response({'data':serializer.errors, 'message': 'Failed', 'success':False}, status=status.HTTP_400_BAD_REQUEST)
    

class getAlljobapplied(GenericAPIView):
    serializer_class = JobApplySerializer 
    def get(self,request):
        queryset = Job_apply.objects.all().values()
        return Response({'data': queryset, 'message':'Fetched all jobs applied', 'success':True}, status=status.HTTP_200_OK)
    

    
class getAllMedicalBooking(GenericAPIView):
    serializer_class = MedBookingSerializer 
    def get(self,request):
        queryset = Med_booking.objects.all().values()
        return Response({'data': queryset, 'message':'Fetched all medical bookings', 'success':True}, status=status.HTTP_200_OK)
    
class getAllMedicalSlots(GenericAPIView):
    serializer_class = MedSlotSerializer 
    def get(self,request,id):
        queryset = Med_Slot.objects.all().filter(Officer_id=id).values()
        return Response({'data': queryset, 'message':'Fetched all medical slots', 'success':True}, status=status.HTTP_200_OK)
    
class getAllLegalSlots(GenericAPIView):
    serializer_class = LegalSlotSerializer 
    def get(self,request,id):
        queryset = Legal_Slot.objects.all().filter(Officer_id=id).values()
        return Response({'data': queryset, 'message':'Fetched all legal slots', 'success':True}, status=status.HTTP_200_OK)
    

class MedicalOfficerRegisterAPI(GenericAPIView):
    serializer_class = OfficerSerializer
    serializer_class_login = LoginUsersSerializer

    def post(self,request):
        login_id=''
        Name= request.data.get('Name') 
        username = request.data.get('username')
        password = request.data.get('password')
        Gender= request.data.get('Gender') 
        Email= request.data.get('Email') 
        Contact_number= request.data.get('Contact_number') 
        House_name= request.data.get('House_name') 
        State= request.data.get('State') 
        District= request.data.get('District') 
        Street= request.data.get('Street') 
        Pin= request.data.get('Pin') 
        Registration_number= request.data.get('Registration_number') 
        Specialisation= request.data.get('Specialisation') 
        Qualification_1= request.data.get('Qualification_1') 
        Qualification_2= request.data.get('Qualification_2') 
        Qualification_3= request.data.get('Qualification_3') 
        Other_qualification= request.data.get('Other_qualification') 
        office_name= request.data.get('office_name') 
        office_place= request.data.get('office_place') 
        office_number= request.data.get('office_number') 
        office_pin= request.data.get('office_pin') 
        office_state= request.data.get('office_state') 
        office_district= request.data.get('office_district') 
        photo= request.data.get('photo') 
        User_approach=request.data.get('User_approach')
        Proof_id=request.data.get('Proof_id')
        Proof_type=request.data.get('Proof_type')
        Proof_image=request.data.get('Proof_image')
        

        Type ='doctor'
        Officer_status = '0'

        if (Login.objects.filter(username=username)):

            return Response({'message': 'Duplicate Username Found!'}, status = status.HTTP_400_BAD_REQUEST)

        else:
            serializer_login = self.serializer_class_login(data = {'username': username, 'password' :password, 'role':Type})
        if serializer_login.is_valid():

            log=serializer_login.save() 
            print("logi====>",log)
            login_id=log.id
            print(login_id)
        serializer = self.serializer_class(data={'Name':Name,'Gender':Gender,'Email':Email,'Contact_number':Contact_number,'House_name':House_name,'State':State,'District':District,'Street':Street,'Pin':Pin,'Registration_number':Registration_number,'Specialisation':Specialisation,'Qualification_1':Qualification_1,'Qualification_2':Qualification_2,'Qualification_3':Qualification_3,'Other_qualification':Other_qualification,'Type':Type,'office_name':office_name,'office_place':office_place,'office_number':office_number,'office_pin':office_pin,'office_state':office_state,'office_district':office_district,'login_id':login_id,'photo':photo,'User_approach':User_approach,'Proof_id':Proof_id,'Proof_type':Proof_type,'Proof_image':Proof_image,'Officer_status':Officer_status})
        print(serializer)

        if serializer.is_valid():
             print("hi")
             serializer.save()
             return Response({'data': serializer.data, 'message': 'medical officer registered successfully', 'success': True}, status = status.HTTP_201_CREATED)

        return Response({'data':serializer.errors, 'message': 'Failed', 'success':False}, status=status.HTTP_400_BAD_REQUEST)
    
    
class LegalOfficerRegisterAPI(GenericAPIView):
    serializer_class = OfficerSerializer
    serializer_class_login = LoginUsersSerializer

    def post(self,request):
        login_id =''
        Name= request.data.get('Name') 
        username = request.data.get('username')
        password = request.data.get('password')
        Gender= request.data.get('Gender') 
        Email= request.data.get('Email') 
        Contact_number= request.data.get('Contact_number') 
        House_name= request.data.get('House_name') 
        State= request.data.get('State') 
        District= request.data.get('District') 
        Street= request.data.get('Street') 
        Pin= request.data.get('Pin') 
        Registration_number= request.data.get('Registration_number') 
        Specialisation= request.data.get('Specialisation') 
        Qualification_1= request.data.get('Qualification_1') 
        Qualification_2= request.data.get('Qualification_2') 
        Qualification_3= request.data.get('Qualification_3') 
        Other_qualification= request.data.get('Other_qualification') 
        office_name= request.data.get('office_name') 
        office_place= request.data.get('office_place') 
        office_number= request.data.get('office_number') 
        office_pin= request.data.get('office_pin') 
        office_state= request.data.get('office_state') 
        office_district= request.data.get('office_district') 
        photo= request.data.get('photo') 
        User_approach=request.data.get('User_approach')
        Proof_id=request.data.get('Proof_id')
        Proof_type=request.data.get('Proof_type')
        Proof_image=request.data.get('Proof_image')

        Type ='lawyer'
        Officer_status = '0'

        if (Login.objects.filter(username=username)):

            return Response({'message': 'Duplicate Username Found!'}, status = status.HTTP_400_BAD_REQUEST)

        else:
            serializer_login = self.serializer_class_login(data = {'username': username, 'password' :password, 'role':Type})
        if serializer_login.is_valid():
            log=serializer_login.save() 
            print("logi====>",log)
            login_id=log.id
            print(login_id)
        serializer = self.serializer_class(data={'Name':Name,'Gender':Gender,'Email':Email,'Contact_number':Contact_number,'House_name':House_name,'State':State,'District':District,'Street':Street,'Pin':Pin,'Registration_number':Registration_number,'Specialisation':Specialisation,'Qualification_1':Qualification_1,'Qualification_2':Qualification_2,'Qualification_3':Qualification_3,'Other_qualification':Other_qualification,'Type':Type,'office_name':office_name,'office_place':office_place,'office_number':office_number,'office_pin':office_pin,'office_state':office_state,'office_district':office_district,'login_id':login_id,'photo':photo,'User_approach':User_approach,'Proof_id':Proof_id,'Proof_type':Proof_type,'Proof_image':Proof_image,'Officer_status':Officer_status})
        print(serializer)

        if serializer.is_valid():
             print("hi")
             serializer.save()
             return Response({'data': serializer.data, 'message': 'legal officer registered successfully', 'success': True}, status = status.HTTP_201_CREATED)

        return Response({'data':serializer.errors, 'message': 'Failed', 'success':False}, status=status.HTTP_400_BAD_REQUEST)



class UserRegisterAPIView(GenericAPIView):
    serializer_class = UserRegisterSerializer 
    serializer_class_login = LoginUsersSerializer

    def post(self, request):
        login_id=''
        Name= request.data.get('Name') 
        Gender =request.data.get('Gender')
        Email= request.data.get('Email')
        Dob= request.data.get('Dob') 
        Contact_number= request.data.get('Contact_number') 
        House_name= request.data.get('House_name') 
        State= request.data.get('State') 
        District= request.data.get('District') 
        Street= request.data.get('Street') 
        Pin= request.data.get('Pin') 
        username = request.data.get('username')
        password = request.data.get('password')
        Proof_id= request.data.get('Proof_id') 
        Proof_type= request.data.get('Proof_type') 
        Proof_image= request.data.get('Proof_image') 
        # Action_date=request.data.get('Action_date')
        # Action=request.data.get('Action')
        # Reject_Reason=request.data.get('Reject_Reason')



        
    

        role ='trans_user'
        Userstatus = '0'

        if (Login.objects.filter(username=username)):

            return Response({'message': 'Duplicate Username Found!'}, status = status.HTTP_400_BAD_REQUEST)

        else:

            serializer_login = self.serializer_class_login(data = {'username': username, 'password' :password, 'role':role})

        if serializer_login.is_valid():

            log=serializer_login.save() 
            print("logi====>",log)
            login_id=log.id
            print(login_id)
        serializer = self.serializer_class (data ={'Name': Name, 'Gender':Gender,'Email':Email,'Dob':Dob,'Contact_number':Contact_number,'House_name':House_name,'State':State,'District':District ,'Street':Street,'Pin':Pin,'Proof_type':Proof_type,'Proof_id':Proof_id,'Proof_image':Proof_image,'login_id':login_id,'Userstatus':Userstatus,'role':role})
        print(serializer)


        if serializer.is_valid():
             print("hi")
             serializer.save()
             return Response({'data': serializer.data, 'message': 'user registered successfully', 'success': True}, status = status.HTTP_201_CREATED)

        return Response({'data':serializer.errors, 'message': 'Failed', 'success':False}, status=status.HTTP_400_BAD_REQUEST)


######################################################################################################################################################################################################################################################################################################


#LOGIN

class LoginUsersAPIView(GenericAPIView):

    serializer_class = LoginUsersSerializer
    def post(self, request):

        username = request.data.get('username')
        password = request.data.get('password')

        logreg = Login.objects.filter(username= username, password=password)

        if (logreg.count()>0):
            read_serializer = LoginUsersSerializer(logreg, many=True)
            return Response({'data':read_serializer.data, 'success': True, 'message':'Logged in successfully'}, status = status.HTTP_201_CREATED)
        else:
            return Response({'data': 'username or password is invalid', 'success': False,} , status= status.HTTP_400_BAD_REQUEST)


################################################################################################################################################################################################################################################################################################


#Board Members


class BoardRegisterAPIView(GenericAPIView):
    serializer_class = BoardRegisterSerializer 
    serializer_class_login =LoginUsersSerializer

    def post(self, request):
        login_id=''
        Name= request.data.get('Name') 
        Gender =request.data.get('Gender')
        Email= request.data.get('Email')
        Dob= request.data.get('Dob') 
        Contact_number= request.data.get('Contact_number') 
        House_name= request.data.get('House_name') 
        State= request.data.get('State') 
        District= request.data.get('District') 
        Street= request.data.get('Street') 
        Pin= request.data.get('Pin') 
        username = request.data.get('username')
        password = request.data.get('password')
        Proof_id= request.data.get('Proof_id') 
        Proof_type= request.data.get('Proof_type') 
        Proof_image= request.data.get('Proof_image') 


        
        # Age=request.data.get('Age') 
        # Userstatus= request.data.get('Userstatus') 
        # Street= request.data.get('Street') 
        # username = request.data.get('username')
        # password = request.data.get('password')

        role ='Brdmember'
        Userstatus = '0'

        if (Login.objects.filter(username=username)):

            return Response({'message': 'Duplicate Username Found!'}, status = status.HTTP_400_BAD_REQUEST)

        else:

            serializer_login = self.serializer_class_login(data = {'username': username, 'password' :password, 'role':role})

        if serializer_login.is_valid():

            log=serializer_login.save() 
            print("logi====>",log)
            login_id=log.id
            print(login_id)
        serializer = self.serializer_class (data ={'Name': Name, 'Gender':Gender,'Email':Email,'Dob':Dob,'Contact_number':Contact_number,'House_name':House_name,'State':State,'District':District ,'Street':Street,'Pin':Pin,'Proof_type':Proof_type,'Proof_id':Proof_id,'Proof_image':Proof_image,'login_id':login_id,'Userstatus':Userstatus,'role':role})
        print(serializer)


        if serializer.is_valid():
             print("hi")
             serializer.save()
             return Response({'data': serializer.data, 'message': 'Board member registered successfully', 'success': True}, status = status.HTTP_201_CREATED)

        return Response({'data':serializer.errors, 'message': 'Failed', 'success':False}, status=status.HTTP_400_BAD_REQUEST)


####################################################################################################################################################################################################################################################################################################


#Course

class  CourseAPIView(GenericAPIView):
    serializer_class = CourseSerializer 
       
    def post(self, request):

        course = request.data.get('course') 
        qualification = request.data.get('qualification') 
        duration = request.data.get('duration') 
        course_status = request.data.get('course_status')


        # reservation = request.data.get('reservation') 
        # Dob = models.CharField(max_length=50)
        # Institution_name = request.data.get('Institution_name') 
        # Institution_number = request.data.get('Institution_number') 
        # Institution_state = request.data.get('Institution_state') 
        # Institution_district =request.data.get('Institution_district') 
        # Institution_pin = request.data.get('Institution_pin') 
        # scholarship = request.data.get('scholarship') 
        # How_to_apply = request.data.get('How_to_apply') 
        # Applications_starts = request.data.get('Applications_starts') 
        # Application_end = request.data.get('Application_end') 


        role ='Course'
        course_status = '0'

    
        serializer = self.serializer_class (data ={'course': course, 'qualification':qualification,'duration':duration,'course_status':course_status,'role':role})
        print(serializer)


        if serializer.is_valid():
             print("hi")
             serializer.save()
             return Response({'data': serializer.data, 'message': 'user registered successfully', 'success': True}, status = status.HTTP_201_CREATED)

        return Response({'data':serializer.errors, 'message': 'Failed', 'success':False}, status=status.HTTP_400_BAD_REQUEST)



########################################################################################################################################################################################################################################3




# Institution

InstitutionSerializer

class  InstitutionAPIView(GenericAPIView):
    serializer_class = InstitutionSerializer 
       
    def post(self, request):

        Institution_name = request.data.get('Institution_name') 
        reservation = request.data.get('reservation') 
        Institution_number = request.data.get('Institution_number') 
        Institution_state = request.data.get('Institution_state') 
        Institution_district =request.data.get('Institution_district') 
        Institution_pin = request.data.get('Institution_pin') 
        scholarship = request.data.get('scholarship') 
        How_to_apply = request.data.get('How_to_apply') 
        Applications_starts = request.data.get('Applications_starts') 
        Application_end = request.data.get('Application_end') 


        # role ='Course'
        institution_status = '0'

    
        serializer = self.serializer_class (data ={'Institution_name': Institution_name,'reservation':reservation,'Institution_number':Institution_number,'Institution_state':Institution_state,'Institution_district':Institution_district,'Institution_pin':Institution_pin,'scholarship':scholarship,'How_to_apply':How_to_apply,'Applications_starts':Applications_starts,'Application_end':Application_end,'institution_status':institution_status,'role':role})
        print(serializer)


        if serializer.is_valid():
             print("hi")
             serializer.save()
             return Response({'data': serializer.data, 'message': 'user registered successfully', 'success': True}, status = status.HTTP_201_CREATED)

        return Response({'data':serializer.errors, 'message': 'Failed', 'success':False}, status=status.HTTP_400_BAD_REQUEST)









# #JOB


class  JobAPIView(GenericAPIView):
    serializer_class = JobSerializer 
       
    def post(self, request):

        Job_title = request.data.get('Job_title') 
        qualification = request.data.get('qualification') 
        description = request.data.get('description') 
        # Dob = models.CharField(max_length=50)
        location = request.data.get('location') 
        Location_pin = request.data.get('Location_pin') 
        Location_state = request.data.get('Location_state') 
        Location_district =request.data.get('Location_district') 
        salary = request.data.get('salary') 
        Contact_number = request.data.get('Contact_number') 
        How_to_apply = request.data.get('How_to_apply') 
        Applications_starts = request.data.get('Applications_starts') 
        Application_end = request.data.get('Application_end')
        email = request.data.get('email') 
        Experience = request.data.get('Experience') 
 


        # Job_status = request.data.get('Job_status')

        role = 'Job'
        Job_status='0'

        serializer = self.serializer_class (data ={'Job_title': Job_title, 'qualification':qualification,'description':description,'location':location,'Location_pin':Location_pin,'Location_state':Location_state,'Location_district':Location_district,'salary':salary,'Contact_number':Contact_number,'How_to_apply':How_to_apply,'Applications_starts':Applications_starts,'Application_end':Application_end,'email':email,'Experience':Experience,'Job_status':Job_status,'role':role})
        print(serializer)


        if serializer.is_valid():
             print("hi")
             serializer.save()
             return Response({'data': serializer.data, 'message': 'user registered successfully', 'success': True}, status = status.HTTP_201_CREATED)

        return Response({'data':serializer.errors, 'message': 'Failed', 'success':False}, status=status.HTTP_400_BAD_REQUEST)


####################################################################################################################################################################################################################################################################################################################################################################



# #Shelters

class  ShelterAPIView(GenericAPIView):
    serializer_class = SheltersSerializer 
       
    def post(self, request):

        Name = request.data.get('Name') 
        Registration_number = request.data.get('Registration_number') 
        # description = request.data.get('description') 
        # Dob = models.CharField(max_length=50)
        location = request.data.get(' location') 
        Location_pin = request.data.get('Location_pin') 
        Location_state = request.data.get('Location_state') 
        Location_district =request.data.get('Location_district') 
        Contact_number = request.data.get('Contact_number') 
        Email=request.data.get('Email')
        How_to_apply = request.data.get('How_to_apply')

        role = 'Shelters'
        Shelters_status = '0'

        
        serializer = self.serializer_class (data ={'Name': Name, 'Registration_number':Registration_number,'location':location,'Location_pin':Location_pin,'Location_state':Location_state,'Location_district':Location_district,'Contact_number':Contact_number,'Email':Email,'Shelters_status':Shelters_status,'role':role})
        print(serializer)


        if serializer.is_valid():
             print("hi")
             serializer.save()
             return Response({'data': serializer.data, 'message': 'user registered successfully', 'success': True}, status = status.HTTP_201_CREATED)

        return Response({'data':serializer.errors, 'message': 'Failed', 'success':False}, status=status.HTTP_400_BAD_REQUEST)


###########################################################################################################################################################################################################################################################################################################################




#Officers



class OfficerRegisterAPIView(GenericAPIView):
    serializer_class = OfficerSerializer 
    serializer_class_login = LoginUsersSerializer

    def post(self, request):
        login_id=''
        Name= request.data.get('Name') 
        Gender =request.data.get('Gender')
        Username = request.data.get('Username')
        Password = request.data.get('Password')
        Email= request.data.get('Email')
        Contact_number= request.data.get('Contact_number') 
        House_name= request.data.get('House_name') 
        State= request.data.get('State') 
        District= request.data.get('District') 
        Street= request.data.get('Street') 
        Pin= request.data.get('Pin') 
        Registration_number= request.data.get('Registration_number') 
        Type = request.data.get('Type') 
        Specialisation= request.data.get('Specialisation') 
        Qualification_1= request.data.get('Qualification_1') 
        
        Qualification_2=request.data.get('Qualification_2') 
        Qualification_3= request.data.get('Qualification_3') 
        Other_qualification= request.data.get('Other_qualification') 
        office_name = request.data.get('office_name')
        office_place = request.data.get('office_place')
        office_number=request.data.get('office_number') 
        office_pin= request.data.get('office_pin') 
        office_state= request.data.get('office_state') 
        office_district = request.data.get('office_district')
        photo=request.data.get('photo')
        User_approach=request.data.get('User_approach')
        Proof_id=request.data.get('Proof_id')
        Proof_type=request.data.get('Proof_type')
        Proof_image=request.data.get('Proof_image')



        
       

        role ='officer'
        Officer_status = '0'

        if (Login.objects.filter(username=Username)):

            return Response({'message': 'Duplicate Username Found!'}, status = status.HTTP_400_BAD_REQUEST)

        else:

            serializer_login = self.serializer_class_login(data = {'username': Username, 'Password' :Password, 'role':role})

        if serializer_login.is_valid():

            log=serializer_login.save() 
            login_id=log.id
            print(login_id)
        serializer = self.serializer_class (data ={'Name': Name, 'Gender':Gender,'Email':Email,'Contact_number':Contact_number,'House_name':House_name,'State':State,'District':District ,'Street':Street,'Pin':Pin,'Registration_number':Registration_number,'Type':Type,'Specialisation':Specialisation,'Qualification_1':Qualification_1,'Qualification_2':Qualification_2,'Qualification_3':Qualification_3,'Other_qualification':Other_qualification,'office_name':office_name,'office_place':office_place,'office_number':office_number,'office_pin':office_pin,'office_state':office_state,'office_district':office_district,'Officer_status':Officer_status,'photo':photo,'User_approach':User_approach,'Proof_id':Proof_id,'Proof_type':Proof_type,'Proof_image':Proof_image,'login_id':login_id,'Username':Username,'Password':Password,'role':role})
        print(serializer)


        if serializer.is_valid():
             print("hi")
             serializer.save()
             return Response({'data': serializer.data, 'message': 'user registered successfully', 'success': True}, status = status.HTTP_201_CREATED)

        return Response({'data':serializer.errors, 'message': 'Failed', 'success':False}, status=status.HTTP_400_BAD_REQUEST)





# # #Med_SLot


class  Med_SLotAPIView(GenericAPIView):
    serializer_class = MedSlotSerializer 
       
    def post(self, request):

        Start_date = request.data.get('Start_date') 
        End_date = request.data.get('End_date') 
        Slot_start_time = request.data.get('Slot_start_time') 
        Slot_end_time = request.data.get('Slot_end_time') 
        Number_of_token = request.data.get('Number_of_token') 
        Officer_id = request.data.get('Officer_id')

        
        Med_Slot_status = '0'

        
        serializer = self.serializer_class (data ={'Start_date': Start_date, 'End_date':End_date,'Slot_start_time':Slot_start_time,'Slot_end_time':Slot_end_time,'Number_of_token':Number_of_token,'Med_Slot_status':Med_Slot_status,'Officer_id':Officer_id})
        print(serializer)


        if serializer.is_valid():
             print("hi")
             serializer.save()
             return Response({'data': serializer.data, 'message': 'medical slots created', 'success': True}, status = status.HTTP_201_CREATED)

        return Response({'data':serializer.errors, 'message': 'Failed', 'success':False}, status=status.HTTP_400_BAD_REQUEST)



########################################################################################################################################################################################################################################

# Slot_legal

class  Legal_SLotAPIView(GenericAPIView):
    serializer_class = LegalSlotSerializer 
       
    def post(self, request):

        Start_date = request.data.get('Start_date') 
        End_date = request.data.get('End_date') 
        Slot_start_time = request.data.get('Slot_start_time') 
        Slot_end_time = request.data.get('Slot_end_time') 
        Number_of_Slots = request.data.get('Number_of_Slots') 
        Officer_id = request.data.get('Officer_id')

        
        Legal_Slot_status = '0'

        
        serializer = self.serializer_class (data ={'Start_date': Start_date, 'End_date':End_date,'Slot_start_time':Slot_start_time,'Slot_end_time':Slot_end_time,'Number_of_Slots':Number_of_Slots,'Legal_Slot_status':Legal_Slot_status,'Officer_id':Officer_id})
        print(serializer)


        if serializer.is_valid():
             print("hi")
             serializer.save()
             return Response({'data': serializer.data, 'message': 'legal slot created', 'success': True}, status = status.HTTP_201_CREATED)

        return Response({'data':serializer.errors, 'message': 'Failed', 'success':False}, status=status.HTTP_400_BAD_REQUEST)



# ###############################################################################################################################################################################################################################################


# # # MEdical BOOKING

class  MedicalBookingAPIView(GenericAPIView):
    serializer_class = MedBookingSerializer 
       
    def post(self, request):

        Book_date = request.data.get('Book_date') 
        Token = request.data.get('Token') 
        Med_book_status = request.data.get(' Med_book_status') 
         

        role = 'MedBook'
        Med_book_status = '0'

        
        serializer = self.serializer_class (data ={'Book_date': Book_date, 'Token':Token,'Med_book_status':Med_book_status,'role':role})
        print(serializer)


        if serializer.is_valid():
             print("hi")
             serializer.save()
             return Response({'data': serializer.data, 'message': 'user registered successfully', 'success': True}, status = status.HTTP_201_CREATED)

        return Response({'data':serializer.errors, 'message': 'Failed', 'success':False}, status=status.HTTP_400_BAD_REQUEST)

# ################################################################################################################################################################################################################################################


# #Legal Booking


class  LegalBookingAPIView(GenericAPIView):
    serializer_class = LegalBookingSerializer 
       
    def post(self, request):

        Book_date = request.data.get('Book_date') 
        Time_slot = request.data.get('Time_slot') 
        Legal_book_status = request.data.get(' Legal_book_status') 
         

        role = 'LegalBook'
        Legal_book_status = '0'

        
        serializer = self.serializer_class (data ={'Book_date': Book_date, 'Time_slot':Time_slot,'Legal_book_status':Legal_book_status,'role':role})
        print(serializer)


        if serializer.is_valid():
             print("hi")
             serializer.save()
             return Response({'data': serializer.data, 'message': 'user registered successfully', 'success': True}, status = status.HTTP_201_CREATED)

        return Response({'data':serializer.errors, 'message': 'Failed', 'success':False}, status=status.HTTP_400_BAD_REQUEST)




# ###############################################################################################################################################################################################################################################


# #EVENT


class  EventAPIView(GenericAPIView):
    serializer_class = EventSerializer 
       
    def post(self, request):

        Name = request.data.get('Name') 
        Description = request.data.get('Description') 
        Venue = request.data.get(' Venue') 
        Date = request.data.get('Date') 
        Time = request.data.get('Time') 
        Participation =request.data.get('Participation') 
        Location = request.data.get('Location') 
        State = request.data.get('State')
        District = request.data.get('District') 
        pin =request.data.get('pin') 
        EventStatus = request.data.get('EventStatus') 
        Reason = request.data.get('Reason')
        Apply_via = request.data.get('Apply_via')


        role = 'Event'
        EventStatus = '0'

        
        serializer = self.serializer_class (data ={'Name': Name, 'Description':Description,'Venue':Venue,'Date':Date,'Time':Time,'Participation':Participation,'Location':Location,'State':State,'District':District,'pin':pin,'EventStatus':EventStatus,'Reason':Reason,'Apply_via':Apply_via,'role':role})
        print(serializer)


        if serializer.is_valid():
             print("hi")
             serializer.save()
             return Response({'data': serializer.data, 'message': 'user registered successfully', 'success': True}, status = status.HTTP_201_CREATED)

        return Response({'data':serializer.errors, 'message': 'Failed', 'success':False}, status=status.HTTP_400_BAD_REQUEST)





# ###############################################################################################################################################################################################################################################################################################################################


# #Event_participation


class   EventParticipationAPIView(GenericAPIView):
    serializer_class = EventParticipationBookingSerializer 
       
    def post(self, request):

        Participation_status = request.data.get(' Participation_status') 
         

        role = 'E-Part'
        Legal_book_status = '0'

        
        serializer = self.serializer_class (data ={'Participation_status': Participation_status,'role':role})
        print(serializer)


        if serializer.is_valid():
             print("hi")
             serializer.save()
             return Response({'data': serializer.data, 'message': 'user registered successfully', 'success': True}, status = status.HTTP_201_CREATED)

        return Response({'data':serializer.errors, 'message': 'Failed', 'success':False}, status=status.HTTP_400_BAD_REQUEST)


##################################################################################################


class memberCreateEvents(GenericAPIView):
    serializer_class = EventSerializer

    def post(self, request):

        Name = request.data.get('Name') 
        Description = request.data.get('Description') 
        Venue = request.data.get('Venue') 
        Date = request.data.get('Date') 
        Time = request.data.get('Time') 
        Participation = request.data.get('Participation') 
        Location = request.data.get('Location') 
        State = request.data.get('State') 
        District= request.data.get('District') 
        pin= request.data.get('pin') 
        member_id= request.data.get('member_id') 
        Apply_via= request.data.get('Apply_via') 
        
        EventStatus = '0'

        serializer = self.serializer_class (data ={'Name': Name,'Description':Description,'Venue':Venue ,'Date':Date,'Time':Time,'Participation':Participation,'Location':Location,'State':State,'District':District,'pin':pin,'member_id':member_id,'Apply_via':Apply_via,'EventStatus':EventStatus})
        print(serializer)


        if serializer.is_valid():
             print("hi")
             serializer.save()
             return Response({'data': serializer.data, 'message': 'event created successfully', 'success': True}, status = status.HTTP_201_CREATED)

        return Response({'data':serializer.errors, 'message': 'Failed', 'success':False}, status=status.HTTP_400_BAD_REQUEST)