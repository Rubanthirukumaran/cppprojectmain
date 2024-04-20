# food_items/views.py
from django.shortcuts import render
from .models import FoodItem
from numbers_properties_pkg import numbers_properties

def food_list(request):
    food_items = FoodItem.objects.all()
    

    # Convert queryset to a list of dictionaries
    food_items_data = [{'name': item.name, 'price': item.price} for item in food_items]

    # Calculate the total price using the imported function and dynamically fetched food items
    # total_price1 = calculate_total_price(food_items_data)
    
    
   
    # Calculate the total price using the imported function and dynamically fetched food items
    total_price = numbers_properties.FoodPriceCalculator.calculate_total_price(food_items_data)
    return render(request, 'food_items/food_list.html', {'food_items': food_items, 'total_price': total_price})
    





    
    