from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.core.mail import send_mail
from app.forms import *
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from rest_framework.viewsets import ViewSet
from app.serializers import *
from rest_framework.response import Response
from django.views.generic import CreateView

# Create your views here.

def Registration(request):
    d={'uso':UserForm()}
    if request.method=='POST':
        usd=UserForm(request.POST)
        if usd.is_valid():
            nusd=usd.save(commit=False)
            nusd.set_password(usd.cleaned_data['password'])
            nusd.save()
            return HttpResponse('DATA INSERTED SUCCESSFULLY')
        else:
            return HttpResponse('DATA IS INVALID')
        
    return render(request,'Registration.html',d)

def home(request):
    if request.session.get('username'):
        username=request.session.get('username')
        d={'username':username}
        return render(request,'home.html',d)
    return render(request,'home.html')

def user_login(request):
    if request.method=='POST':
        username=request.POST['un']
        password=request.POST['pw']
        AUO=authenticate(username=username, password=password)

        if AUO and AUO.is_active:
            login(request, AUO)
            request.session['username']=username
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponse('Invalid Username/Password')
    return render(request,'user_login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

# class Create_Organization(CreateView):
#     model = Organization
#     fields = '__all__' 
#     template_name = 'organization.html'
#     success_url = '/home/'

@login_required
def insert_data(request):
    d={'CFO':OrganizationForm()}
    if request.method == 'POST' and request.FILES:
        CO=OrganizationForm(request.POST,request.FILES)
        if CO.is_valid():
            CO.save()
            return HttpResponse("The data is inserted")
        else:
            return HttpResponse("The data is not valid")
    return render(request,'insert_data.html',d)




class OrganizationData(ViewSet):
    def list(self,request):
        ADO=Organization.objects.all()
        SJD=Organizationserializer(ADO,many=True)
        d={'data':SJD.data}
        return render(request,'list.html',d)

    def retrieve(self,request,pk):
        TO=Organization.objects.get(pk=pk)
        SDO=Organizationserializer(TO)
        return Response(SDO.data)


    def update(self,request,pk):
        SPO=Organization.objects.get(pk=pk)
        SPD=Organizationserializer(SPO,data=request.data)
        if SPD.is_valid():
            SPD.save()
            return Response({'Updated':'Product is updated'})
        else:
            return Response({'Failed':'Prodct is Not Updated'})
    
    def partial_update(self,request,pk):
        SPO=Organization.objects.get(pk=pk)
        SPD=Organizationserializer(SPO,data=request.data,partial=True)
        if SPD.is_valid():
            SPD.save()
            return Response({'Updated':'Product is updated'})
        else:
            return Response({'Failed':'Prodct is Not Updated'})
    def destroy(self,request,pk):
        Organization.objects.get(pk=pk).delete()
        return Response({'Deleted':'Product is deleted'})









