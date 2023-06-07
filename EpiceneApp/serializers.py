from rest_framework import serializers
from .models import Login,TransUser,Course,Institution,Job,Shelters,Med_Slot,Officer,Officer,Legal_Slot,Med_booking,Legal_booking,Event,Event_participation,Job_apply

class LoginUsersSerializer (serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = '__all__'


##############################################################################################################################


#user


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransUser
        fields ='__all__' 
    def create(self, validated_data):
        return TransUser.objects.create(**validated_data)


##################################################################################################################################


#board

class BoardRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransUser
        fields ='__all__' 
    def create(self, validated_data):
        return TransUser.objects.create(**validated_data)


####################################################################################################################################        


#education



class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields ='__all__' 
    def create(self, validated_data):
        return Course.objects.create(**validated_data)


#########################################################################################################################################



#Institution


class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields ='__all__' 
    def create(self, validated_data):
        return Institution.objects.create(**validated_data)




################################################################################################################################################


#JOb


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields ='__all__' 
    def create(self, validated_data):
        return Job.objects.create(**validated_data)



##############################################################################################################################################

#shelters
class SheltersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shelters
        fields ='__all__' 
    def create(self, validated_data):
        return Shelters.objects.create(**validated_data)


##############################################################################################################################################


#OFFICERS



class OfficerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Officer
        fields ='__all__' 
    def create(self, validated_data):
        return Officer.objects.create(**validated_data)




##################################################################################################################################################


#MED_SLOT


class MedSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Med_Slot
        fields ='__all__' 
    def create(self, validated_data):
        return Med_Slot.objects.create(**validated_data)



#################################################################################################################################################



#Legal_Slot

class LegalSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Legal_Slot
        fields ='__all__' 
    def create(self, validated_data):
        return Legal_Slot.objects.create(**validated_data)



######################################################################################################################################################


#Med_booking


class MedBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Med_booking
        fields ='__all__' 
    def create(self, validated_data):
        return Med_booking.objects.create(**validated_data)



#####################################################################################################################################################


#Legal_booking


class LegalBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Legal_booking
        fields ='__all__' 
    def create(self, validated_data):
        return Legal_booking.objects.create(**validated_data)



########################################################################################################################################################


#Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields ='__all__' 
    def create(self, validated_data):
        return Event.objects.create(**validated_data)



######################################################################################################################################################


#Event_participation


class EventParticipationBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event_participation
        fields ='__all__' 
    def create(self, validated_data):
        return Event_participation.objects.create(**validated_data)
    
class JobApplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Job_apply
        fields ='__all__' 
    def create(self, validated_data):
        return Job_apply.objects.create(**validated_data)


#####################################################################################################################################################



