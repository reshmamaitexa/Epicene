from django.db import models

# Create your models here.
class Login(models.Model):

    username = models.CharField(max_length=20, unique=True) 
    password = models.CharField(max_length=20, unique=True) 
    role = models.CharField(max_length=10)

    def __str__(self):
        return self.username

# ##############################################################################################################

#TRansUSER

class TransUser(models.Model):
    Name = models.CharField(max_length= 20)
    Gender = models.CharField(max_length= 20)
    Email = models.CharField(max_length= 20)
    Dob = models.CharField(max_length=50)
    Contact_number = models.CharField(max_length=20)
    House_name = models.CharField(max_length=20)
    State = models.CharField(max_length=20)
    District = models.CharField(max_length=20)
    Street = models.CharField(max_length=20)
    Pin = models.CharField(max_length=20)
    # Board_mem
    Userstatus = models.CharField(max_length=20)
    # Age = models.CharField(max_length=5)
    Proof_type = models.CharField(max_length=50, blank=True, null=True)
    Proof_id = models.CharField(max_length=50, blank=True, null=True)
    Proof_image =  models.ImageField(upload_to='images/', blank=True, null=True)
    accept_date=models.CharField(max_length=50, blank=True, null=True)
    accept_reason=models.CharField(max_length=50, blank=True, null=True)
    reject_reason= models.CharField(max_length=50, blank=True, null=True)
    reject_date= models.CharField(max_length=50, blank=True, null=True)
    # Reject_date=models.CharField(max_length=50)
    login_id = models.OneToOneField(Login, on_delete=models.CASCADE)
    role = models.CharField(max_length=10)
    def __str__(self):
        return self.Name
    



#########################################################################################################################


#COURSE


class Course(models.Model):
    #instistution
    course = models.CharField(max_length= 20)
    qualification = models.CharField(max_length= 20)
    duration = models.CharField(max_length= 20)
    course_status = models.CharField(max_length= 20)
    # Institution_id = models.OneToOneField(Institution, on_delete=models.CASCADE)
    # role = models.CharField(max_length=10)
    def __str__(self):
       return self.course


############################################################################################################


# INSTITUTION


class Institution(models.Model):

    course = models.CharField(max_length= 20)
    qualification = models.CharField(max_length= 20)
    duration = models.CharField(max_length= 20)
    Institution_name = models.CharField(max_length=20)
    Institution_number = models.CharField(max_length=20)
    Institution_state = models.CharField(max_length=20)
    Institution_district = models.CharField(max_length=20)
    Institution_pin = models.CharField(max_length=20)
    reservation = models.CharField(max_length= 20)
    scholarship = models.CharField(max_length=20)
    How_to_apply = models.CharField(max_length=20)
    Applications_starts = models.CharField(max_length=20)
    Application_end = models.CharField(max_length=20)


    institution_status = models.CharField(max_length=20)
    # role = models.CharField(max_length=10)
    def __str__(self):
       return self.course



###########################################################################################################


#JOB



class Job(models.Model):
    Job_title = models.CharField(max_length= 20)
    qualification = models.CharField(max_length= 20)
    description = models.CharField(max_length= 20)
    # Dob = models.CharField(max_length=50)
    location = models.CharField(max_length=20)
    Location_pin = models.CharField(max_length=20)
    Location_state = models.CharField(max_length=20)
    Location_district = models.CharField(max_length=20)
    salary = models.CharField(max_length=20)
    Contact_number = models.CharField(max_length=20)
    How_to_apply = models.CharField(max_length=20)
    Applications_starts = models.CharField(max_length=20)
    Application_end = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    Experience = models.CharField(max_length=20)


    Job_status = models.CharField(max_length=20)

    # login_id = models.OneToOneField(Login, on_delete=models.CASCADE)
    # role = models.CharField(max_length=10)
    def __str__(self):
       return self.Job_title



#######################################################################################################################



#SHELTERS



class Shelters(models.Model):
    Name = models.CharField(max_length= 20)
    Registration_number = models.CharField(max_length= 20)
    location = models.CharField(max_length=20)
    Location_pin = models.CharField(max_length=20)
    Location_state = models.CharField(max_length=20)
    Location_district = models.CharField(max_length=20)
    Contact_number = models.CharField(max_length=20)
    Email=models.CharField(max_length=30)
    Shelters_status = models.CharField(max_length=20)
    status = models.CharField(max_length=20)

    # login_id = models.OneToOneField(Login, on_delete=models.CASCADE)
    # role = models.CharField(max_length=10)
    def __str__(self):
       return self.Name



#########################################################################################################################


# # #Officers





class Officer(models.Model):
    # username,password,img
    Name = models.CharField(max_length= 20)
    Gender = models.CharField(max_length= 20)
    Email = models.CharField(max_length= 20)
    Contact_number = models.CharField(max_length=20)
    House_name = models.CharField(max_length=20)
    State = models.CharField(max_length=20)
    District = models.CharField(max_length=20)
    Street = models.CharField(max_length=20)
    Pin = models.CharField(max_length=20)
    Registration_number = models.CharField(max_length=20)
    Type = models.CharField(max_length=20)
    Specialisation = models.CharField(max_length=20)
    Qualification_1 = models.CharField(max_length=20)
    Qualification_2 = models.CharField(max_length=20)
    Qualification_3 = models.CharField(max_length=20)
    Other_qualification = models.CharField(max_length=20)
    office_name = models.CharField(max_length=20)
    office_place = models.CharField(max_length=20)
    office_number = models.CharField(max_length=20)
    office_pin = models.CharField(max_length=20)
    office_state = models.CharField(max_length=20)
    office_district = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='images/', blank=True, null=True)
    login_id = models.OneToOneField(Login, on_delete=models.CASCADE)
    Officer_status = models.CharField(max_length=20)
    User_approach=models.CharField(max_length=10, blank=True, null=True)
    accept_date=models.CharField(max_length=50, blank=True, null=True)
    accept_reason=models.CharField(max_length=20, blank=True, null=True)
    reject_reason= models.CharField(max_length=50, blank=True, null=True)
    reject_date= models.CharField(max_length=50, blank=True, null=True)
    Proof_id=models.CharField(max_length=50, blank=True, null=True)
    Proof_type=models.CharField(max_length=20, blank=True, null=True)
    Proof_image=models.ImageField(upload_to='images/', blank=True, null=True)
    def __str__(self):
       return self.Name


##########################################################################################################################



# #Slot




class Med_Slot(models.Model):
    Start_date = models.CharField(max_length= 20)
    End_date = models.CharField(max_length=20)
    Slot_start_time = models.CharField(max_length=20)
    Slot_end_time = models.CharField(max_length=20)
    Number_of_token = models.CharField(max_length=20)

    Med_Slot_status = models.CharField(max_length=20)

    Officer_id = models.OneToOneField(Officer, on_delete=models.CASCADE)


    def __str__(self):
       return self.Name


################################################################################################################


# #Slot_legal




class Legal_Slot(models.Model):
    Start_date = models.CharField(max_length= 20)
    End_date = models.CharField(max_length=20)
    Slot_start_time = models.CharField(max_length=20)
    Slot_end_time = models.CharField(max_length=20)
    Number_of_Slots = models.CharField(max_length=20)

    Legal_Slot_status = models.CharField(max_length=20)

    Officer_id = models.OneToOneField(Officer, on_delete=models.CASCADE)

 
    def __str__(self):
       return self.Name
   

###############################################################################################################

# # MEdical BOOKING



class Med_booking(models.Model):
    Book_date = models.CharField(max_length= 20)
    Med_book_status = models.CharField(max_length=20)
    booking_note = models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    Officer_id = models.OneToOneField(Officer, on_delete=models.CASCADE)
    TransUser_id = models.OneToOneField(TransUser, on_delete=models.CASCADE)
    med_slot_id = models.OneToOneField(Med_Slot, on_delete=models.CASCADE)


    def __str__(self):
       return self.Name
    


##########################################################################################################


####Legal Booking



class Legal_booking(models.Model):
    Book_date = models.CharField(max_length= 20)
    Legal_book_status = models.CharField(max_length=20)
    booking_note = models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    Officer_id = models.OneToOneField(Officer, on_delete=models.CASCADE)
    TransUser_id = models.OneToOneField(TransUser, on_delete=models.CASCADE)
    legal_slot_id = models.OneToOneField(Legal_Slot, on_delete=models.CASCADE)




    def __str__(self):
       return self.Name
    

##########################################################################################################



####EVENT



class Event(models.Model):
    Name = models.CharField(max_length= 20)
    Description = models.CharField(max_length= 20)
    Venue = models.CharField(max_length=20)
    Date = models.CharField(max_length=20)
    Time = models.CharField(max_length=20)
    Participation = models.CharField(max_length=20)
    Location = models.CharField(max_length=20)
    State = models.CharField(max_length=20)
    District = models.CharField(max_length=20)
    pin = models.CharField(max_length=20)
    EventStatus = models.CharField(max_length=20)
    Reason = models.CharField(max_length=20,blank=True,null=True)
    member_id = models.OneToOneField(TransUser, on_delete=models.CASCADE,blank=True,null=True)
    Apply_via = models.CharField(max_length=20)
   


    def __str__(self):
       return self.Name
    # Officer_id = models.OneToOneField(Officer, on_delete=models.CASCADE)


####################################################################################################


######Event Participation




class Event_participation(models.Model):

    Event_id = models.OneToOneField(Event, on_delete=models.CASCADE)
    TransUser_id = models.OneToOneField(TransUser, on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    Event_note = models.CharField(max_length=100)
    Participation_status=models.CharField(max_length=20)

    def __str__(self):
       return self.Name
    
class Job_apply(models.Model):
    job_id = models.OneToOneField(Job, on_delete=models.CASCADE)
    TransUser_id = models.OneToOneField(TransUser, on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    job_note = models.CharField(max_length=100)
    application_status=models.CharField(max_length=20)

    def __str__(self):
       return self.Name


    