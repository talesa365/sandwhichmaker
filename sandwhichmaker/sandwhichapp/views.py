from django.shortcuts import render
from django.http import Http404
from django.views import View
import random

ingredients={
    'meats': ['corned beef', 'pastrami', 'honey turkey', 'pepper steak', 'veggie burger'],
    'cheeses': ['american', 'swiss', 'provolone', 'cheddar', 'mozzarella'],
    'toppings': ['lettuce', 'totmato', 'onions', 'peppers', 'pickles']
}

# Create your views here.
class SandwhichappView(View):
    def get(self, request):
        if request.method=='GET':
            return render(
                request=request,
                template_name='sandwhich.html',
                context={'ingredients': ingredients.keys()}
            )

class IngredientsListView(View):
    def get(self, request, ingredient_type):
        if request.method=='GET':
            if ingredient_type not in ingredients:
                raise Http404(f'No such ingredient: {ingredient_type}')
            
            return render(
                request=request,
                template_name='ingredients_list.html',
                context={ 'ingredients': ingredients[ingredient_type],
                            'ingredient_type': ingredient_type}
            )

class SandwhichGeneratorView(View):
    def get(self, request):
        if request.method=='GET':
            selected_meat=random.choice(ingredients['meats'])
            selected_cheese=random.choice(ingredients['cheeses'])
            selected_toppings=random.choice(ingredients['toppings'])

            sandwhich=f'{selected_meat} & {selected_cheese} with {selected_toppings}'
            return render(request, 'sandwhich_generator.html', context={'sandwhich': sandwhich})
            