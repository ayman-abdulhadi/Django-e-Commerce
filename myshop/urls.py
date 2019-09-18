from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# from django.conf.urls.i18n import i18n_patterns
# from django.utils.translation import gettext_lazy as _


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls', namespace='cart')),
    path('orders/', include('orders.urls', namespace='ordera')),
    path('payment/', include('payment.urls', namespace='payment')),
    path('coupons/', include('coupons.urls', namespace='coupons')),
    # path('rosetta/', include('rosetta.urls')),
    path('', include('products.urls', namespace='products')),
    path('account/', include('account.urls', namespace='account')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
