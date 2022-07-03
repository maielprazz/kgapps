from django.urls import path
from .views import CategoryView, CategoryListView, ProductView, ProductListView, BannerView, BannerListView

urlpatterns = [
    path('category/', CategoryListView.as_view(), name="listcategory"),
    path('category/<str:pid>', CategoryView.as_view(), name="category"),
    
    path('product/', ProductListView.as_view(), name="productcategory"),
    path('product/<str:pid>', ProductView.as_view(), name="product"),
    
    path('banner/', BannerListView.as_view(), name="listbanner"),
    path('banner/<str:pid>', BannerView.as_view(), name="banner"),

]
