from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from account.models import *
from account.forms import CustomerApplicationForm
from django.contrib import messages
from django.http import JsonResponse
# Create your views here.

# @login_required(login_url='login')
def home(request):
    context={}
    return render(request,'home/home.html',context)
def newpage(request):
    gender_choices = CustomrerApplication.GENDER_CHOICES 
    district_choices = District.objects.all()
    account_type_choices = CustomrerApplication.ACCOUNT_TYPE_CHOICES
    material_choices = Material.objects.all()

    context = {
        'gender_choices': gender_choices,
        'district_choices': district_choices,
        'account_type_choices': account_type_choices,
        'material_choices': material_choices
    }

    if request.method == "POST":
        form = CustomerApplicationForm(request.POST)
        if form.is_valid():
            customer_application = form.save(commit=False)
            customer_application.user = request.user
            customer_application.save()

            messages.success(request, 'Application Accepted. Thank you!')
            return redirect('home') 
    else:
        form = CustomerApplicationForm()

    context['form'] = form

    selected_district_id = request.GET.get('district')
    if selected_district_id:
        selected_district = District.objects.get(id=selected_district_id)
        branch_choices = Branch.objects.filter(district=selected_district)
        context['branch_choices'] = branch_choices

    return render(request, 'home/newpage.html', context)




def userprofile(request):
    context={}
    
    if request.user.is_authenticated:
      
        try:
            customer_application=CustomrerApplication.objects.get(user_id=request.user)
            print(customer_application,'heleeeeeeeeeeeeeeee')
        except CustomrerApplication.DoesNotExist:
            customer_application=None
        
        context={'customerapplication':customer_application}
       
    return render(request,'home/userprofile.html',context)


def get_branches(request):
    district_id=request.GET.get('district_id')
    branches=Branch.objects.filter(district_id=district_id).values('id','name')
    return JsonResponse({'branches':list(branches)})