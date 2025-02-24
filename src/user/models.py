from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField
from django.core.validators import MinValueValidator
from ..main.models import Achievement, Skill, Level


class User(AbstractUser):
    bio = models.TextField(max_length=2000, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    overall_exp = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0)
        ]
    )
    level = models.ForeignKey(Level, blank=True, null=True, on_delete=models.SET_NULL)
    achievements = models.ManyToManyField(Achievement, blank=True)
    skills = models.ManyToManyField(Skill, blank=True)
    user_image = CloudinaryField(
        'users/',
        blank=True,
        null=True,
        default='https://res.cloudinary.com/dvo1jlfym/image/upload/v1740376966/profile_soldier_da3kfy.png'
    )

    def save(self, *args, **kwargs):
        if not self.level:
            first_level = Level.objects.filter(level_number=1).first()
            self.level = first_level if first_level else None
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.username} lvl.{self.level}'
