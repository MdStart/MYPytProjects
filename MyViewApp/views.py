from MyTaskData.models import MyData
from pure_pagination import Paginator,PageNotAnInteger
from django.template.context import RequestContext
from django.conf import settings
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse, reverse_lazy
from MyTaskData.models import MyData
from .utility import myUtiLity
#This is the view used for filtering
def myView(request):
    context = RequestContext(request)
    #pagination Logic
    page=myUtiLity.my_page(request)
    if request.method == 'GET':
       mydata=MyData.objects.all()
       p = Paginator(mydata,settings.PER_PAGE_NUMBER, request=request)
       myList = p.page(page)
       return render_to_response(
           'myview/myView.html', {'myData':myList,'all_records':1}, context)
    elif request.method == 'POST':
       search_text = str(request.POST.get('search_text','')).strip()
       mydata=MyData.objects.filter(device_name__icontains=search_text)
       print(mydata)
       return render_to_response(
           'myview/myView.html',{'myData':mydata,'all_records':0}, context)

#This is the admin Panel
def myPanel(request):
    context = RequestContext(request)
    page=myUtiLity.my_page(request)
    if request.method == 'GET':
       my_data=MyData.objects.all()
       myList=[]
       #This Part will Put recrently added article above at top of list
       for field in my_data[::-1]:
           myList.append(field)
       p = Paginator(myList,settings.PER_PAGE_NUMBER, request=request)
       myList = p.page(page)
       return render_to_response(
           'myview/myPanel.html', {'myData':myList,'all_records':1}, context)

#This is the delete me function
def deleteme(request,id):
    mydata=MyData.objects.get(pk=id)
    mydata.delete()
    return HttpResponseRedirect(reverse('myPanel',args=[]))

#This is the edit me function
def editme(request,id):
    context=RequestContext(request)
    if request.method=='POST':
       device_name=request.POST.get("device_name","")
       magnification=myUtiLity.form_field_value(request,"magnification")
       range=myUtiLity.form_field_value(request,"range")
       field_of_view=myUtiLity.form_field_value(request,"field_of_view")
       mydata=MyData.objects.get(pk=id)

       MyData(pk=mydata.pk,device_name=device_name,magnification=magnification,range=range,field_of_view=field_of_view).save()

       return HttpResponseRedirect(reverse('myPanel',args=[]))
    elif request.method=='GET':
       try:
           mydata=MyData.objects.get(pk=id)
       except:
           return HttpResponse('Sorrry Id Not Available')
       return render_to_response(
           'myview/editData.html',{"mydata":mydata}, context)

#This is add Data method
def addme(request):
    context=RequestContext(request)
    if request.method=='POST':
       device_name=request.POST.get("device_name","")
       magnification=myUtiLity.form_field_value(request,"magnification")
       range=myUtiLity.form_field_value(request,"range")
       field_of_view=myUtiLity.form_field_value(request,"field_of_view")

       MyData(device_name=device_name,magnification=magnification,range=range,field_of_view=field_of_view).save()
       return HttpResponseRedirect(reverse('myPanel',args=[]))
    elif request.method=='GET':
       return render_to_response(
           'myview/addData.html',{}, context)



