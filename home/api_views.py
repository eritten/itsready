# importing contactSerializer, smsSerializer, voiceMailSerializer, userSerializer from serializers.py
from .serializers import ContactSerializer, SmsSerializer, VoiceMailSerializer, NoteSerializer, CreditCardSerializer
# importing Contact, Sms, VoiceMail, User from models.py
from .models import Contact, Sms, VoiceMail, User, CreditCard
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

# importing api view and status and response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
# importing Q for for search 
from django.db.models import Q
from django.contrib.auth.models import User
# make_password for password encryption
from django.contrib.auth.hashers import make_password
from .models import Profile

# view to add contact. using user id to add contact. user is as request.data.get("userid"). use functional based view. contact information contact_name, contact_email, contact_telephonenumber is as request.data.get("contact_name"), request.data.get("contact_email"), request.data.get("contact_telephonenumber")
@api_view(['POST'])
def add_contact(request):
    if request.method == 'POST':
        user = request.data.get("userid")
        contact_name = request.data.get("contact_name")
        contact_email = request.data.get("contact_email")
        contact_telephonenumber = request.data.get("contact_phone_number")
        # if contact_name, contact_email, contact_telephonenumber is not empty then add contact
        if contact_name and contact_email and contact_telephonenumber:
            # get user from User model
            user = User.objects.get(id=user)
            # create contact using Contact model
            contact = Contact.objects.create(user=user, contact_name=contact_name, contact_email=contact_email, contact_phone_number=contact_telephonenumber)
            # save contact
            contact.save()
            # return response as contact added successfully
            return Response({"message": "Contact added successfully"}, status=status.HTTP_201_CREATED)
        # else return response as contact not added
        else:
            return Response({"message": "Contact not added"}, status=status.HTTP_400_BAD_REQUEST)
        
# view to get contact. using user id to get contacts. user is as request.query_params.get("userid"). use functional based view.
@api_view(['GET'])
def get_contacts(request):
    if request.method == 'GET':
        user = request.query_params.get("userid")
        # if user is not empty then get contact
        if user:
            # get user from User model
            user = User.objects.get(id=user)
            # get contacts using Contact model
            contacts = Contact.objects.filter(user=user)
            # serialize contacts using ContactSerializer
            serializer = ContactSerializer(contacts, many=True)
            # return response as contacts
            return Response(serializer.data, status=status.HTTP_200_OK)
        # else return response as no contacts found
        else:
            return Response({"message": "No contacts found"}, status=status.HTTP_400_BAD_REQUEST)
        
        
# view to delete contact. using contact id to delete contact. contact is as request.data.get("contactid"). use functional based view.
@api_view(['DELETE'])
def delete_contact(request):
    if request.method == 'DELETE':
        contact = request.data.get("contactid")
        # if contact is not empty then delete contact
        if contact:
            # get contact from Contact model
            contact = Contact.objects.get(id=contact)
            # delete contact
            contact.delete()
            # return response as contact deleted successfully
            return Response({"message": "Contact deleted successfully"}, status=status.HTTP_200_OK)
        # else return response as contact not deleted
        else:
            return Response({"message": "Contact not deleted"}, status=status.HTTP_400_BAD_REQUEST)
        
# view to update contact. using contact id to update contact. contact is as request.data.get("contactid"). use functional based view. contact information contact_name, contact_email, contact_telephonenumber is as request.data.get("contact_name"), request.data.get("contact_email"), request.data.get("contact_telephonenumber")
@api_view(['PUT'])
def update_contact(request):
    if request.method == 'PUT':
        contact = request.data.get("contactid")
        contact_name = request.data.get("contact_name")
        contact_email = request.data.get("contact_email")
        contact_telephonenumber = request.data.get("contact_phone_number")
        # if contact is not empty then update contact
        if contact:
            # get contact from Contact model
            contact = Contact.objects.get(id=contact)
            # if contact_name is not empty then update contact_name
            if contact_name:
                contact.contact_name = contact_name
            # if contact_email is not empty then update contact_email
            if contact_email:
                contact.contact_email = contact_email
            # if contact_telephonenumber is not empty then update contact_telephonenumber
            if contact_telephonenumber:
                contact.contact_phone_number = contact_telephonenumber
            # save contact
            contact.save()
            # return response as contact updated successfully
            return Response({"message": "Contact updated successfully"}, status=status.HTTP_200_OK)
        # else return response as contact not updated
        else:
            return Response({"message": "Contact not updated"}, status=status.HTTP_400_BAD_REQUEST)
#  view to search for contact_name, contact_email, contact_telephonenumber. using user id to search contact. user is as request.query_params.get("userid"). use functional based view. search is as request.query_params.get("search")
@api_view(['GET'])
def search_contact(request):
    if request.method == 'GET':
        user = request.query_params.get("userid")
        search = request.query_params.get("search")
        # if user is not empty then search contact
        if user:
            # get user from User model
            user = User.objects.get(id=user)
            # search contact using Contact model
            contacts = Contact.objects.filter(Q(contact_name__icontains=search) | Q(contact_email__icontains=search) | Q(contact_phone_number__icontains=search), user=user)
            # serialize contacts using ContactSerializer
            serializer = ContactSerializer(contacts, many=True)
            # return response as contacts
            return Response(serializer.data, status=status.HTTP_200_OK)
        # else return response as no contacts found
        else:
            return Response({"message": "No contacts found"}, status=status.HTTP_400_BAD_REQUEST)
        
        


#user specific views


@api_view(['POST'])
def change_email(request):
    user_id = request.data.get("user_id")
    email = request.data.get("email")
    # check whether user exists or not
    if User.objects.filter(id=user_id).exists():
        user = User.objects.get(id=user_id)
        user.email = email
        user.save()
        return Response({"message": "Email changed successfully"}, status=status.HTTP_200_OK)
    else:
        return Response({"message": "User does not exist"}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def change_password(request):
    user_id = request.data.get("user_id")
    password = request.data.get("password")
    # check whether user exists or not
    if User.objects.filter(id=user_id).exists():
        user = User.objects.get(id=user_id)
        user.set_password(password)
        user.save()
        return Response({"message": "Password changed successfully"}, status=status.HTTP_200_OK)
    else:
        return Response({"message": "User does not exist"}, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['POST'])
def change_username(request):
    user_id = request.data.get("user_id")
    username = request.data.get("username")
    # check whether user exists or not
    if User.objects.filter(id=user_id).exists():
        user = User.objects.get(id=user_id)
        user.username = username
        user.save()
        return Response({"message": "Username changed successfully"}, status=status.HTTP_200_OK)
    else:
        return Response({"message": "User does not exist"}, status=status.HTTP_400_BAD_REQUEST)
 
@api_view(["POST"])
def create_account(request):
    username = request.data.get("username")
    password = request.data.get("password")
    company_name = request.data.get("company_name")
    email = request.data.get("email")
    # check whether user exists or not
    if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
        return Response({"message": "User already exists"}, status=status.HTTP_400_BAD_REQUEST)
    else:
        user=User.objects.create(username=username, password=make_password(password), email=email)
        Profile.objects.create(user=user, company_name=company_name)
#        user.save()
        return Response({"message": "Account created successfully"}, status=status.HTTP_201_CREATED)
    
# delete account
@api_view(["DELETE"])
def delete_account(request):
    user_id = request.data.get("user_id")
    # check whether user exists or not
    if User.objects.filter(id=user_id).exists():
        user = User.objects.get(id=user_id)
        user.delete()
        return Response({"message": "Account deleted successfully"}, status=status.HTTP_200_OK)
    else:
        return Response({"message": "User does not exist"}, status=status.HTTP_400_BAD_REQUEST)
    
    


class MyTokenObtainPair(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        # serializer = UserSerializerWithToken(self.user).data
        # for k,v in serializer.items():
        # data[k] = v
        data['user_id'] = self.user.id
        data['username'] = self.user.username
        data['email'] = self.user.email
        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPair

from .models import Note

# function view to add note params: userid, note.
@api_view(['POST'])
def add_note(request):
    if request.method == 'POST':
        user = request.data.get("userid")
        note = request.data.get("note")
        # if user and note is not empty then add note
        if user and note:
            # get user from User model
            user = User.objects.get(id=user)
            # create note using Note model
            note = Note.objects.create(user=user, note=note)
            # save note
            note.save()
            # return response as note added successfully
            return Response({"message": "Note added successfully"}, status=status.HTTP_201_CREATED)
        # else return response as note not added
        else:
            return Response({"message": "Note not added"}, status=status.HTTP_400_BAD_REQUEST)
        
# function view to get notes params: userid.
@api_view(['GET'])
def get_notes(request):
    if request.method == 'GET':
        user = request.query_params.get("userid")
        # if user is not empty then get note
        if user:
            # get user from User model
            user = User.objects.get(id=user)
            # get notes using Note model
            notes = Note.objects.filter(user=user)
            # serialize notes using NoteSerializer
            serializer = NoteSerializer(notes, many=True)
            # return response as notes
            return Response(serializer.data, status=status.HTTP_200_OK)
        # else return response as no notes found
        else:
            return Response({"message": "No notes found"}, status=status.HTTP_400_BAD_REQUEST)
        
# function view to delete note params: noteid.
@api_view(['DELETE'])
def delete_note(request):
    if request.method == 'DELETE':
        note = request.data.get("noteid")
        # if note is not empty then delete note
        if note:
            # get note from Note model
            note = Note.objects.get(id=note)
            # delete note
            note.delete()
            # return response as note deleted successfully
            return Response({"message": "Note deleted successfully"}, status=status.HTTP_200_OK)
        # else return response as note not deleted
        else:
            return Response({"message": "Note not deleted"}, status=status.HTTP_400_BAD_REQUEST)
        
# function view to update note params: noteid, note.
@api_view(['PUT'])
def update_note(request):
    if request.method == 'PUT':
        note = request.data.get("noteid")
        note_text = request.data.get("note")
        # if note and note_text is not empty then update note
        if note and note_text:
            # get note from Note model
            note = Note.objects.get(id=note)
            # update note_text
            note.note = note_text
            # save note
            note.save()
            # return response as note updated successfully
            return Response({"message": "Note updated successfully"}, status=status.HTTP_200_OK)
        # else return response as note not updated
        else:
            return Response({"message": "Note not updated"}, status=status.HTTP_400_BAD_REQUEST)
        
    
# end point for returning sms history
@api_view(['GET'])
def sms_history(request):
    if request.method == 'GET':
        # get the user id from the request
        user_id = request.query_params.get("userid")
        # if user id is not empty then get sms history
        if user_id:
            # get user from User model
            user = User.objects.get(id=user_id)
            # get sms history using Sms model
            sms = Sms.objects.filter(contact__user=user)
            # serialize sms using SmsSerializer
            serializer = SmsSerializer(sms, many=True)
            # return response as sms
            return Response(serializer.data, status=status.HTTP_200_OK)
        # else return response as no sms history found
        else:
            return Response({"message": "No sms history found"}, status=status.HTTP_400_BAD_REQUEST)
        
# end point for returning voicemail history
@api_view(['GET'])
def voicemail_history(request):
    if request.method == 'GET':
        # get the user id from the request
        user_id = request.query_params.get("userid")
        # if user id is not empty then get voicemail history
        if user_id:
            # get user from User model
            user = User.objects.get(id=user_id)
            # get voicemail history using VoiceMail model
            voicemail = VoiceMail.objects.filter(contact__user=user)
            # serialize voicemail using VoiceMailSerializer
            serializer = VoiceMailSerializer(voicemail, many=True)
            # return response as voicemail
            return Response(serializer.data, status=status.HTTP_200_OK)
        # else return response as no voicemail history found
        else:
            return Response({"message": "No voicemail history found"}, status=status.HTTP_400_BAD_REQUEST)

# end point for saving credit card details
# first check whether credit card details already exists or not if exists then update else create
@api_view(['POST'])
def credit_card(request):
    if request.method == 'POST':
        # get the user id from the request
        user_id = request.data.get("userid")
        # get the credit card number from the request
        credit_card_number = request.data.get("credit_card_number")
        # get the credit card expiry date from the request
        credit_card_expiry_date = request.data.get("credit_card_expiry_date")
        # get the credit card cvv from the request
        credit_card_cvv = request.data.get("credit_card_cvv")
        # if user id, credit card number, credit card expiry date, credit card cvv is not empty then save credit card details
        if user_id and credit_card_number and credit_card_expiry_date and credit_card_cvv:
            # get user from User model
            user = User.objects.get(id=user_id)
            # getting the profile
            profile = Profile.objects.get(user=user)
            # setting the is_credit_card_active to True
            profile.is_credit_card_active = True
            # save profile
            profile.save()
            # if credit card details already exists then update credit card details
            if CreditCard.objects.filter(user=user).exists():
                # get credit card details using CreditCard model
                credit_card = CreditCard.objects.get(user=user)
                # update credit card details
                credit_card.card_number = credit_card_number
                credit_card.expiration_date = credit_card_expiry_date
                credit_card.cvv = credit_card_cvv
                # save credit card details
                credit_card.save()
                # return response as credit card details updated successfully
                return Response({"message": "Credit card details updated successfully"}, status=status.HTTP_200_OK)
            # else create credit card details
            else:
                # create credit card using CreditCard model
                CreditCard.objects.create(user=user, card_number=credit_card_number, expiration_date=credit_card_expiry_date, cvv=credit_card_cvv)
                # return response as credit card details saved successfully 
                return Response({"message": "Credit card details saved successfully"}, status=status.HTTP_201_CREATED)
        # else return response as no credit card details found
        else:
            return Response({"message": "No credit card details found"}, status=status.HTTP_400_BAD_REQUEST)
        
        
# creating end point for updating credit card details
@api_view(['PUT'])
def update_credit_card(request):
    if request.method == 'PUT':
        # get the user id from the request
        user_id = request.data.get("userid")
        # get the credit card number from the request
        credit_card_number = request.data.get("credit_card_number")
        # get the credit card expiry date from the request
        credit_card_expiry_date = request.data.get("credit_card_expiry_date")
        # get the credit card cvv from the request
        credit_card_cvv = request.data.get("credit_card_cvv")
        # if user id, credit card number, credit card expiry date, credit card cvv is not empty then update credit card details
        if user_id and credit_card_number and credit_card_expiry_date and credit_card_cvv:
            # get user from User model
            user = User.objects.get(id=user_id)
            # getting the profile
            profile = Profile.objects.get(user=user)
            # setting the is_credit_card_active to True
            
            # create credit card using CreditCard model
            CreditCard.objects.create(user=user, credit_card_number=credit_card_number, expiry_date=credit_card_expiry_date, card_cvv=credit_card_cvv)
            # setting the is_credit_card_active to True
            profile.is_credit_card_active = True
            # save profile
            profile.save()
            # save credit card
@api_view(["POST"])
def send_sms(request):
    userid = request.data.get("userid")
    sms_text = request.data.get("sms_text")
    if userid:
        sms = Sms.objects.create(user=user, sms_text=sms_text)
        return Response({"message": "sms sent successfully"}, status=status.HTTP_200_OK)
    else:
        return Response({"message": "sms not sent"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def send_voice_mail(request):
    userid = request.data.get("userid")
    voice_mail_text = request.data.get("voice_mail_text")
    if userid:
        voice_mail = VoiceMail.objects.create(user=user, voice_mail_text=voice_mail_text)
        return Response({"message": "voice mail sent successfully"}, status=status.HTTP_200_OK)
    else:
        return Response({"message": "voice mail not sent"}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["GET"])
def get_user(request):
    userid = request.query_params.get("userid")
    user = User.objects.get(id=userid)
# getting user profile
    profile = Profile.objects.get(user=user)
    data= {"username": user.username, "email": user.email, "company_name": profile.company_name, "is_credit_card_active": profile.is_credit_card_active}
    return Response(data, status=status.HTTP_200_OK)



# end point for getting credit card details for a specific user using his userid
@api_view(['GET'])
def get_credit_card(request):
    if request.method == 'GET':
        # get the user id from the request
        user_id = request.query_params.get("userid")
        # if user id is not empty then get credit card details
        if user_id:
            # get user from User model
            user = User.objects.get(id=user_id)
            # get credit card details using CreditCard model
            credit_card = CreditCard.objects.get(user=user)
            # serialize credit card using CreditCardSerializer
            serializer = CreditCardSerializer(credit_card)
            # return response as credit card details
            return Response(serializer.data, status=status.HTTP_200_OK)
        # else return response as no credit card details found
        else:
            return Response({"message": "No credit card details found"}, status=status.HTTP_400_BAD_REQUEST)
        
# end point for deleting credit card details for a specific user using his userid
@api_view(['DELETE'])
def delete_credit_card(request):
    if request.method == 'DELETE':
        # get the user id from the request
        user_id = request.data.get("userid")
        # if user id is not empty then delete credit card details
        if user_id:
            # get user from User model
            user = User.objects.get(id=user_id)
            # get credit card details using CreditCard model
            credit_card = CreditCard.objects.get(user=user)
            # delete credit card details
            credit_card.delete()
            # automatically set is_credit_card_active to False
            profile = Profile.objects.get(user=user)
            profile.is_credit_card_active = False
            profile.save()
            # return response as credit card details deleted successfully
            return Response({"message": "Credit card details deleted successfully"}, status=status.HTTP_200_OK)
        # else return response as no credit card details found
        else:
            return Response({"message": "No credit card details found"}, status=status.HTTP_400_BAD_REQUEST)
        
# end point for updating credit card details for a specific user using his userid
@api_view(['PUT'])
def update_credit_card(request):
    if request.method == 'PUT':
        # get the user id from the request
        user_id = request.data.get("userid")
        # get the credit card number from the request
        credit_card_number = request.data.get("credit_card_number")
        # get the credit card expiry date from the request
        credit_card_expiry_date = request.data.get("credit_card_expiry_date")
        # get the credit card cvv from the request
        credit_card_cvv = request.data.get("credit_card_cvv")
        # if user id, credit card number, credit card expiry date, credit card cvv is not empty then update credit card details
        if user_id and credit_card_number and credit_card_expiry_date and credit_card_cvv:
            # get user from User model
            user = User.objects.get(id=user_id)
            # get credit card details using CreditCard model
            credit_card = CreditCard.objects.get(user=user)
            # update credit card details
            credit_card.credit_card_number = credit_card_number
            credit_card.credit_card_expiry_date = credit_card_expiry_date
            credit_card.credit_card_cvv = credit_card_cvv
            # save credit card details
            credit_card.save()
            # return response as credit card details updated successfully
            return Response({"message": "Credit card details updated successfully"}, status=status.HTTP_200_OK)
        # else return response as no credit card details found
        else:
            return Response({"message": "No credit card details found"}, status=status.HTTP_400_BAD_REQUEST)
