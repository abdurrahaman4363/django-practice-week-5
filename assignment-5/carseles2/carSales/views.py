from django.shortcuts import render
from brand.models import Brand
from car.models import Car


def home(request, brand_slug=None):
    car = Car.objects.all()
    if brand_slug is not None:
        brand = Brand.objects.get(slug=brand_slug)
        car = Car.objects.filter(brand=brand)
    brand = Brand.objects.all()
    return render(request, "home.html", {"car": car, "brand": brand})
