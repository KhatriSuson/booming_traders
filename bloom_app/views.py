from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView, View, DetailView
import datetime


from bloom_app.models import Slider
from django.utils import timezone
from django.contrib import messages


# Create your views here.
class IndexView(ListView):
    model = Slider
    template_name = "blooming/index.html"
    context_object_name = "sliders"

    def get_queryset(self):
        queryset = Slider.objects.all()
        return queryset


class ShopView(View):
    template_name = "blooming/shop.html"

    def get(self, request):
        return render(request, self.template_name)


class DetailView(View):
    template_name = "blooming/detail.html"

    def get(self, request):
        return render(request, self.template_name)


from bloom_app.forms import ContactForm


class ContactView(View):
    template_name = "blooming/contact.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your query was successfully submitted.")
            return redirect("contact")
        else:
            messages.error(request, "Cannot submit your query. Something went wrong.")
            return render(
                request,
                self.template_name,
                {"form": form},
            )


class CheckoutView(View):
    template_name = "blooming/checkout.html"

    def get(self, request):
        return render(request, self.tempalte_name)


class CartView(View):
    template_name = "blooming/cart.html"

    def get(self, request):
        return render(request, self.template_name)


# def about(request):
#     return render(request, "about.html")
