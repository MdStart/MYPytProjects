from MyTaskData.models import MyData
from pure_pagination import Paginator,PageNotAnInteger
from django.template.context import RequestContext
from django.conf import settings
from django.shortcuts import render_to_response,get_object_or_404


def myView(request):
    context = RequestContext(request)
    try:
        page = request.GET.get('page',settings.INTIAL_PAGE)
    except PageNotAnInteger:
            page = settings.INTIAL_PAGE
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





