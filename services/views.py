from django.shortcuts import render
from services.models import trips
from services.models import locs
from django.contrib import messages
from django.shortcuts import redirect
from django.http import HttpResponseBadRequest

# Create your views here.

def location(request):
    return render(request,'location.html')





# def create_trip(request):
#       if request.method=="POST":
#         location_name=request.POST.get('location_name')
#         tour_dates=request.POST.get('tour_dates')
#         preferences=request.POST.get('preferences')
#         trip_user=trip.objects.create(location_name=location_name,tour_dates=tour_dates,preferences=preferences)
#         trip_user.save()
#         messages.success(request,'Trip Successfully Created')
#         return redirect('index')
#       else:
#          return render(request,'createT.html')
def create_trip(request):
     if request.method=="POST":
        location_name=request.POST.get('location_name')
        tour_dates=request.POST.get('tour_dates')
        preferences=request.POST.get('preferences')
        trip_user=trips.objects.create(location_name=location_name,tour_dates=tour_dates,preferences=preferences)
        trip_user.save()
        messages.success(request,'Trip Successfully Created')
     category=trips.objects.all().values()
    #  locate=locs.objects.all().values()
     return render(request,'createT.html',{ 'category':category})

def create_new(request,pkid):
    categ=trips.objects.get(id=pkid)
    category=trips.objects.filter(location_name=categ)
    return render(request,'browseT.html',{'category':category})

       
def browse_trips(request):
     return HttpResponseBadRequest("hey")


def search_view(request):
    searches= request.GET['find']
    if searches:
        search_results = trips.objects.filter(location_name__icontains=searches)
    else:
        search_results = []
    # category=trips.objects.all()
    # places=trips.objects.filter(location_name__icontains=searches)
    # res={'place':places,
    #      'category':category}
    return render(request,'search.html',{'search_results': search_results})
     
       
