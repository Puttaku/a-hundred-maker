from django.shortcuts import render
import random
def index(request):
    numberOne = 0
    numberTwo = 0
    numberOne = random.randint(0, 200)
    numberTwo = random.randint(0, 200)
    case = random.randint(1, 4)
    if case == 1:
        numberOne = random.randint(0, 99)
        numberTwo = 100 - numberOne
        return render(request, 'index.html',{"numberOne": numberOne, "numberTwo": numberTwo, "method": "plus"})
    elif case == 2:
        numberOne = random.randint(101, 200)
        numberTwo = numberOne - 100
        return render(request, 'index.html',{"numberOne": numberOne, "numberTwo": numberTwo, "method": "minus"})
    elif case == 3:
        pool = [1,2,4,5,10,20,25,50,100]
        numberOne = random.choice(pool)
        numberTwo = int(100 / numberOne)
        return render(request, 'index.html',{"numberOne": numberOne, "numberTwo": numberTwo, "method": "multiply"})
    elif case == 4:
        numberOne = random.randint(1,9) * 100
        numberTwo = int(numberOne / 100)
        return render(request, 'index.html',{"numberOne": numberOne, "numberTwo": numberTwo, "method": "diverge"})

# Create your views here.
