from django.forms import ModelForm
from .models import review,novels

class reviewForm(ModelForm):
    class Meta:
        model = review
        fields = '__all__'

# class BookForm(ModelForm):
#     class Meta:
#         model = Book
#         fields = ['name', 'authors']