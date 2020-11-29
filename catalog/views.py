from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View
from .models import Product, Order, Item, Category, Attribute, AttributeValue
from .forms import OrderForm
from shop.settings import RECIPIENTS_EMAIL, DEFAULT_FROM_EMAIL
from django.core.mail import send_mail
from django.contrib import messages


class ProductListView(ListView):  # home page
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['attributes_values'] = {attr: AttributeValue.objects.filter(attribute=attr).distinct('value')
                                        for attr in Attribute.objects.all()}

        return context

    def get_queryset(self):
        category = self.request.GET.getlist('category')
        attribute_value = self.request.GET.getlist('value')
        queryset = Product.objects.all()
        if category:
            queryset = queryset.filter(category__id__in=category)
        if attribute_value:
            queryset = queryset.filter(attributevalue__value__in=attribute_value)
        return queryset


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'

    def post(self, request, pk, **kwargs):
        self.object = self.get_object()

        if 'items' not in request.session:
            request.session['items'] = []
            request.session.save()

        if pk not in request.session['items']:
            request.session['items'].append(pk)
            request.session.save()

        context = self.get_context_data(**kwargs)
        context['item_list'] = request.session['items']
        return render(request, self.template_name, context=context)


class ItemListView(View):
    template_name = 'catalog/item_list.html'

    def get(self, request, *args, **kwargs):
        order_product_list = Product.objects.filter(pk__in=request.session.get('items', []))

        list_of_price = [prod.price for prod in order_product_list]
        total_price = sum(list_of_price)

        context = {'products': order_product_list,
                   'total_price': total_price}

        return render(request, self.template_name, context=context)


class OrderListView(ListView):
    model = Order
    template_name = 'catalog/order_list.html'

    def post(self, request):
        form = OrderForm(request.POST)
        if form.is_valid():
            customer_name = form.cleaned_data['customer_name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']

            products_in_items = Product.objects.filter(pk__in=request.session['items'])  # get product by id
            items_object_list = [Item.objects.create(product=prod)
                                 for prod in products_in_items]  # add to db Item object

            order = Order.objects.create()

            for item in items_object_list:
                order.items.add(item)  # add items to order

            order.customer_name = customer_name
            order.email = email
            order.phone = phone
            order.save()

            del request.session['items']  # delete session data

            messages.success(request, 'Success! Thanks for your order')

            send_mail(f'Order from {email}', f'{customer_name} made an order №{order.id}, phone: {phone}',
                      DEFAULT_FROM_EMAIL, RECIPIENTS_EMAIL)

            return redirect('home')



