from django.urls import path
from .views import ProductListApi, ProductDetailApi


urlpatterns = [

    path('', ProductListApi.as_view(), name='product_list_api'),
    path('<int:id>/', ProductDetailApi.as_view(), name='product_detail_api'),
]