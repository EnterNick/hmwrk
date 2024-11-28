from django.urls import path
from .views import IndexView, GoodsView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('recipes/', GoodsView.as_view(), name='recipes'),
    path('recipes/<int:id>/', GoodsView.as_view(), name='recipe'),
]
