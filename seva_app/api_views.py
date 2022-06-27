from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics

from seva_app.forms import farmerform
from seva_app.models import market
from seva_app.serializers import MarketSerializer


@csrf_exempt
def farmer_reg(request):
    result_data = None
    if request.method == 'POST':
        form = farmerform(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.is_active = True
            form.is_farmer = True
            form.save()
            result_data = True
    try:
        if result_data:
            data = {'result': True}
        else:
            print(list(form.errors))
            error_data = form.errors
            error_dict = {}
            for i in list(form.errors):
                error_dict[i] = error_data[i][0]

            data = {
                'result': False,
                'errors': error_dict
            }
    except:
        data = {
            'result': False
        }
    return JsonResponse(data, safe=False)


@csrf_exempt
def login_view_api(request):
    print('hi')
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        print('hi', username)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_officer:
                type = 'officer'
            elif user.is_tstaff:
                type = 'technical staff'
            elif user.is_farmer:
                type = 'farmer'
                result = user.is_authenticated
    try:
        result = user.is_authenticated
        data = {
            'result': {
                'id': user.id,
                'name': user.username,
                'email': user.email,
                'type': type
            }
        }
    except:
        data = {
            'result': False
        }
    return JsonResponse(data, safe=False)


# market api

def market_ADD(request):
    result_data = None
    if request.method == 'POST':
        form = farmerform(request.POST)
        if form.is_valid():
            form.save()
            result_data = True
    try:
        if result_data:
            data = {'result': True}
        else:
            print(list(form.errors))
            error_data = form.errors
            error_dict = {}
            for i in list(form.errors):
                error_dict[i] = error_data[i][0]

            data = {
                'result': False,
                'errors': error_dict
            }
    except:
        data = {
            'result': False
        }
    return JsonResponse(data, safe=False)

class Market_api(generics.ListCreateAPIView):
    queryset = market.objects.all()
    serializer_class = MarketSerializer



#send application api

# @app.route('/uploader', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         f = request.files['file']
#         f.save(secure_filename(f.filename))
#         return 'file uploaded successfully'




