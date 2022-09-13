from django.shortcuts import render

def index(request):
    context = {
        'title': 'Shop-Store'
    }
    return render(request, 'products\index.html', context)

def products(request):
    context = {
        'title': 'Каталог'
    }
    return render(request, 'products\products.html', context)

def test_context(request):
    context = {
        'title': 'Store',
        'header': 'Hi',
        'username': 'Erik Mikulaev',
        'products': [
            {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': 6090.00},
            {'name': 'Синяя куртка The North Face', 'price': 23725.00},
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': 3390.00}
        ],
        'products_in_promotion': [
            {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex', 'price': 13590.00}
        ],
    }
    return render(request, 'products/test-context.html', context)