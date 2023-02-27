from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Review(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    rating = models.IntegerField(validators=[MinValueValidator(1, "Минимальная оценка - 1"), MaxValueValidator(10, "Максимальная оценка - 10")])
    comment = models.TextField(max_length=200, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    like_count = models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return f"{self.name} {self.rating}/10"