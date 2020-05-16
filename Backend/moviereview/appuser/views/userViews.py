from rest_framework.decorators import api_view
from rest_framework.response import Response
from passlib.hash import pbkdf2_sha256
from ..models import User


@api_view(['POST']) 
def signupuser(request):

    if request.method == 'POST':
        try:
            user = User.objects.get(email=request.data["email"])

        except User.DoesNotExist:
            encryptpassword=pbkdf2_sha256.using(rounds=1000,salt_size=20).hash(request.data["password"])
            newUser = User(email=request.data["email"], nickname=request.data["nickname"], password=encryptpassword, state=True, typeuser=False)
            newUser.save()
            return Response({
                "message": "USER CREATED", 
                "user": {
                        "email": request.data["email"],
                        "nickname": request.data["nickname"]
                    },
                "isLogged": True,
                "signupCorrect": True})

        return Response({
                "message": "USER ALREADY EXISTS", 
                "user": {},
                "isLogged": False,
                "signupCorrect": False})


@api_view(['POST'])
def signinuser(request):

    if request.method == 'POST':
        try:
            user = User.objects.get(email=request.data["email"])

        except User.DoesNotExist:
            return Response({
                "message": "USER DOESNT EXISTS", 
                "user": {},
                "isLogged": False,
                "signinCorrect": False})

        if pbkdf2_sha256.verify(request.data["password"], user.password):
            return Response({
                    "message": "USER FOUND", 
                    "user": {
                        "email": user.email,
                        "nickname": user.nickname
                    },
                    "isLogged": True,
                    "signinCorrect": True})

        else: 
            return Response({
                    "message": "PASSWORD INCORRECT", 
                    "user": {},
                    "isLogged": False,
                    "signinCorrect": False})


@api_view(['PUT'])
def updatepassword(request):

   if request.method == 'PUT':

        try:
            user = User.objects.get(email=request.data["email"])

        except User.DoesNotExist:
            return Response({
                "message": "USER DOESNT EXISTS",
                "passwordUpdate": False})
        
        
        if  pbkdf2_sha256.verify(request.data["password"], user.password):
            newhashpass=pbkdf2_sha256.using(rounds=1000,salt_size=20).hash(request.data["newpassword"])
            user.password=newhashpass
            user.save()
            return Response({
                "message": "USER UPDATE",
                "passwordUpdate": True})

        else:
            return Response({
                "message": "PASSWORD INCORRECT",
                "passwordUpdate": False})

