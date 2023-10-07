from django.http import JsonResponse

# api view makes it possible to handle the view, authentication and permission classes can override 
# the default classes ins settings.py REST_FRAMEWORK
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .forms import SignupForm

@api_view(['GET'])
# use default authentication classes
def me(request):
    return JsonResponse({
        'id': request.user.id,
        'email': request.user.email,
        'name': request.user.name,
    })

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def signup(request):
    data = request.data
    print(data)
    message = 'success'

    form = SignupForm({
        'email': data.get('email'),
        'name': data.get('name'),
        'password1': data.get('password1'),
        'password2': data.get('password2'),
    })

    if form.is_valid():
        form.save()
    # send verification email
    else:
        message = 'error'

    # this will return the error message if the form is not valid
    return JsonResponse({'message': message})