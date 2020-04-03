from django import forms
from .models import Animal, Dog, Cat, Dragon


class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = '__all__'


class DogForm(forms.ModelForm):
    class Meta:
        model = Dog
        fields = '__all__'


class CatForm(forms.ModelForm):
    class Meta:
        model = Cat
        fields = '__all__'


class DragonForm(forms.ModelForm):
    class Meta:
        model = Dragon
        fields = '__all__'


class FormChoiceForm(forms.Form):
    form_choice = forms.ChoiceField(label='Form', choices=[
        ('dog', 'Dog Form'),
        ('cat', 'Cat Form'),
        ('dragon', 'Dragon Form'),
        ('animal', 'Animal Form'),
        ])
