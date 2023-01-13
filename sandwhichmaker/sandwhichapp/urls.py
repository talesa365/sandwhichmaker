
from django.urls import path
from sandwhichapp.views import SandwhichappView, IngredientsListView, SandwhichGeneratorView


urlpatterns=[
    path('', SandwhichappView.as_view(), name='sandwhich'),
    path('ingredients/<str:ingredient_type>', IngredientsListView.as_view(), name='ingredients_list'),
    path('random', SandwhichGeneratorView.as_view(), name='sandwhich_generator'),
]