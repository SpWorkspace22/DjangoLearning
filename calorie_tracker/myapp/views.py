from django.shortcuts import render, redirect   

# Create your views here.
from .models import Food, Consume

def index(request):
    if request.method == "POST":
        food_consume = request.POST['food_consumed']
        consume = Food.objects.get(name=food_consume)
        user = request.user
        consume = Consume(user=user,food_consumed=consume)
        consume.save()

        foods = Food.objects.all()
    else:
        foods = Food.objects.all()
    
    consume_food = Consume.objects.filter(user=request.user)
    print(foods)

    return render(request,'index.html',{'foods':foods, 'consume_food':consume_food})

def delete_consume(request, id):
    consume_food = Consume.objects.get(id=id)
    if request.method=='POST':
        consume_food.delete()
        return redirect('/')
    else:
        return render(request, 'delete.html')




