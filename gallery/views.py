from django.shortcuts import render,redirect
import datetime as dt
from django.shortcuts import render
from django.http  import HttpResponse
from .models import Image




# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')
  

def gallery_of_day(request):
      date = dt.date.today()
      photos = Image.objects.all()
      return render(request, 'all-gallery/todays-gallery.html', {"date": date,"photos":photos})


def image(request,image_id):
    try:
        photo = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-gallery/image.html", {"image":photo})




def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        name = request.GET.get("category")
        searched_categories = Image.search_by_category(name)
        message = f"{name}"

        return render(request, 'all-gallery/search.html',{"message":message,"categories": searched_categories})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-gallery/search.html',{"message":message})

