from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView

# Create your views here.
class IndexView(TemplateView):
    template_name = "index.html"


class ShopView(TemplateView):
    template_name = "shop.html"



# def about(request):
#     return render(request, "about.html")




