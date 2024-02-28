from django.shortcuts import render, get_object_or_404, redirect
from . models import Cart, CartItem, Accessory, Product, Brand, Color, Operator
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def index(request):
    products_bestsellers = Product.objects.filter(bestsellers=True)
    sales = Product.objects.filter(sales=True)
    context = {
        # 'category': category_page,
        'products_bestsellers': products_bestsellers,
        'sales': sales,
        # 'brand_choices': brand_choices,
        # 'price_choices': price_choices,
        # 'battery_choices': battery_choices,
    }
    return render(request, 'index.html', context)

    # Products listing functions
# ======================================


def listing(request):
    # def smartphones (request, smartphones_slug=None ):
    # smartphones_page=None
    # products=None
    # if smartphones_page!=None:
        #category_page=get_object_or_404(Category, slug=category_slug)
    queryset_list = Product.objects.all()
    
    paginator = Paginator(queryset_list, 12)
    page = request.GET.page('page')
    queryset_list = paginator.get_page(page)
 
    # else:
    #     products=Product.objects.all().filter(available=True)
    context = {
        # 'category': category_page,
        'queryset_list': queryset_list,
        # 'brand_choices': brand_choices,
        # 'price_choices': price_choices,
        # 'battery_choices': battery_choices,
    }
    return render(request, 'cart/listing.html', context)


def listing_smartphone(request):
    queryset = Product.objects.filter(category=2)
    paginator = Paginator(queryset, 2)

    page_number = request.GET.get('page')
    queryset_list = paginator.get_page(page_number)

    context = {
        'queryset_list': queryset_list,
    }
    return render(request, 'cart/listing_smartphone.html', context)


def listing_smartwatch(request):
    queryset_list = Product.objects.filter(category=3)
    context = {
        'queryset_list': queryset_list,
    }
    return render(request, 'cart/listing_smartwatch.html', context)


def listing_sim(request):
    queryset_list = Product.objects.filter(category=4)
    context = {
        'queryset_list': queryset_list,
    }
    return render(request, 'cart/listing_sim.html', context)


def listing_lte(request):
    queryset_list = Product.objects.filter(category=5)
    context = {
        'queryset_list': queryset_list,
    }
    return render(request, 'cart/listing_lte.html', context)


def listing_accessory(request):
    queryset_list = Accessory.objects.all()
    context = {
        'queryset_list': queryset_list,
    }
    return render(request, 'cart/listing_accessory.html', context)

    # Single Product Card
# =================================================
# def productPage(request, category_slug, product_slug):


def productPage(request, product_id):
    try:
        #product=Product.objects.get(category__slug=category_slug, slug=product_slug)
        product = Product.objects.get(id=product_id)
        accessories = Accessory.objects.filter(link=product_id)
    except Exception as e:
        raise e
    context = {
        'product': product,
        'accessories': accessories,
    }
    template = 'cart/product.html'
    return render(request, template, context)

    # Single Accessory Page
# =======================================================


def accessoryPage(request, accs_id):
    try:
        #product=Product.objects.get(category__slug=category_slug, slug=product_slug)
        # product=Product.objects.get(id=product_id)
        accessory = Accessory.objects.get(id=accs_id)
    except Exception as e:
        raise e
    context = {
        'accessory': accessory,
    }
    template = 'cart/accessory/accessory.html'
    return render(request, template, context)

    # Search functions
# ============================================


def gen_search(request):
    if request.method == 'POST':
        keyword = request.POST['keyword']
        if keyword:  # if search line is not blank
            if Product.objects.filter(model_name__icontains=keyword).exists():
                queryset_list = Product.objects.filter(
                    model_name__icontains=keyword)
                context = {
                    'queryset_list': queryset_list
                }
                template = 'cart/listing.html'
                return render(request, template, context)
            else:
                if Brand.objects.filter(name__icontains=keyword).exists():
                    brand_name = Brand.objects.get(name__icontains=keyword)
                    queryset_list = Product.objects.filter(brand=brand_name)
                    context = {
                        'queryset_list': queryset_list
                    }
                    template = 'cart/listing.html'
                    return render(request, template, context)
                else:
                    return redirect('index')
        else:
            return redirect('index')


def search_smartphone(request):

    queryset_list = Product.objects.filter(category=2).order_by('price')
    if 'manufacture' in request.GET:
        manufacturers = request.GET.getlist('manufacture', None)
        if manufacturers:  # if checked
            brand_names = Brand.objects.filter(name__in=manufacturers)
            queryset_list = queryset_list.filter(brand__in=brand_names)

    #checking if 'price' name is in request.GET from radiobuttons (listing_smartphone.html)
    if 'price' in request.GET: 
        option=request.GET['price']
        if option == 'all':
            context = {
                 'queryset_list': queryset_list,
             }
        elif option == '3000-5000':
            queryset_list = queryset_list.filter(price__gte=3000, price__lte=5000)
        elif option == '5000-7000':
            queryset_list = queryset_list.filter(price__gte=5000, price__lte=7000)
        elif option == '7000-10000':
            queryset_list = queryset_list.filter(price__gte=7000, price__lte=10000)
        elif option == '10000-15000':
            queryset_list = queryset_list.filter(price__gte=10000, price__lte=15000)
        elif option == '15000-20000':
            queryset_list = queryset_list.filter(price__gte=15000, price__lte=20000)

    # if 'price' in request.GET:
    #     price = request.GET['price']
    #     if price:  # if checked
    #         queryset_list = queryset_list.filter(price__lte=price)

    # if 'price' in request.GET:
    #     price = request.GET.getlist('price', None)
    #     if price:  # if checked
    #         queryset_list = queryset_list.filter(price__gte=price[0], price__lte=price[-1])#range between first & last object in list

    if 'ram' in request.GET:  # if checked
        ram = request.GET.getlist('ram', None)
        if ram:  # if checked
            queryset_list = queryset_list.filter(ram__in=ram)

    if 'hdd' in request.GET:  # if checked
        hdd = request.GET.getlist('hdd', None)
        if hdd:  # if checked
            queryset_list = queryset_list.filter(hdd__in=hdd)

    if 'processor_core' in request.GET:  # if checked
        processor_core = request.GET.getlist('processor_core', None)
        if processor_core:  # if checked
            queryset_list = queryset_list.filter(processor_core__in=processor_core)

    if 'processor_frequency' in request.GET:  # if checked
        processor_frequency = request.GET.getlist('processor_frequency', None)
        if processor_frequency:  # if checked
            queryset_list = queryset_list.filter(processor_frequency__in=processor_frequency)

    if 'battery' in request.GET: 
        option=request.GET['battery']
        if option == 'all':
            context = {
                 'queryset_list': queryset_list,
             }
        elif option == 'lower 2000':
            queryset_list = queryset_list.filter(battery__lte=2000)
        elif option == '2000-3000':
            queryset_list = queryset_list.filter(price__gte=5000, price__lte=7000)
        elif option == '7000-10000':
            queryset_list = queryset_list.filter(price__gte=7000, price__lte=10000)
        elif option == '10000-15000':
            queryset_list = queryset_list.filter(price__gte=10000, price__lte=15000)
        elif option == '15000-20000':
            queryset_list = queryset_list.filter(price__gte=15000, price__lte=20000)


    context = {
        'queryset_list': queryset_list,
    }
    return render(request, 'cart/listing_smartphone.html', context)


def search_smartwatch(request):
    queryset_list = Product.objects.filter(category=3)
    if 'manufacture' in request.GET:
        manufacturers = request.GET.getlist('manufacture', None)
        if manufacturers:  # if checked
            brand_names = Brand.objects.filter(name__in=manufacturers)
            queryset_list = queryset_list.filter(brand__in=brand_names)

    if 'price' in request.GET:
        price = request.GET['price']
        if price:  # if checked
            queryset_list = queryset_list.filter(price__lte=price)
           
    if 'ram' in request.GET:  # if checked
        ram = request.GET['ram']
        if ram:
            queryset_list = queryset_list.filter(ram__lte=ram)
    context = {
        'queryset_list': queryset_list,
    }
    return render(request, 'cart/listing_smartwatch.html', context)


def search_accessory(request):
    queryset_list = Product.objects.filter(category=3)
    if 'manufacture' in request.GET:
        manufacturers = request.GET.getlist('manufacture', None)
        if manufacturers:  # if checked
            brand_names = Brand.objects.filter(name__in=manufacturers)
            queryset_list = queryset_list.filter(brand__in=brand_names)
    if 'price' in request.GET:
        price = request.GET['price']
        if price:  # if checked
            queryset_list = queryset_list.filter(price__lte=price)
    if 'ram' in request.GET:  # if checked
        ram = request.GET['ram']
        if ram:
            queryset_list = queryset_list.filter(ram__lte=ram)
    context = {
        'queryset_list': queryset_list,
    }
    return render(request, 'cart/listing_accessory.html', context)


def search_sim(request):
    queryset_list = Product.objects.filter(category=4)
    if 'operator' in request.GET:
        operators = request.GET.getlist('operator', None)
        if operators:  # if checked
            operator_names = Operator.objects.filter(name__in=operators)
            queryset_list = queryset_list.filter(operator__in=operator_names)
    context = {
        'queryset_list': queryset_list,
    }
    return render(request, 'cart/listing_sim.html', context)


def search_lte(request):
    queryset_list = Product.objects.filter(category=5)
    if 'manufacture' in request.GET:
        manufacturers = request.GET.getlist('manufacture', None)
        if manufacturers:  # if checked
            brand_names = Brand.objects.filter(name__in=manufacturers)
            queryset_list = queryset_list.filter(brand__in=brand_names)
    if 'price' in request.GET:
        price = request.GET['price']
        if price:  # if checked
            queryset_list = queryset_list.filter(price__lte=price)
    if 'operator' in request.GET:
        operators = request.GET.getlist('operator', None)
        if operators:  # if checked
            operator_names = Operator.objects.filter(name__in=operators)
            queryset_list = queryset_list.filter(operator__in=operator_names)
    context = {
        'queryset_list': queryset_list,
    }
    return render(request, 'cart/listing_lte.html', context)

    # Cart Functions
    # Creating a cart with unique session key
# =================================================

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

# =====================================================
    # Adding single product to cart
# =================================================

def add_cart(request, product_slug):
    # if product_id in request.GET:
    # if 'product_id' in request.path:
    if Accessory.objects.filter(slug=product_slug).exists():
        product = Accessory.objects.get(slug=product_slug)
        try:
            cart = Cart.objects.get(cart_id=_cart_id(request))
        except Cart.DoesNotExist:
            cart = Cart.objects.create(cart_id=_cart_id(request))
            cart.save()
        try:
            cart_item = CartItem.objects.get(product=product.name, cart=cart)
            # cart_item=CartItem.objects.get(Q(product=product) | Q(accessory=accessory), cart=cart)
            cart_item.quantity += 1
            cart_item.save()
        except CartItem.DoesNotExist:
            cart_item = CartItem.objects.create(
                product=product.name,
                brand=product.brand,
                cart=cart,
                quantity=1,
                price=product.price,
                image=product.image,
                slug=product_slug,
            )
            cart_item.save()
            context = {
                'cart_item': cart_item,
            }
        return redirect('cart_detail')

    else:
        product = Product.objects.get(slug=product_slug)
        try:
            cart = Cart.objects.get(cart_id=_cart_id(request))
        except Cart.DoesNotExist:
            cart = Cart.objects.create(cart_id=_cart_id(request))
            cart.save()
        try:
            cart_item = CartItem.objects.get(
                product=product.model_name, cart=cart)
            # cart_item=CartItem.objects.get(Q(product=product) | Q(accessory=accessory), cart=cart)
            cart_item.quantity += 1
            cart_item.save()
        except CartItem.DoesNotExist:
            cart_item = CartItem.objects.create(
                product=product.model_name,
                brand=product.brand.name,
                cart=cart,
                quantity=1,
                price=product.price,
                image=product.image,
                slug=product_slug
            )
            cart_item.save()
            context = {
                'cart_item': cart_item,
            }
        return redirect('cart_detail')
# ================================================


def cart_detail(request, total=0, counter=0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, active=True)

        new_total = 0.00
        for cart_item in cart_items:
            line_total = float(cart_item.price)*cart_item.quantity
            new_total += line_total
            counter += cart_item.quantity
    except ObjectDoesNotExist:
        new_total = 0.00
    return render(request, 'cart/cart.html', dict(cart_items=cart_items, new_total=new_total, counter=counter))


def remove_from_cart(request, product_slug):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    cart_item = CartItem.objects.get(cart=cart, slug=product_slug)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    context = {
        'cart_item': cart_item,
    }
    return redirect('cart_detail')


def delete_cartitem(request, product_slug):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    cart_item = CartItem.objects.get(cart=cart, slug=product_slug)
    cart_item.delete()
    context = {
        'cart_item': cart_item,
    }
    return redirect('cart_detail')

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
