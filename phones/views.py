from django.shortcuts import render
from phones.models import Phone


def show_catalog(request):
    sort_param = request.GET.get('sort')
    template = 'catalog.html'
    if sort_param == 'name':
        phones = list(Phone.objects.order_by('name'))
    if sort_param == 'min_price':
        phones = list(Phone.objects.order_by('price'))
    if sort_param == 'max_price':
        phones = list(Phone.objects.order_by('price'))
        phones = reversed(phones)
    context = {
        'phones': phones
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {
        'name': phone.name,
        'image': phone.image,
        'price': phone.price,
        'lte_exists': phone.lte_exists,
        'release_date': phone.release_date
    }

    return render(request, template, context)

def base(request):
    template = 'base.html'
    context = {}
    return render(request, template, context)
