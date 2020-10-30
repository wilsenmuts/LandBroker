from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth import  authenticate, login, logout
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import FileSerializer
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    if request.method == 'POST':
        fname_input = request.POST.get('fname', None)
        sname_input = request.POST.get('sname', None)
        uname_input = request.POST.get('uname', None)
        email_input = request.POST.get('mail', None)
        pswd_input = request.POST.get('pswd', None)
        photo = request.POST.get('photo', None)
        tel = request.POST.get('tel', None)
        user = User.objects.create_user(
            first_name = fname_input,
            last_name = sname_input,
            username = uname_input,
            email = email_input,
            password = pswd_input,
        )
        create_bio = profile(
            username= uname_input,
            photo = photo,
            tel_no = tel

        )
        create_bio.save()
        return redirect('/')
    context={}
    return render(request, 'landbroker/register.html', context)

def home(request):
    return HttpResponse('Welcome')

def login1(request):
    if request.method == 'POST':
        username_input = request.POST.get('uname', None)
        password_input = request.POST.get('pword', None)
        user = authenticate(username=username_input, password=password_input)
        if user is not None:
            request.session['username'] = username_input
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            reply ='Your details are invalid. Please,try again'
            context ={'reply':reply}
            return render(request, 'landbroker/index.html', context)
    context={}
    return render(request,'landbroker/index.html', context)

@login_required(login_url='/login/')
def submit_sale(request):
    if request.method == 'POST':
        if request.session.has_key('username'):
            myusername = User.objects.get(username = request.session.get('username'),)
            item2 = request.POST.get('tel_no')
            item3 = request.POST.get('nin')
            item4 = request.POST.get('reside')
            item5 = request.POST.get('price')
            item6 = request.POST.get('size')
            item7 = request.FILES['id_scan']
            item8 = request.FILES['title_scan']
            item9 = request.FILES['map_scan']
            item10 = request.POST.get('parts')
            item11 = request.POST.get('whole')
            item12 = request.POST.get('ownership')
            item13 = request.POST.get('desc')

            if item10:
                dec = True
            else:
                dec = False
            if item11:
                dec1 = True
            else:
                dec1 = False

            create_sale= sell(
                username = myusername,
                tel_no = item2,
                nin_no = item3,
                reside = item4,
                amount = item5,
                size = item6,
                id_card = item7,
                title_scan = item8,
                map_scan = item9,
                mode_whole = dec,
                mode_part = dec1,
                ownership = item12,
                description=item13

            )
            create_sale.save()
            context={'query':'Your request to show your land has been submitted. Landbroker Ug will now validate its authenticity'}
            return render(request, 'landbroker/sell.html', context)
        else:
            context={'query1':'We encountered an error, please try again...'}
            return render(request, 'landbroker/sell.html', context)
    context={}
    return render(request, 'landbroker/sell.html', context)

def show_buy(request):
    if request.method=='POST':
        search = request.POST.get('search')
        query = sell.objects.filter(reside__contains=search)
        paginator = Paginator(query, 16)
        page = request.GET.get('page')
        object_list= paginator.get_page(page)
        context ={'operation':object_list}
        return render(request, 'landbroker/buy.html', context)
    query = sell.objects.order_by('-date_box').filter(is_active=True)
    paginator = Paginator(query, 20)
    page = request.GET.get('page')
    object_list= paginator.get_page(page)
    context ={'operation':object_list}
    return render(request, 'landbroker/buy.html', context)

def delete_interest(request, id):
    interest = get_object_or_404(buy, id=id)
    interest.delete()
    user=request.user
    bids = buy.objects.filter(username=user).order_by('reside')
    user_details=get_object_or_404(profile, username=user)
    lands = sell.objects.filter(username=user).order_by('reside')
    context={'user':user_details, 'bids':bids, 'lands':lands, 'query':'The expression of interest was successfully deleted' }
    return render(request, 'landbroker/account.html', context)

def delete_land(request, id):
    interest = get_object_or_404(sell, id=id)
    interest.delete()
    user=request.user
    bids = buy.objects.filter(username=user).order_by('reside')
    user_details=get_object_or_404(profile, username=user)
    lands = sell.objects.filter(username=user).order_by('reside')
    context={'user':user_details, 'bids':bids, 'lands':lands, 'query':'The land was successfully deleted' }
    return render(request, 'landbroker/account.html', context)


@login_required(login_url='/login/')
def account(request):
    #user_details = profile.objects.filter(username=request.user)
    user=request.user
    bids = buy.objects.filter(username=user).order_by('reside')
    user_details=get_object_or_404(profile, username=user)
    lands = sell.objects.filter(username=user).order_by('reside')
    context={'user':user_details, 'bids':bids, 'lands':lands }
    return render(request, 'landbroker/account.html', context)

def logout1(request):
    logout(request)
    return HttpResponseRedirect('/')

def makeorder(request, article_id, article_reside):
    print(article_id)
    query = sell.objects.filter(id=article_id)
    print(article_reside)
    return redirect('/buy/')

def show_more(request, id):
    query = get_object_or_404(sell, id=id)
    context={'query': query}
    return render(request, 'landbroker/land.html', context )

@login_required(login_url='/login/')
def interest(request, id):
    target = get_object_or_404(sell, id=id)
    interested = buy(
        username = request.user,
        reside = target.reside,
        size = target.size,
        tel_no= target.tel_no,
        amount= target.amount,
        size_wanted = 000,
        status= False
    )
    interested.save()
    query = sell.objects.order_by('date_box').filter(is_active=True)
    alert='Your expression of interest has been received. Landbroker Ug will call you within 1-2 weeks to understand your interest better.'
    context ={'operation':query, 'alert':alert}
    return render(request, 'landbroker/buy.html', context)

class FileUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):

      file_serializer = FileSerializer(data=request.data['files'])

      if file_serializer.is_valid():
          file_serializer.save()
          return Response(file_serializer.data, status=status.HTTP_201_CREATED)
      else:
          return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)