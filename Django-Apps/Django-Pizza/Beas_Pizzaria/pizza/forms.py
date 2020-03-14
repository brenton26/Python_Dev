from django import forms
from .models import Pizza, Size

# class PizzaForm(forms.Form):
#     # This let's users write in any topping. Notice the widget lets you further customize user input
#     # topping1 = forms.CharField(label='Topping 1', max_length=50, widget=forms.Textarea)
#     # topping2 = forms.CharField(label='Topping 2', max_length=50)

#     # This creates a list of toppings for users to select from:
#     # toppings = forms.MultipleChoiceField(choices=[
#     #     ('pep', 'Pepperoni'),
#     #     ('cheese', 'Cheese'),
#     #     ('sausage', 'Sausage')
#     # ], widget=forms.CheckboxSelectMultiple)

#     size = forms.ChoiceField(label='Size', choices=[
#         ('Small', 'Small'),
#         ('Medium', 'Medium'),
#         ('Large', 'Large')
#     ])


class PizzaForm(forms.ModelForm):
    # size = forms.ModelChoiceField(queryset=Size.objects, empty_label=None, widget=forms.RadioSelect )
    # image = forms.ImageField()

    class Meta:
        model = Pizza
        fields = ['topping1', 'topping2', 'size']
        labels = {
            'topping1': 'Topping 1',
            'topping2': 'Topping 2'
        }
        # widgets = {'size':forms.CheckboxSelectMultiple}

class MultiplePizzaForm(forms.Form):
    number = forms.IntegerField(min_value=2, max_value=10)
 