from django.shortcuts import render, get_object_or_404, redirect
from . models import Cart, CartItem, Accessory, Product
from django.core.exceptions import ObjectDoesNotExist
from . choices import brand_choices, price_choices, battery_choices
from django.db.models import Q

def index(request):
    return render (request, 'index.html', {})

    # Products listing functions
# ======================================
def listing (request):
#def smartphones (request, smartphones_slug=None ):
    # smartphones_page=None
    # products=None
    # if smartphones_page!=None:
        #category_page=get_object_or_404(Category, slug=category_slug)
    products=Product.objects.all()
    # else:
    #     products=Product.objects.all().filter(available=True)
    context = {
        #'category': category_page,
        'products': products,
        # 'brand_choices': brand_choices,
        # 'price_choices': price_choices,
        # 'battery_choices': battery_choices,
        }
    return render (request, 'cart/listing.html',context )

def listing_smartphone (request):
    products=Product.objects.filter(category=1)
    context = {
        'products': products,
        }
    return render (request, 'cart/listing.html',context )

def listing_smartwatch (request):
    products=Product.objects.filter(category=3)
    context = {
        'products': products,
        }
    return render (request, 'cart/listing.html',context )

def listing_sim (request):
    products=Product.objects.filter(category=4)
    context = {
        'products': products,
        }
    return render (request, 'cart/listing.html',context )

def listing_lte (request):
    products=Product.objects.filter(category=5)
    context = {
        'products': products,
        }
    return render (request, 'cart/listing.html',context )

def listing_accessory (request):
    accessories=Accessory.objects.all()
    context = {
        'accessories': accessories,
        }
    return render (request, 'cart/listing.html',context )  

    # Single Product Card
# =================================================
#def productPage(request, category_slug, product_slug):
def productPage(request, product_id):
    try:
        #product=Product.objects.get(category__slug=category_slug, slug=product_slug)
        product=Product.objects.get(id=product_id)
        accessories=Accessory.objects.filter(link=product_id)
    except Exception as e:
        raise e
    context = {
        'product': product,
        'accessories': accessories
    }
    template='cart/product.html'
    return render (request, template, context)

    # Single Accessory Page
# =======================================================
def accessoryPage(request, accs_id):
    try:
        #product=Product.objects.get(category__slug=category_slug, slug=product_slug)
        # product=Product.objects.get(id=product_id)
        accessory=Accessory.objects.get(id=accs_id)
    except Exception as e:
        raise e
    context = {
        'accessory': accessory,
    }
    template='cart/accessory/accessory.html'
    return render (request, template, context)

    # Search functions
# ============================================
def search(request):
    queryset_list=Product.objects.order_by('-created')

    if 'manufacture' in request.GET:
        manufacturers=request.GET.getlist('manufacture', None)
        if manufacturers:
            queryset_list=queryset_list.filter(brand__in=manufacturers)

    if 'model' in request.GET:
         model=request.GET['model']
         if model:
           queryset_list=queryset_list.filter(name__icontains=model) 
           #queryset_list=queryset_list.filter(name__iexact=model)

    if 'brand' in request.GET:
         brand=request.GET['brand']
         if brand:
           queryset_list=queryset_list.filter(brand__iexact=brand) 
    if 'price' in request.GET:
         price=request.GET['price']
         if price:
           queryset_list=queryset_list.filter(price__lte=price) #lower than
    if 'battery' in request.GET:
         battery=request.GET['battery']
         if battery:
            queryset_list=queryset_list.filter(battery__gte=battery) #greater then
        #    queryset_list=queryset_list.filter(battery__range=battery) #greater then
    context= {
        'brand_choices': brand_choices,
        'price_choices': price_choices,
        'battery_choices': battery_choices,
        'products': queryset_list,
        'values': request.GET #leaves the input data in the form
    }
    return render (request, 'cart/search.html', context)


    # Cart Functions
# =================================================
def _cart_id(request):
    cart= request.session.session_key
    if not cart:
       cart=request.session.create()
    return cart

# =====================================================
    # Adding single product to cart
# =================================================
def add_cart(request, product_slug):
    # if product_id in request.GET:
    # if 'product_id' in request.path:
    if Accessory.objects.filter(slug=product_slug).exists():
        product=Accessory.objects.get(slug=product_slug)
        try:
            cart=Cart.objects.get(cart_id =_cart_id(request))
        except Cart.DoesNotExist:
            cart = Cart.objects.create(cart_id =_cart_id(request))
            cart.save()
        try:
            cart_item=CartItem.objects.get(product=product.name, cart=cart)
            # cart_item=CartItem.objects.get(Q(product=product) | Q(accessory=accessory), cart=cart)
            cart_item.quantity+=1
            cart_item.save()
        except CartItem.DoesNotExist:
            cart_item=CartItem.objects.create(
                product = product.name,
                cart=cart,
                quantity = 1,
                price=product.price,
                image=product.image,
                slug=product_slug,
                )
            cart_item.save()
            context={
                'cart_item':cart_item,
            }
        return redirect ('cart_detail')

    else:
        product=Product.objects.get(slug=product_slug)
        try:
            cart=Cart.objects.get(cart_id =_cart_id(request))
        except Cart.DoesNotExist:
            cart = Cart.objects.create(cart_id =_cart_id(request))
            cart.save()
        try:
            cart_item=CartItem.objects.get(product=product.model_name, cart=cart)
            # cart_item=CartItem.objects.get(Q(product=product) | Q(accessory=accessory), cart=cart)
            cart_item.quantity+=1
            cart_item.save()
        except CartItem.DoesNotExist:
            cart_item=CartItem.objects.create(
                product = product.model_name,
                cart=cart,
                quantity = 1,
                price=product.price,
                image=product.image,
                slug=product_slug
                )
            cart_item.save()
            context={
                'cart_item':cart_item,
            }
        return redirect ('cart_detail')
# ================================================
def cart_detail(request, total=0, counter=0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, active=True)
       
        new_total=0.00
        for cart_item in cart_items:
            line_total = float(cart_item.price)*cart_item.quantity
            new_total+=line_total
            counter +=cart_item.quantity
    except ObjectDoesNotExist:
        new_total=0.00   
    return render (request, 'cart/cart.html', dict(cart_items = cart_items, new_total=new_total, counter=counter))

# ============================================================
    # Adding Accessories to Cart
# =================================================
# def add_cart_accs(request, accessory_slug):
#     accessory=Accessory.objects.get(slug=accessory_slug)
#     try:
#         cart=Cart.objects.get(cart_id =_cart_id(request))
#     except Cart.DoesNotExist:
#         cart = Cart.objects.create(cart_id =_cart_id(request))
#         cart.save()
    # try:
    #     cart_item=CartItem.objects.get(accessory=accessory, cart=cart)
    #     # cart_item=CartItem.objects.get(Q(product=product) | Q(accessory=accessory), cart=cart)
    #     cart_item.quantity+=1
    #     cart_item.save()
    # except CartItem.DoesNotExist:
    # cart_item=CartItem.objects.create(
    #         product = accessory,
    #         cart=cart,
    #         quantity = 1
    #     )
    # cart_item.save() 
    # return redirect ('cart_detail')



