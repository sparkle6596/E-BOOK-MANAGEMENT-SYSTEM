from django.db import models

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator

def validate_rate(value):
    if value >= 5:
        raise ValidationError(
            _('%(value)s rating must be less than 5'),
            params={'value': value},
        )


class books(models.Model):
    CATEGORY = (
        ('Fantasy', 'Fantasy'),
        ('Literary', 'Literary'),
        ('Mystery', 'Mystery'),
        ('Non-Fiction', 'Non-Fiction'),
        ('Science', 'Science'),
        ('Fiction', 'Fiction'),
        ('Thriller', 'Thriller'),
    )

    book_name=models.CharField(max_length=200,unique=True)
    author=models.CharField(max_length=200)
    category=models.CharField(max_length=200,choices=CATEGORY, null=True)
    review = models.IntegerField(null=True)

    favourites = models.BooleanField(default=True)
    image = models.ImageField(upload_to='pic', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.book_name


class users(models.Model):
    name=models.CharField(max_length=200,unique=True)
    image=models.ImageField(default='default.jpg', upload_to='profile')

    def __str__(self):
        return self.name


