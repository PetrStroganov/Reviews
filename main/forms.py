from django import forms
from .models import Review
# class CreatReviewForm(forms.Form):
#     name = forms.CharField(max_length=30, label="Имя")
#     email = forms.EmailField(label="Почта")
#     rating = forms.IntegerField(max_value=10, min_value=0, label="Оценка")
#     comment = forms.CharField(max_length=200, widget=forms.Textarea(), label="Комментарий")
class CreatReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["name", "email", "rating", "comment"]
        labels = {
            "name": "Ваше Имя",
            "email": "Почта",
            "rating": "Оценка",
            "comment": "Комментарий"
        }
        error_messages = {
            "name": {
                "max_length": "Введите имя содержащее не более 30 букв",
                "required": "Это поле обязательно для заполнения"
            }
        }