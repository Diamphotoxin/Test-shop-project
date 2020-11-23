from django.contrib import admin
from django.urls import path, include
from catalog.views import ProductListView, ItemListView, OrderListView, ProductDetailView

from django.conf.urls.static import static, settings

import debug_toolbar


urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
    path('', ProductListView.as_view(), name='home'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='detail'),
    path('order/', OrderListView.as_view(), name='order'),
    path('cart/', ItemListView.as_view(), name='cart'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

