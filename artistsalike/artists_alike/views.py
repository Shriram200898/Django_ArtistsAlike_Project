from django.shortcuts import render, HttpResponseRedirect
from django.db.models import Q, Sum, Count
import os
import re
# Create your views here.
from django.shortcuts import render,redirect
from .models import Users
from .models import Category
from .models import Artists
from django.contrib import messages
from .forms import AddCategory
from .forms import AddOrder
from .models import Feedback
from .models import Order
from .models import Admin
from django.http import JsonResponse
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
import csv
from datetime import datetime
from datetime import date,timedelta
import xlwt
from django.template.loader import get_template
from xhtml2pdf import pisa

def Index(request):
    return render(request,'artistsalike/index1.html')


def Indexpage(request,Email):
    profile = Users.objects.get(Email=Email)
    return render(request,'artistsalike/index1.html',{'profile':profile})

def adminpage(request):
    today = date.today()
    today1 = today - timedelta(1)
    today2 = today - timedelta(2)
    today3 = today - timedelta(3)
    today4 = today - timedelta(4)
    today5 = today - timedelta(5)
    oc = Order.objects.filter(Order_Date=today).count()
    oc1 = Order.objects.filter(Order_Date=today1).count()
    oc2 = Order.objects.filter(Order_Date=today2).count()
    oc3 = Order.objects.filter(Order_Date=today3).count()
    oc4 = Order.objects.filter(Order_Date=today4).count()
    oc5 = Order.objects.filter(Order_Date=today5).count()
    count = Order.objects.all().count()
    complete = Order.objects.filter(Order_Status=True).count()
    pending = Order.objects.filter(Order_Status=False).count()
    context = {'count': count, 'complete': complete, 'pending': pending,'today':today,
               'today1':today1,'today2':today2,'today3':today3,'today4':today4,'today5':today5,
               'oc':oc,'oc1':oc1,'oc2':oc2,'oc3':oc3,'oc4':oc4,'oc5':oc5}
    return render(request,'artistsalike/admin.html',context)

def services(request,Email):
    profile = Users.objects.get(Email=Email)
    return render(request,'artistsalike/Services.html',{'profile':profile})

def contactus(request,Email):
    profile = Users.objects.get(Email=Email)
    return render(request,'artistsalike/contact.html',{'profile':profile})

def services1(request):
    return render(request,'artistsalike/Services.html')

def contactus1(request):
    return render(request,'artistsalike/contact.html')


def portfolio(request,Email):
    artist = Artists.objects.all()
    profile = Users.objects.get(Email=Email)
    return render(request, 'artistsalike/portfolio.html', {'arti': artist,'profile':profile})

def search_artists(request):
    if request.method == 'POST':
        Artist = request.POST['Search_Artists']
        lookup = (Q(Artist_Firstname__icontains=Artist) | Q(Artist_Lastname__icontains=Artist) | Q(Avg_Rating__icontains=Artist) | Q(Artist_Category__icontains=Artist))
        artist = Artists.objects.filter(lookup)
        return render(request, 'artistsalike/portfolio.html', {'arti': artist})

def portfolio1(request):
    artist = Artists.objects.all()
    return render(request, 'artistsalike/portfolio1.html', {'arti': artist})

def search_artists1(request):
    if request.method == 'POST':
        Artist = request.POST['Search_Artists']
        lookup = (Q(Artist_Firstname__icontains=Artist) | Q(Artist_Lastname__icontains=Artist) | Q(Avg_Rating__icontains=Artist) | Q(Artist_Category__icontains=Artist))
        artist = Artists.objects.filter(lookup)
        return render(request, 'artistsalike/portfolio1.html', {'arti': artist})

def Userreg(request):
    if request.method=='POST':
        Email = request.POST['Email']
        Username = request.POST['Username']
        Firstname = request.POST['Firstname']
        Lastname = request.POST['Lastname']
        Password = request.POST['Password']
        Cpassword = request.POST['Cpassword']
        DOB = request.POST['DOB']
        Gender = request.POST['Gender']
        Mobileno = request.POST['Mobileno']
        Address = request.POST['Address']
        reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
        pat = re.compile(reg)
        mat = re.search(pat, Password)
        if mat:
            Users(Email=Email, Username=Username, Firstname=Firstname, Lastname=Lastname, Password=Password,
                  Cpassword=Cpassword, DOB=DOB, Gender=Gender, Mobileno=Mobileno, Address=Address).save()
            messages.success(request, request.POST['Username'] + " Registered Successfully....!")
            return render(request, 'artistsalike/register.html')
        else:
            messages.success(request, " Please enter valid password....!")
            return render(request, 'artistsalike/register.html')

    else:
        return render(request,'artistsalike/register.html')

def Artistreg(request):
    cate = Category.objects.all()
    if request.method=='POST':
        Artist_Email = request.POST['Artist_Email']
        Artist_Firstname = request.POST['Artist_Firstname']
        Artist_Lastname = request.POST['Artist_Lastname']
        Artist_Category = request.POST['Artist_Category']
        Category_Price = request.POST['Category_Price']
        Artist_Password = request.POST['Artist_Password']
        Artist_Cpassword = request.POST['Artist_Cpassword']
        Artist_DOB = request.POST['Artist_DOB']
        Artist_Gender = request.POST['Artist_Gender']
        Artist_Mobileno = request.POST['Artist_Mobileno']
        Artist_Address = request.POST['Artist_Address']
        Artist_Photo = request.FILES['Artist_Photo']
        reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
        pat = re.compile(reg)
        mat = re.search(pat, Artist_Password)
        if mat:
            Artists(Artist_Email=Artist_Email, Artist_Firstname=Artist_Firstname, Artist_Lastname=Artist_Lastname,
                    Artist_Category=Artist_Category, Category_Price=Category_Price, Artist_Password=Artist_Password,
                    Artist_Cpassword=Artist_Cpassword, Artist_DOB=Artist_DOB, Artist_Gender=Artist_Gender,
                    Artist_Mobileno=Artist_Mobileno, Artist_Address=Artist_Address, Artist_Photo=Artist_Photo).save()
            messages.success(request, request.POST['Artist_Email'] + " Registered Successfully....!")
            return render(request, 'artistsalike/artist_register.html', {"ct": cate})
        else:
            messages.success(request," Please enter valid password....!")
            return render(request, 'artistsalike/artist_register.html', {"ct": cate})

    else:
        return render(request,'artistsalike/artist_register.html',{"ct":cate})


def userlogin(request):
    if request.method=="POST":
        try:
            Userdetails=Users.objects.get(Email=request.POST['Email'],Password=request.POST['Password'])
            print("Email=",Userdetails)
            request.session['Email']=Userdetails.Email
            return render(request,'artistsalike/index1.html',{'profile':Userdetails})
        except Users.DoesNotExist as e:
            messages.success(request,'Username / Password Invalid...!')
    return render(request,'artistsalike/login.html')

def userlogout(request):
    try:
        del request.session['Email']
    except:
        return HttpResponseRedirect('/Login')
    return render(request,'artistsalike/index1.html')


def artistslogin(request):
    if request.method=="POST":
        try:
            Artistdetails=Artists.objects.get(Artist_Email=request.POST['Artist_Email'],Artist_Password=request.POST['Artist_Password'])
            if Artistdetails.is_active == True:
                print("Artist_Email=", Artistdetails)
                request.session['Artist_Email'] = Artistdetails.Artist_Email
                count = Order.objects.filter(Artist_Email=Artistdetails.Artist_Email).count()
                complete = Order.objects.filter(Artist_Email=Artistdetails.Artist_Email, Order_Status=True).count()
                pending = Order.objects.filter(Artist_Email=Artistdetails.Artist_Email, Order_Status=False).count()
                context = {'profile':Artistdetails, 'count': count, 'complete': complete, 'pending': pending}
                return render(request,'artistsalike/artists.html',context)
            else:
                messages.success(request, 'Artist is Deactivated...!')
            return render(request, 'artistsalike/artist_login.html')
        except Artists.DoesNotExist as e:
            messages.success(request,'Email / Password Invalid...!')
    return render(request,'artistsalike/artist_login.html')

def artistlogout(request):
    try:
        del request.session['Artist_Email']
    except:
        return HttpResponseRedirect('/ArtistsLogin')
    return HttpResponseRedirect('/ArtistsLogin')


def adminlogin(request):
    today = date.today()
    today1 = today - timedelta(1)
    today2 = today - timedelta(2)
    today3 = today - timedelta(3)
    today4 = today - timedelta(4)
    today5 = today - timedelta(5)
    oc = Order.objects.filter(Order_Date=today).count()
    oc1 = Order.objects.filter(Order_Date=today1).count()
    oc2 = Order.objects.filter(Order_Date=today2).count()
    oc3 = Order.objects.filter(Order_Date=today3).count()
    oc4 = Order.objects.filter(Order_Date=today4).count()
    oc5 = Order.objects.filter(Order_Date=today5).count()
    count = Order.objects.all().count()
    complete = Order.objects.filter(Order_Status=True).count()
    pending = Order.objects.filter(Order_Status=False).count()
    context = {'today':today,'count': count, 'complete': complete, 'pending': pending,'today': today,
               'today1': today1, 'today2': today2, 'today3': today3, 'today4': today4, 'today5': today5,
               'oc': oc,'oc1': oc1, 'oc2': oc2,'oc3': oc3, 'oc4': oc4, 'oc5': oc5}
    if request.method=="POST":
        try:
            Admindetails=Admin.objects.get(Admin_Email=request.POST['Admin_Email'],Admin_Password=request.POST['Admin_Password'])
            print("Admin_Email=",Admindetails)
            request.session['Admin_Email']=Admindetails.Admin_Email
            return render(request,'artistsalike/admin.html',context)
        except Admin.DoesNotExist as e:
            messages.success(request,'Admin Email / Password Invalid...!')
    return render(request,'artistsalike/admin_login.html')

def adminlogout(request):
    try:
        del request.session['Admin_Email']
    except:
        return HttpResponseRedirect('/AdminLogin')
    return HttpResponseRedirect('/AdminLogin')


#This Function will Add Category and Display all Category
def add_show(request):
    if request.method == 'POST':
        fm = AddCategory(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['Category_Name']
            des = fm.cleaned_data['Category_Description']
            cat = Category(Category_Name=nm,Category_Description=des)
            cat.save()
            fm = AddCategory()
    else:
        fm = AddCategory()
    cate = Category.objects.all()
    return render(request, 'artistsalike/addandshow.html',{'form':fm,'ca':cate})


#This Function will Update Category
def update_category(request, Category_id):
    if request.method == 'POST':
        pi = Category.objects.get(pk=Category_id)
        fm = AddCategory(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi1 = Category.objects.get(pk=Category_id)
        fm = AddCategory(instance=pi1)
    return render(request, 'artistsalike/updatecategory.html', {'form':fm})



#This Function Delete Category
def delete_category(request, Category_id):
    if request.method == 'POST':
        pi = Category.objects.get(pk=Category_id)
        pi.delete()
        return HttpResponseRedirect('/Category')

# This function retreive artists details
def show_artists(request):
    arti = Artists.objects.all()
    return render(request, 'artistsalike/show_artists.html', {'ar': arti})


# This function deactivate artists details
def deactivate(request, Artist_id):
    artist = Artists.objects.get(pk=Artist_id)
    artist.is_active = False
    artist.save()
    messages.success(request, "Artist Account has been Successfully Deactivated...!")
    return redirect('show_artists')

# This function activate artists details
def activate(request, Artist_id):
    artist = Artists.objects.get(pk=Artist_id)
    artist.is_active = True
    artist.save()
    messages.success(request, "Artist Account has been Successfully Activated...!")
    return redirect('show_artists')

#This Function Delete Artist
def delete_artist(request, Artist_id):
    if request.method == 'POST':
        pi = Artists.objects.get(pk=Artist_id)
        pi.delete()
        return HttpResponseRedirect('/ShowArtists')


def feedback(request,Email,Artist_id,Order_id):
    cu = Users.objects.get(Email=Email)
    ar = Artists.objects.get(pk=Artist_id)
    Artist_Email = ar.Artist_Email
    if request.method=='POST':
        User_Name = request.POST['User_Name']
        User_Email = request.POST['User_Email']
        Description = request.POST['Description']
        Suggestions = request.POST['Suggestions']
        Rating = request.POST['Rating']

        Feedback(Order_id=Order_id,Artist_id=Artist_id,Artist_Email=Artist_Email,User_Name=User_Name,User_Email=User_Email,Description=Description,Suggestions=Suggestions,Rating=Rating).save()
        messages.success(request,"ThankYou for your valuable Feedback....!")
        return render(request, 'artistsalike/feedback.html',{'cu':cu,'ar':ar})
    else:
        return render(request, 'artistsalike/feedback.html',{'cu':cu,'ar':ar})



def order(request, Artist_id,Email):
    pi = Artists.objects.get(pk=Artist_id)
    Artist_Email = pi.Artist_Email
    cu = Users.objects.get(Email=Email)
    if request.method=='POST':
        User_Name = request.POST['User_Name']
        Artist_Name = request.POST['Artist_Name']
        O_Category = request.POST['O_Category']
        Price = request.POST['Price']
        Order_Description = request.POST['Order_Description']
        Mobile_No = request.POST['Mobile_No']
        User_Email = request.POST['User_Email']
        Upload_File = request.FILES['Upload_File']
        Order(User_Name=User_Name,Artist_id=Artist_id,Artist_Name=Artist_Name,Artist_Email=Artist_Email,O_Category=O_Category,Price=Price,Order_Description=Order_Description,Mobile_No=Mobile_No,User_Email=User_Email,Upload_File=Upload_File).save()
        messages.success(request,"Order Placed Successfully....!")
        return render(request, 'artistsalike/order.html',{'pi':pi,'cu':cu})
    else:
        return render(request,'artistsalike/order.html',{'pi':pi,'cu':cu})

def view_userorder(request,Email):
    order = Order.objects.filter(User_Email=Email)
    profile = Users.objects.get(Email=Email)
    return render(request,'artistsalike/view_userorder.html',{'order':order,'profile':profile})

def search_userorder(request,Email):
    if request.method == 'POST':
        profile = Users.objects.get(Email=Email)
        Order_Date = request.POST['Order_Date']
        order = Order.objects.filter(Order_Date=Order_Date,User_Email=Email)
    return render(request, 'artistsalike/view_userorder.html', {'order': order,'profile':profile})


def view_artistorder(request,Artist_Email):
    profile = Artists.objects.get(Artist_Email=Artist_Email)
    order = Order.objects.filter(Artist_Email=Artist_Email)
    return render(request,'artistsalike/view_artistorder.html',{'order': order,'profile':profile})

def view_complete(request,Artist_Email):
    profile = Artists.objects.get(Artist_Email=Artist_Email)
    order = Order.objects.filter(Artist_Email=Artist_Email,Order_Status=True)
    count = Order.objects.filter(Artist_Email=Artist_Email).count()
    complete = Order.objects.filter(Artist_Email=Artist_Email, Order_Status=True).count()
    pending = Order.objects.filter(Artist_Email=Artist_Email, Order_Status=False).count()
    context = {'order': order, 'profile': profile, 'count': count, 'complete': complete, 'pending': pending}
    return render(request,'artistsalike/artist_completeorder.html',context)

def view_pending(request,Artist_Email):
    profile = Artists.objects.get(Artist_Email=Artist_Email)
    order = Order.objects.filter(Artist_Email=Artist_Email,Order_Status=False)
    count = Order.objects.filter(Artist_Email=Artist_Email).count()
    complete = Order.objects.filter(Artist_Email=Artist_Email, Order_Status=True).count()
    pending = Order.objects.filter(Artist_Email=Artist_Email, Order_Status=False).count()
    context = {'order': order, 'profile': profile, 'count': count, 'complete': complete, 'pending': pending}
    return render(request,'artistsalike/artist_pendingorder.html',context)






def admin_allorder(request):
    order = Order.objects.all()
    count = Order.objects.all().count()
    complete = Order.objects.filter(Order_Status=True).count()
    pending = Order.objects.filter(Order_Status=False).count()
    context = {'order': order, 'count': count, 'complete': complete, 'pending': pending}
    return render(request,'artistsalike/admin_allorder.html',context)

def admin_complete(request):
    order = Order.objects.filter(Order_Status=True)
    count = Order.objects.all().count()
    complete = Order.objects.filter(Order_Status=True).count()
    pending = Order.objects.filter(Order_Status=False).count()
    context = {'order': order, 'count': count, 'complete': complete, 'pending': pending}
    return render(request,'artistsalike/admin_completeorder.html',context)

def admin_pending(request):
    order = Order.objects.filter(Order_Status=False)
    count = Order.objects.all().count()
    complete = Order.objects.filter(Order_Status=True).count()
    pending = Order.objects.filter(Order_Status=False).count()
    context = {'order': order, 'count': count, 'complete': complete, 'pending': pending}
    return render(request,'artistsalike/admin_pendingorder.html',context)





def search_artistorder(request,Artist_Email):
    if request.method == 'POST':
        profile = Artists.objects.get(Artist_Email=Artist_Email)
        Order_Date = request.POST['Order_Date']
        order = Order.objects.filter(Order_Date=Order_Date, Artist_Email=Artist_Email)
    return render(request, 'artistsalike/view_artistorder.html', {'order': order,'profile':profile})


def search_feedback(request,Artist_Email):
    if request.method == 'POST':
        profile = Artists.objects.get(Artist_Email=Artist_Email)
        Feedback_Date = request.POST['Feedback_Date']
        fd = Feedback.objects.filter(Feedback_Date=Feedback_Date,Artist_Email=Artist_Email)
    return render(request, 'artistsalike/view_feedback.html', {'fd':fd,'profile':profile})

def artists(request,Artist_Email):
    profile = Artists.objects.get(Artist_Email=Artist_Email)
    count = Order.objects.filter(Artist_Email=Artist_Email).count()
    complete = Order.objects.filter(Artist_Email=Artist_Email,Order_Status=True).count()
    pending = Order.objects.filter(Artist_Email=Artist_Email, Order_Status=False).count()
    context={'profile':profile,'count':count,'complete':complete,'pending':pending}
    return render(request,'artistsalike/artists.html',context)

def artists1(request):
    return render(request,'artistsalike/artists.html')


def cancel_order(request, Order_id,Email):
    if request.method == 'POST':
        profile = Users.objects.get(Email=Email)
        pi = Order.objects.get(pk=Order_id)
        pi.delete()
        order = Order.objects.filter(User_Email=Email)
        return render(request, 'artistsalike/view_userorder.html', {'order': order,'profile':profile})

def upload_order(request, Order_id,Artist_Email):
    if request.method == 'POST':
        profile = Artists.objects.get(Artist_Email=Artist_Email)
        pi = Order.objects.get(pk=Order_id)
        pi.Edited_File = request.FILES['Edited_File']
        pi.Order_Status = True
        pi.save()
        messages.success(request,"File Uploaded Successfully...!")
        order = Order.objects.filter(Artist_Email=Artist_Email)
        return render(request, 'artistsalike/view_artistorder.html', {'order': order,'profile':profile})
    else:
        messages.success(request, "File Not Uploaded....!")
        return render(request,'artistsalike/view_artistorder.html')

def view_feedback(request,Artist_Email):
    profile = Artists.objects.get(Artist_Email=Artist_Email)
    fd = Feedback.objects.filter(Artist_Email=Artist_Email)
    return render(request,'artistsalike/view_feedback.html',{'fd':fd,'profile':profile})

def view_order(request,Order_id):
    order = Order.objects.get(pk=Order_id)
    return render(request, 'artistsalike/view_order.html', {"or": order})

def update_order(request, Order_id,Email):
    pi = Order.objects.get(pk=Order_id)
    profile = Users.objects.get(Email=Email)
    if request.method == 'POST':
        pi.User_Name = request.POST['User_Name']
        pi.Artist_Name = request.POST['Artist_Name']
        pi.O_Category = request.POST['O_Category']
        pi.Price = request.POST['Price']
        pi.Order_Description = request.POST['Order_Description']
        pi.Mobile_No = request.POST['Mobile_No']
        pi.User_Email = request.POST['User_Email']
        pi.Upload_File = request.FILES['Upload_File']
        pi.save()
        messages.success(request, "Order Updated Successfully....!")
        return render(request, 'artistsalike/update_order.html', {'pi': pi,'profile':profile})
    else:
        return render(request, 'artistsalike/update_order.html', {'pi': pi,'profile':profile})


def view_orderartist(request,Order_id):
    order = Order.objects.get(pk=Order_id)
    return render(request, 'artistsalike/view_orderartist.html', {"or": order})


def avg_rating(request, Artist_id,Artist_Email):
    profile = Artists.objects.get(Artist_Email=Artist_Email)
    if request.method == 'POST':
        pi = Artists.objects.get(pk=Artist_id)
        pi.Avg_Rating = request.POST['Avg_Rating']
        pi.save()
        messages.success(request,"Rating Updated Successfully...!")
        fd = Feedback.objects.filter(Artist_Email=Artist_Email)
        return render(request, 'artistsalike/view_feedback.html', {'fd': fd,'profile':profile})
    else:
        messages.success(request, "Rating Not Updated....!")
        profile = Artists.objects.get(Artist_Email=Artist_Email)
        fd = Feedback.objects.filter(Artist_Email=Artist_Email)
        return render(request, 'artistsalike/view_feedback.html', {'fd': fd,'profile':profile})


def export_excel(request):
    x = str(datetime.now())
    if request.method == 'POST':
        From_Date = request.POST.get('From_Date')
        To_Date = request.POST.get('To_Date')

        response=HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition']='attachment; filename=Order'+x+'    FromDate-'+str(From_Date)+'   ToDate-'+str(To_Date)+'.xls'

        wb=xlwt.Workbook(encoding='utf-8')
        ws=wb.add_sheet('Order')
        row_num=0
        font_style = xlwt.XFStyle()
        font_style.font.bold=True
        columns = ['Order ID','Order Date','User Name','Artist Name','Order Category','Order Amount Paid']
        for i in range(len(columns)):
            ws.write(row_num, i,columns[i], font_style)

        font_style = xlwt.XFStyle()
        filterorder = Order.objects.filter(Order_Date__gte=From_Date,Order_Date__lte=To_Date,Order_Status=True).values_list('Order_id','Order_Date','User_Name','Artist_Name','O_Category','Price')

        for row in filterorder:
            row_num += 1

            for i in range(len(row)):
                ws.write(row_num, i, str(row[i]), font_style)
        wb.save(response)

        return response


def export_pdf(request):
    x = str(datetime.now())
    if request.method == 'POST':
        From_Date = request.POST.get('From_Date')
        To_Date = request.POST.get('To_Date')
        filterorder = Order.objects.raw('select Order_id,Order_Date,User_Name,Artist_Name,O_Category,Price from artists_alike_order where Order_Date between "' + str(From_Date) + '" and "' + str(To_Date)+ '" AND Order_Status=1')
        context = {'order':filterorder,'From_Date':From_Date,'To_Date':To_Date}
        template_path = 'artistsalike/pdf_output.html'
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'filename="Order'+x+'    FromDate-'+str(From_Date)+'   ToDate-'+str(To_Date)+'.pdf"'
        template = get_template(template_path)
        html = template.render(context)

        pisa_status = pisa.CreatePDF(html, dest=response)

        if pisa_status.err:
             return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response


def order_report(request):
    if request.method == 'POST':
        From_Date = request.POST.get('From_Date')
        To_Date = request.POST.get('To_Date')
        filterorder = Order.objects.raw('select Order_id,Order_Date,User_Name,Artist_Name,O_Category,Price,Order_Status from artists_alike_order where Order_Date between "'+From_Date+'" and "'+To_Date+'"')
        return render(request, 'artistsalike/report.html', {'order': filterorder})
    else:
        order = Order.objects.all()
    return render(request, 'artistsalike/report.html', {'order': order})

def view_pdf(request):
    if request.method == 'POST':
        From_Date = request.POST.get('From_Date2')
        To_Date = request.POST.get('To_Date2')
        filterorder = Order.objects.raw('select Order_id,Order_Date,User_Name,Artist_Name,O_Category,Price,Order_Status from artists_alike_order where Order_Date between "'+From_Date+'" and "'+To_Date+'"')
        return render(request, 'artistsalike/pdf_output.html', {'order': filterorder})
    else:
        order = Order.objects.all()
    return render(request, 'artistsalike/pdf_output', {'order': order})


def profile(request,Email):
    profile = Users.objects.get(Email=Email)
    return render(request,'artistsalike/profile.html',{'profile':profile})

def update_profile(request,User_id):
    up = Users.objects.get(User_id=User_id)
    if request.method == 'POST':
        up.Email = request.POST['Email']
        up.Username = request.POST['Username']
        up.Firstname = request.POST['Firstname']
        up.Lastname = request.POST['Lastname']
        up.DOB = request.POST['DOB']
        up.Gender = request.POST['Gender']
        up.Mobileno = request.POST['Mobileno']
        up.Address = request.POST['Address']
        up.Profile_Photo = request.FILES['Profile_Photo']
        up.save()
        messages.success(request,"Profile Updated Successfully....!")
        return render(request,'artistsalike/update_profile.html',{'up':up})
    else:
        return render(request,'artistsalike/update_profile.html',{'up':up})


def artist_profile(request,Artist_Email):
    profile = Artists.objects.get(Artist_Email=Artist_Email)
    return render(request,'artistsalike/artist_profile.html',{'profile':profile})

def update_artistprofile(request,Artist_id):
    up = Artists.objects.get(Artist_id=Artist_id)
    cate = Category.objects.all()
    if request.method=='POST':
        up.Artist_Email = request.POST['Artist_Email']
        up.Artist_Firstname = request.POST['Artist_Firstname']
        up.Artist_Lastname = request.POST['Artist_Lastname']
        up.Artist_Category = request.POST['Artist_Category']
        up.Category_Price = request.POST['Category_Price']
        up.Artist_DOB = request.POST['Artist_DOB']
        up.Artist_Gender = request.POST['Artist_Gender']
        up.Artist_Mobileno = request.POST['Artist_Mobileno']
        up.Artist_Address = request.POST['Artist_Address']
        up.Artist_Photo = request.FILES['Artist_Photo']

        up.save()
        messages.success(request,"Profile Updated Successfully....!")
        return render(request,'artistsalike/update_artistprofile.html',{"ct":cate,"up":up})
    else:
        return render(request,'artistsalike/update_artistprofile.html',{"ct":cate,"up":up})
