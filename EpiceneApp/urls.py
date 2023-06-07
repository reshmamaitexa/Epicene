from django.urls import path
from EpiceneApp import views

urlpatterns = [
   
   path('login_users', views.LoginUsersAPIView.as_view(), name='login_users'),

   # transuser

   path('user_register', views.UserRegisterAPIView.as_view(), name='user_register'),

   #board

   path('board_register', views.BoardRegisterAPIView.as_view(), name='board_register'),
   path('medical_officer_register', views.MedicalOfficerRegisterAPI.as_view(), name='medical_officer_register'),
   path('legal_officer_register', views.LegalOfficerRegisterAPI.as_view(), name='legal_officer_register'),

  #Education
   path('course', views.CourseAPIView.as_view(), name='course'),

   #JOB

   path('job_details', views.JobAPIView.as_view(), name='job_details'),


   #Shelter


   path('Shelter_details', views.ShelterAPIView.as_view(), name='Shelter_details'),


   #Officers

   path('Legal-Officer', views.OfficerRegisterAPIView.as_view(), name='Legal-Officer'),





###Med_Slot
   path('Med_slot', views.Med_SLotAPIView.as_view(), name='Med_slot'),


#Legal slot


   path('Legal_slot', views.Legal_SLotAPIView.as_view(), name='Legal_slot'),
   

# #medbooking


   path('Med_booking', views.MedicalBookingAPIView.as_view(), name='Med_booking'),


# #legalbooking

   path('Legal_booking', views.LegalBookingAPIView.as_view(), name='Legal_booking'),


#Event

   path('Event', views.EventAPIView.as_view(), name='Event'),


#Eveent Particcipation


   path('Event_participation', views.EventParticipationAPIView.as_view(), name='Event_participation'),


#Institution


   path('Institution', views.InstitutionAPIView.as_view(), name='Institution'),
   path('list_medical_officers/<str:type>', views.getAllMedicalOfficers.as_view(), name='list_medical_officers'),
   path('list_legal_officers/<str:type>', views.getAllLegalOfficers.as_view(), name='list_legal_officers'),
   path('get_user_details/<int:id>', views.GetSingleUserDetails.as_view(), name='get_user_details'),
   path('get_officer_details/<int:id>', views.GetSingleOfficerDetails.as_view(), name='get_officer_details'),
   path('get_medical_slots/<int:id>', views.getAllMedicalSlots.as_view(), name='get_medical_slots'),
   path('get_legal_slots/<int:id>', views.getAllLegalSlots.as_view(), name='get_legal_slots'),
   path('update_user/<int:id>', views.UpdateUserDetails.as_view(), name='update_user'),
   path('all_events', views.getAllEvents.as_view(), name='all_events'),
   path('all_shelters', views.getAllShelters.as_view(), name='all_shelters'),
   path('all_jobvacancy', views.getAllJobVacancy.as_view(), name='all_jobvacancy'),
   path('all_institutions', views.getAllInstitution.as_view(), name='all_institutions'),
   path('book_medical_officer', views.MedicalBooking.as_view(), name='book_medical_officer'),
   path('book_legal_officer', views.LegalOfficerBooking.as_view(), name='book_legal_officer'),
   path('book_event', views.EventBooking.as_view(), name='book_event'),
   path('job_apply', views.JobApplyAPI.as_view(), name='job_apply'),
   path('list_medical_bookings', views.getAllMedicalBooking.as_view(), name='list_medical_bookings'),
   path('list_legal_bookings', views.getAlllegalBooking.as_view(), name='list_legal_bookings'),
   path('list_events', views.getAllEventsBooking.as_view(), name='list_events'),
   path('list_job_applied', views.getAlljobapplied.as_view(), name='list_job_applied'),
   path('update_medical_slot/<int:id>', views.updateMedicalSlots.as_view(), name='update_medical_slot'),
   path('update_legal_slot/<int:id>', views.updateLegalSlots.as_view(), name='update_legal_slot'),
   path('memberCreateEvents', views.memberCreateEvents.as_view(), name='memberCreateEvents'),

]
