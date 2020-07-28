from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from app_goods.models import Product, Accessory
import datetime
from django.http import HttpResponseRedirect
from .models import Review

def reviews(request, product_id):
    if request.user.is_authenticated:
        if request.method=='POST':
            product=Product.objects.get(id=product_id)
            review=request.POST['content']   
            comment=Review(subject=product, review=review, user=request.user)
            comment.save()
            comments=Review.objects.filter(subject=product)
            context={
                'comments': comments
            }
            # return render(request, 'cart/product.html', context)
            product=Product.objects.get(id=product_id)
            accessories=Accessory.objects.filter(link=product_id)
            return HttpResponseRedirect(request.path_info)
        else:
            product=Product.objects.get(id=product_id)
            accessories=Accessory.objects.filter(link=product_id)
            comments=Review.objects.filter(subject=product)
            context={
                'comments': comments,
                'product': product,
                'accessories': accessories
            }
            return render(request, 'cart/product.html', context)
    return redirect ('login')
