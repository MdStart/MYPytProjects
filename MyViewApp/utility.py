from pure_pagination import EmptyPage,PageNotAnInteger,Paginator
from django.conf import settings

class myUtiLity:

      #Will calculate page value for pagination
      def my_page(request):
         try:
            page = request.GET.get('page',settings.INTIAL_PAGE)
         except PageNotAnInteger:
            page = settings.INTIAL_PAGE
         
         return page

      #Will form field  value for Optrional Fields
      def form_field_value(request,tfield):

          tfield=request.POST.get(tfield,"NA")
          if len(tfield.strip()) <= 0:
             tfield='NA'
          return tfield