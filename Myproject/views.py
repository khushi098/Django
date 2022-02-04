




from django.http.response import HttpResponse
from django.shortcuts import render

def myHomeViewFunction(request):
    return render(request,'index.html')
#The role of any function is to return something
    #return HttpResponse('Hello From HOme route')
    #render(request,template_name,context=None,content_type=None,status=None,using=None)

def myAboutUsViewFunction(request):
    return render(request,'about-us.html')


def contact(request):
    nm = request.GET.get('name')
    mi = request.GET.get('mission')
    #render(request, template_name, context=None, content_type=None, status=None, using=None)
    context = {
        "name": nm,
        "ourmission": mi,
    } # dictionary of
    return render(request, 'contact.html',context)

def category(request,category=None):
    x = request.GET.get('name')
    return HttpResponse(f'Hello {x} from Category  {category}')


def cart(request):
    return render(request, 'shopping-cart.html')


def detail(request):
    return render(request, 'single-product.html')


def login(request):
    return render(request, 'login.html')


def home(request):
    return render(request, 'index-2.html')

def landing(request):
    return render(request, 'landing.html')

def checkout(request):
    return render(request, 'checkout.html')

def four04(request):
    return render(request, '404.html')


def blogp(request):
    return render(request, 'blog-post.html')


def blog1(request):
    return render(request, 'blog-v01.html')


def blog2(request):
    return render(request, 'blog-v02.html')

def blog3(request):
    return render(request, 'blog-v03.html')

def category1(request):
    return render(request, 'category-grid-3-cols.html')

def category2(request):
    return render(request, 'category-grid-6-cols.html')


def category3(request):
    return render(request, 'category-grid-left-sidebar.html')

def category4(request):
    return render(request, 'category-grid-right-sidebar.html')

def category5(request):
    return render(request, 'category-grid.html')

def category6(request):
    return render(request, 'category-list-left-sidebar.html')

def category7(request):
    return render(request, 'category-list-right-sidebar.html')

def category8(request):
    return render(request, 'category-list.html')




def home1(request):
    return render(request, 'home-01.html')

def home2(request):
    return render(request, 'home-02.html')

def home3(request):
    return render(request, 'home-03-green.html')

def home4l(request):
    return render(request, 'home-04-light.html')

def home4(request):
    return render(request, 'home-04.html')

def home5(request):
    return render(request, 'home-05.html')

def detail1(request):
    return render(request, 'single-product-external.html')

def detail2(request):
    return render(request, 'single-product-grouped.html')

def detail3(request):
    return render(request, 'single-product-onsale.html')

def detail4(request):
    return render(request, 'single-product-simple.html')




