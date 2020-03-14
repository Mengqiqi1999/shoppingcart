from django.shortcuts import render

# Create your views here.
def product_list(request):
	products = Products.objects.all()
	return render(request, 'shop/product/list.html',{'products':products})

