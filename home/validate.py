import secrets as ss
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from datetime import timedelta as td
from .models import  Profile, Code
from django.contrib.auth.models import User
from django.core.mail import send_mail
from datetime import datetime
import pytz


# specifying the time delta for the time interval

DELTA = td(hours=+1)

def generate_code():
    gen = ss.SystemRandom()
    code = gen.randint(1*1000, 5000)
    return code

@api_view(["POST"])
def generate(request):
    email = request.data.get("email")
    user =  User.objects.filter(email=email)
    if user:
        try:
            code = Code()
            code.user = user[0]
            code.unique_code = str(generate_code())
            code.expiring_date = DELTA + code.date_generated
            code.save()

            send_mail("ITSREADDY EMAIL ACCOUNT VERIFICATION CODE", f'Hello {user[0].username.capitalize()}, \rPlease use below code to verify your email address in the itsreaddy mobile app.\n\r Code: {code.unique_code} \r This code will expire in an hour time. \nThank you. \n\n\n Need help? Send an email to our support team at support@itsreaddy.com.', 'support@itsreaddy.com', [email], fail_silently=True)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({"status": "ok"})
    return Response({"status": "error"}, status=status.HTTP_404_NOT_FOUND)

@api_view(["POST"])
def reset(request):
    try:
        code_number = request.data.get("code")
        code = Code.objects.filter(unique_code=code_number)
        if code:
            code = code[0]

            if  datetime.now(tz=pytz.utc) < code.expiring_date:
                return Response({"status": "ok"})
            return Response({"status": "Code expired"}, status=status.HTTP_423_LOCKED)
        return Response({"status": "Invalid code"}	, status=status.HTTP_417_EXPECTATION_FAILED)
    except Exception as e:
        return Response({"error": str(e)})




@api_view(["POST"])
def validate_code(request):
    code_number = request.data.get("code")
    print(code_number)
    code = Code.objects.filter(unique_code=code_number)[0]
    print(code)

    if code:
        if datetime.now(tz=pytz.utc) < code.expiring_date:
            user = Profile.objects.get(user=code.user)
            print(user)
            user.is_validated=True
            user.save()
            send_mail('ITSREADDY Welcome message', f'Hello {user.user.username.capitalize()}, Your itsreaddy account has been verified\n\n\n Need help? Send an email to our support team at support@itsreaddy.com.', 'support@itsreaddy.com',  [user.user.email], fail_silently=True)
            return Response({"status": "ok"})
            code.delete()

        return Response({"status": "Code expired"}, status=status.HTTP_423_LOCKED)
    return Response({"status": "Invalid code"}	, status=status.HTTP_417_EXPECTATION_FAILED)
from .models import EmailCode
        
@api_view(["POST"])
def email_code(request):
    email = request.data.get("email")
    # checking if the email is in the database. so if the email already exists in the database, it will not be sent again. it will only be sent if the email is not in the database and there will response saying that the email already exists
    user = User.objects.filter(email=email)
    if user:
        return Response({"status": "Email already exists"}, status=status.HTTP_409_CONFLICT)
    try:
        code = EmailCode()
#        code.email = email
        code.unique_code = str(generate_code())
        code.expiring_date = DELTA + code.date_generated
        code.save()

        send_mail("ITSREADDY EMAIL ACCOUNT VERIFICATION CODE", f"Hello, Please use below code to verify your email address in the itsreaddy mobile app.\n\r Code: {code.unique_code} \r This code will expire in an hour time. \nThank you. \n\n\n Need help? Send an email to our support team at support@itsreaddy.com.", 'support@itsreaddy.com', [email], fail_silently=True)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response({"status": "ok"})


@api_view(["POST"])
def email_code_validate(request):
# checking if the code is in the emailcode table and if it is not expired
    code_number = request.data.get("code")
    code = EmailCode.objects.filter(unique_code=code_number)
    if code:
        code = code[0]
        if datetime.now(tz=pytz.utc) < code.expiring_date:
            code.delete()
            return Response({"status": "ok"})
        return Response({"status": "Code expired"}, status=status.HTTP_423_LOCKED)
    return Response({"status": "Invalid code"}	, status=status.HTTP_417_EXPECTATION_FAILED)