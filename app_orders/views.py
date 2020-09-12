from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
# from app_accounts.views import login
from .forms import OrderCreateForm
from app_goods.models import Cart, CartItem
from .models import Order, OrderItem
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
#from .tasks import order_created
import datetime
from .utils import render_to_pdf
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from pr_dir import settings
from django.template import Context
import xhtml2pdf.pisa as pisa
from io import BytesIO
from django.core.mail import send_mail, EmailMessage
from pr_dir.settings import EMAIL_HOST_USER

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def order_create(request):
    # if request.user.is_authenticated:
    order = Order.objects.create()
    order.save()
    cart = Cart.objects.get(cart_id=_cart_id(request))
    cart_items = CartItem.objects.all().filter(cart=cart)
    for item in cart_items:
        # if item.product:
        OrderItem.objects.create(
            order=order,
            product=item.product,
            brand=item.brand,
            quantity=item.quantity,
            price=item.price
        )
        # else:
        #     OrderItem.objects.create(
        #         order=order,
        #         brand=item.brand,
        #         product=item.accessory,
        #         quantity=item.quantity,
        #         price=item.price
        #     )

      # clear the cart
            # cart.clear()
            # launch asynchronous task
            # order_created.delay(order.id)
    context = {
            'order': order,
        }
    return render(request, 'orders/select_delivery_type.html', context)

def delivery_choice(request, order_id):
    if 'delivery' in request.GET: #checking if 'delivery name is in request.GET from radiobuttons (delivery.html)
        option=request.GET['delivery']
        if option == 'address':
            context = {
                 'order_id': order_id,
             }
            return render(request, 'orders/edit_order.html', context)
        elif option == 'office':
            order=Order.objects.get(id=order_id)
            context = {
                  'order': order,
              }
            return render (request, 'orders/select_customer_type.html', context)
        else:
            order = Order.objects.get(id=order_id)
            context = {
              'order': order,
            }
            return render(request, 'orders/select_logistics_type.html', context)
            
def edit_order(request, order_id):
    if request.method == "POST":
        order = get_object_or_404(Order, id=order_id)
        order.postal_code =request.POST['code']
        order.region =request.POST['region']
        order.city =request.POST['city']
        order.street =request.POST['street']
        order.building =request.POST['building']
        order.appartment = request.POST['appartment']
        order.save()
        context = {
            'order': order
        }
        return render (request, 'orders/select_customer_type.html', context )
    else:
        return render(request, 'edit_oder.html')
        
def customer_choice(request, order_id):
     # checking if 'delivery name is in request.GET from radiobuttons (delivery.html)
     if 'customer' in request.GET:
        option = request.GET['customer']
        if option == 'person':
            context = {
                'order_id': order_id,
            }
            return render(request, 'orders/edit_customer_name.html', context)
        else:
            if request.user.is_authenticated:
                order = Order.objects.get(id=order_id)
                context = {
                    'order': order
                }
                return render(request, 'orders/select_payment_type.html', context)
            else:
                return redirect('login')
     

def edit_customer_name (request, order_id):
    if request.method == "POST":
        order = get_object_or_404(Order, id=order_id)
        order.first_name =request.POST['first_name']
        order.last_name =request.POST['last_name']
        order.email =request.POST['email']
        order.phone = request.POST['phone']
        order.save()
        context = {
            'order': order
        }
        return render (request, 'orders/select_payment_type.html', context )
    else:
        return render(request, 'edit_oder.html')

def anonymous_pick_up(request):
    return render(request, 'orders/payment.html')

def payment_choice(request, order_id):
    # checking if 'payment name is in request.GET from radiobuttons (payment.html)
    if 'payment' in request.GET:
        option = request.GET['payment']
        if option == 'credit':
            context ={
                'order_id': order_id
            }
            return render(request, 'orders/payment_stripe.html', context)
        elif option == 'cash':
            order_items = OrderItem.objects.all().filter(order=order_id)
            order = Order.objects.get(id=order_id)
            context = {
                'order_items': order_items,
                'order': order
            }
            return render(request, 'inoice.html', context) 
        else:
            order_items = OrderItem.objects.all().filter(order=order_id)
            order=Order.objects.get(id=order_id)
            context = {
                'order_items': order_items,
                'order': order
            }
        return render(request, 'invoice.html', context)


def logistics_choice(request, order_id):
     # checking if 'delivery name is in request.GET from radiobuttons (delivery.html)
     if 'logistics' in request.GET:
        option = request.GET['logistics']
        if option == 'SDEK':
            order=Order.objects.get(id=order_id)
            context = {
                'order': order,
            }
            return render(request, 'orders/sdek_map.html', context)
        else:
            order = Order.objects.get(id=order_id)
            context = {
                'order': order,
            }
            return render(request, 'orders/post_map.html', context)

def orders_history(request):  # for authenticated users
    if request.user.is_authenticated:  # checking if the user is authenticated
        email = str(request.user.email)
        # filtering the users' orders by email
        order_details = Order.objects.filter(email=email)
        user = User.objects.get(email=email)
        context = {
            'order_details': order_details,
            'user': user
        }
        return render(request, 'orders/orders_history.html', context)
    else:
        return redirect('login')

class GeneratePDF(View):
    # def get(self, request, *args, **kwargs):
    def get(self, request, pk):
        invoice = OrderItem.objects.filter(order=pk)
        order = Order.objects.get(id=pk)
        new_total = 0.00
        counter = 0
        for item in invoice:
            line_total = float(item.price)*item.quantity
            new_total += line_total
            counter += item.quantity
        data = {
            'order': order,
            'invoice': invoice,
            'new_total': new_total
        }
        pdf = render_to_pdf('pdf_invoice.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

class DownloadPDF(View):
    # def get(self, request, *args, **kwargs):
    def get(self, request, pk):
        invoice = OrderItem.objects.filter(order=pk)
        order = Order.objects.get(id=pk)
        new_total = 0.00
        counter = 0
        for item in invoice:
            line_total = float(item.price)*item.quantity
            new_total += line_total
            counter += item.quantity
        data = {
            'order': order,
            'invoice': invoice,
            'new_total': new_total
        }
        pdf = render_to_pdf('pdf_invoice.html', data)
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Invoice_%s.pdf" % (pk)
        content = "attachment; filename='%s'" % (filename)
        response['Content-Disposition'] = content
        return response


# def email(request):
#     send_mail(
#         'Hello from DjangoDev',
#         'Here goes email text',
#         '79200711112@yandex.ru',
#         ['Sergei_Vinokurov@rambler.ru'],
#         fail_silently=False
#     )
#     return render(request, 'email/email.html')

def email(request):
    message=request.POST.get('message', '')
    subject=request.POST.get('subject', '')
    mail_id = request.POST.get('email', '')
    email = EmailMessage(subject, message, EMAIL_HOST_USER, [mail_id])
    email.content_subtype = 'html'
    email.send()
    return render(request, 'email/email.html')

def send_stored_file(request, pk):
    message = request.POST.get('message', '')
    subject=request.POST.get('subject', '')
    mail_id = request.POST.get('email', '')
    email = EmailMessage(subject, message, EMAIL_HOST_USER, [mail_id])
    email.content_subtype = 'html'
    file = open("README.md", "r")
    email.attach("README.md", file.read(), 'text/plain')
    email.send()
    return render(request, 'email/email.html')
  
def send_file(request):
    message = request.POST.get('message', '')
    subject=request.POST.get('subject', '')
    mail_id = request.POST.get('email', '')
    email = EmailMessage(subject, message, EMAIL_HOST_USER, [mail_id])
    email.content_subtype = 'html'
    file = request.FILES['file']
    email.attach(file.name, file.read(), file.content_type)
    email.send()
    return render(request, 'email/email.html')


        # clear the cart
        # cart.clear()
        
        
    # else:
    #     cart=Cart.objects.get(cart_id =_cart_id(request))
    #     cart_items=CartItem.objects.all().filter(cart=cart)
    #     if request.method=="POST":
    #         first_name =request.POST['first_name']
    #         last_name =request.POST['last_name']
    #         email =request.POST['email']
    #         phone =request.POST['phone']
    #         postal_code =request.POST['code']
    #         region =request.POST['region']
    #         city =request.POST['city']
    #         street =request.POST['street']
    #         building =request.POST['building']
    #         appartment =request.POST['appartment']
    #         # created =request.POST['created']
    #         # updated =request.POST['updated']
    #         # paid =request.POST['paid']

    #         order=Order(
    #             first_name=first_name,
    #             last_name=last_name,
    #             email=email,
    #             phone=phone,
    #             postal_code=postal_code,
    #             region=region,
    #             city=city,
    #             street=street,
    #             building=building,
    #             appartment=appartment
    #             # created=created,
    #             # updated=updated,
    #             # paid=paid,
    #         )
    #         order.save()
    #         for item in cart_items:
    #             if item.product:
    #                 OrderItem.objects.create(
    #                     order=order,
    #                     product=item.product,
    #                     quantity=item.quantity
    #                 #   #product= item['product'],
    #                 #   #quantity=item['quantity']
    #                     #price=item['price'],
    #                 )
    #             # clear the cart
    #             # cart.clear()
    #             # launch asynchronous task
    #             # order_created.delay(order.id)
    #         return render(request, 'orders/payment.html') 
    # # else:
    #     order = Order.objects.create()
    #     order.save()
    #     cart = Cart.objects.get(cart_id=_cart_id(request))
    #     cart_items = CartItem.objects.all().filter(cart=cart)
    #     for item in cart_items:
    #         if item.product:
    #             OrderItem.objects.create(
    #                 order=order,
    #                 product=item.product,
    #                 quantity=item.quantity
    #             )
    #         # clear the cart
    #         # cart.clear()
    #         # launch asynchronous task
    #         # order_created.delay(order.id)
    #         else:
    #             OrderItem.objects.create(
    #                 order=order,
    #                 product=item.accessory,
    #                 quantity=item.quantity
    #                 #   #product= item['product'],
    #                 #   #quantity=item['quantity']
    #                 #price=item['price'],
    #             )


    #     # clear the cart
    #     # cart.clear()
    #     return render (request, 'orders/create_order.html')
