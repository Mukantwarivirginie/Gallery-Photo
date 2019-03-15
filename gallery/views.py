from django.shortcuts import render,redirect
import datetime as dt
from django.shortcuts import render
from django.http  import HttpResponse



# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')
    # return HttpResponse('Welcome to the Gallery-Photo')

def gallery_of_day(request):
      date = dt.date.today()
      gallery = Images.objects.all()
      return render(request, 'all-gallery/today-gallery.html', {"date": date,"gallery":gallery})


def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-images/images.html", {"image":image})




def search_results(request):

    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Article.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-gallery/search.html',{"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-gallery/search.html',{"message":message})

