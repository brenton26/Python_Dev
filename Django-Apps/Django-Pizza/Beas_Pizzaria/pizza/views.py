from django.shortcuts import render
from .forms import PizzaForm, MultiplePizzaForm
from django.forms import formset_factory

# Create your views here.
def home(request):
    return render(request, 'pizza/home.html')


def order(request):
    multiple_form = MultiplePizzaForm()
    if request.method == 'POST':
        # filled_form = PizzaForm(request.POST, request.FILES) # could be used if we wanted a user to upload a file
        filled_form = PizzaForm(request.POST)
        if filled_form.is_valid():  #is_valid checks all validations against request.POST data
            filled_form.save()
            size = filled_form.cleaned_data['size']  #cleaned_data ensures that validation rules for the form are satisfied 
            topping1 = filled_form.cleaned_data['topping1']
            topping2 = filled_form.cleaned_data['topping2']
            note = f"Thanks for ordering, bitch. Your {size} {topping1} and {topping2} pizza is on it's way"
            new_form = PizzaForm()
            return render(request, 'pizza/order.html', {'pizzaform':new_form, 'note':note, 'multiple_form':multiple_form})
    else:
        form = PizzaForm()
        return render(request, 'pizza/order.html', {'pizzaform': form, 'multiple_form':multiple_form})


def pizzas(request):
    number_of_pizzas = 2
    filled_multiple_pizza_form = MultiplePizzaForm(request.GET)
    if filled_multiple_pizza_form.is_valid():
        number_of_pizzas = filled_multiple_pizza_form.cleaned_data['number']
    PizzaFormSet = formset_factory(PizzaForm, extra=number_of_pizzas)
    formset = PizzaFormSet()
    if request.method == 'POST':
        filled_formset = PizzaFormSet(request.POST)
        if filled_formset.is_valid():
            for form in filled_formset:
                print(form.cleaned_data['topping1'])
            note = "Pizzas have been ordered!"
        else:
            note = "Order was not created, please try again."
        return render(request, 'pizza/pizzas.html', {'note':note, 'formset':formset})
    else:
        return render(request, 'pizza/pizzas.html', {'formset':formset})