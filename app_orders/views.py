from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from .forms import OrderCreateForm
from app_goods.models import Cart, CartItem
from .models import Order, OrderItem
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
#from .tasks import order_created
import datetime
from . utils import render_to_pdf

def _cart_id(request):
    cart= request.session.session_key
    return cart

def delivery(request):
    return render(request, 'orders/delivery.html')

def choice(request):
    if 'delivery' in request.GET: #checking if 'delivery name is in request.GET from radiobuttons (delivery.html)
        option=request.GET['delivery']
        if option=='address':
            return redirect ('order_create')
        else:
            return redirect ('anonymous_pick_up')

def anonymous_pick_up(request):
    return render(request, 'orders/payment.html')  

def payment_choice(request):
    cart=Cart.objects.get(cart_id =_cart_id(request))
    cart_items=CartItem.objects.all().filter(cart=cart)
    order=Order.objects.create()
    for item in cart_items:
        # if item.product:
        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity,
            price=item.price
            )
        #clear the cart
        order_items=OrderItem.objects.filter(order=order)
    if 'payment' in request.GET: #checking if 'payment name is in request.GET from radiobuttons (payment.html)
        option=request.GET['payment']
        if option=='credit':
            return redirect ('payment_stripe')
            # context ={
            #     'cart_items': cart_items
            # }
            # return render(request,'orders/create_order.html', context )
        else:
            context = {
                'order_items': order_items,
                'order': order,
            }
        return render(request, 'invoice.html', context)  

def payment_stripe (request):
    return render (request, 'orders/payment_stripe.html')

def order_create(request):
    if request.user.is_authenticated:
        cart=Cart.objects.get(cart_id =_cart_id(request))#choosing the current cart
        cart_items=CartItem.objects.all().filter(cart=cart)#choosing all the cart_items in 
        if request.method == 'POST':
            first_name =request.POST['first_name']
            last_name =request.POST['last_name']
            email =request.POST['email']
            phone =request.POST['phone']
            postal_code =request.POST['code']
            region =request.POST['region']
            city =request.POST['city']
            street =request.POST['street']
            building =request.POST['building']
            appartment =request.POST['appartment']
            # created =request.POST['created']
            # updated =request.POST['updated']
            # paid =request.POST['paid']

            order=Order(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                postal_code=postal_code,
                region=region,
                city=city,
                street=street,
                building=building,
                appartment=appartment
                # created=created,
                # updated=updated,
                # paid=paid,
            )
            order.save()
        # if request.method == 'POST':
        #     form = OrderCreateForm(request.POST)
        #     if form.is_valid():
        #         order = form.save()

            for item in cart_items:
                if item.product:
                    OrderItem.objects.create(
                                order=order,
                                product=item.product,
                                quantity=item.quantity
                    #           #product= item['product'],
                    #           #quantity=item['quantity']
                                #price=item['price'],
                                            )
                # clear the cart
                # cart.clear()
                # launch asynchronous task
                # order_created.delay(order.id)
                else:
                    OrderItem.objects.create(
                        order=order,
                        product= item.accessory,
                        quantity=item.quantity
                    #   #product= item['product'],
                    #   #quantity=item['quantity']
                        #price=item['price'],
                    )
                # clear the cart
                # cart.clear()
                # launch asynchronous task
                # order_created.delay(order.id)
            context ={
                    'order':order,
                    'cart_items': cart_items
                }
            return render(request, 'orders/payment.html', context)   
    else:
        cart=Cart.objects.get(cart_id =_cart_id(request))
        cart_items=CartItem.objects.all().filter(cart=cart)
        if request.method=="POST":
            first_name =request.POST['first_name']
            last_name =request.POST['last_name']
            email =request.POST['email']
            phone =request.POST['phone']
            postal_code =request.POST['code']
            region =request.POST['region']
            city =request.POST['city']
            street =request.POST['street']
            building =request.POST['building']
            appartment =request.POST['appartment']
            # created =request.POST['created']
            # updated =request.POST['updated']
            # paid =request.POST['paid']

            order=Order(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                postal_code=postal_code,
                region=region,
                city=city,
                street=street,
                building=building,
                appartment=appartment
                # created=created,
                # updated=updated,
                # paid=paid,
            )
            order.save()
            for item in cart_items:
                if item.product:
                    OrderItem.objects.create(
                        order=order,
                        product=item.product,
                        quantity=item.quantity
                    #   #product= item['product'],
                    #   #quantity=item['quantity']
                        #price=item['price'],
                    )
                # clear the cart
                # cart.clear()
                # launch asynchronous task
                # order_created.delay(order.id)
            return render(request, 'orders/payment.html') 
        else:
            form = OrderCreateForm()
            return render (request, 'orders/create_order.html')

def orders_history(request):#for authenticated users
    if request.user.is_authenticated: #checking if the user is authenticated
        email=str(request.user.email)
        order_details=Order.objects.filter(email=email)#filtering the users' orders by email
        user= User.objects.get(email=email)
        context= {
            'order_details': order_details,
            'user': user
        }
        return render(request, 'orders/orders_history.html', context)
    else:
        return redirect('login')

# def pdf_page(request):
#     return render (request, 'pdf_page.html')

# class DownloadPDF(View):
#     def get(self, request, *args, **kwargs):
#         pdf=render_to_pdf('pdf_page.html', data)
#         response=HttpResponse(pdf, content_type='pdf')
#         filename-"Invoice_%s.pdf" %("12341231")
#         content="attachment; filename='%s'" %(filename)
#         response['Content-Disposition']=content
#         return response

class GeneratePDF(View):
    # def get(self, request, *args, **kwargs):
    def get(self, request, pk):
        invoice=OrderItem.objects.filter(order=pk)
        data = {
            'order': pk,
            'invoice': invoice
        }
        pdf = render_to_pdf('pdf_invoice.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

class DownloadPDF(View):
    # def get(self, request, *args, **kwargs):
    def get(self, request, pk):
        invoice=OrderItem.objects.filter(order=pk)
        template = get_template('pdf_invoice.html')
        context = {
            'order': pk,
            'invoice': invoice
        }
        pdf = render_to_pdf('pdf_invoice.html', context)
        response=HttpResponse(pdf, content_type='application/pdf')
        filename = "Invoice_%s.pdf" %(pk)
        content = "attachment; filename='%s'" %(filename)
        response['Content-Disposition'] = content
        return response

