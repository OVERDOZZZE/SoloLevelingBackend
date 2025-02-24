from django.db import models
from django.core.validators import MinValueValidator
from cloudinary.models import CloudinaryField


class Skill(models.Model):
    name = models.CharField(max_length=255)
    skill_image = CloudinaryField(
        'skills/',
        blank=True,
        null=True,
        default='https://res.cloudinary.com/dvo1jlfym/image/upload/v1740378927/default_item_dw3tqa.png'
    )
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.name


class Task(models.Model):
    TASK_STATUS = (
        ('completed', 'Completed'),
        ('not_completed', 'Not completed')
    )
    description = models.TextField(max_length=1000)
    task_status = models.CharField(
        max_length=255,
        choices=TASK_STATUS,
        default='not_completed',
        db_index=True
    )
    value_exp = models.IntegerField(validators=[MinValueValidator(0)])

    def __str__(self):
        return f'{self.description}  +{self.value_exp}'


class Achievement(models.Model):
    ACHIEVEMENT_TYPES = (
        ('level', 'Completed Level'),
        ('exp', 'Gained Experience')
    )

    name = models.CharField(max_length=255)
    value_exp = models.IntegerField(validators=[MinValueValidator(0)])
    description = models.TextField(max_length=1000, blank=True, null=True)
    achievement_type = models.CharField(max_length=255, choices=ACHIEVEMENT_TYPES)
    achievement_image = CloudinaryField(
        'achievements/',
        blank=True,
        null=True,
        default='https://res.cloudinary.com/dvo1jlfym/image/upload/v1740378927/default_item_dw3tqa.png'
    )

    def __str__(self):
        return self.name


class Tip(models.Model):
    text = models.TextField(max_length=255)

    def __str__(self):
        return self.text


class Quest(models.Model):
    QUEST_STATUS = (
        ('completed', 'Completed'),
        ('in_progress', 'In progress'),
        ('not_completed', 'Not completed'),
        ('failed', 'Failed')
    )
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=1000, blank=True, null=True)
    quest_status = models.CharField(max_length=255, choices=QUEST_STATUS, default='not_completed')
    value_exp = models.IntegerField(validators=[MinValueValidator(0)])
    tasks = models.ManyToManyField(Task, blank=True)
    skill = models.ForeignKey(Skill, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.name}  +{self.value_exp}'


class Level(models.Model):
    class Meta:
        ordering = ['level_number']

    level_number = models.IntegerField(
        validators=[
            MinValueValidator(0)
        ],
        default=0
    )
    name = models.CharField(max_length=255, default=f'NONAME lvl.{level_number}')
    achievement = models.ForeignKey(Achievement, blank=True, null=True, on_delete=models.SET_NULL)
    required_exp = models.IntegerField(
        validators=[
            MinValueValidator(0)
        ]
    )
    quests = models.ManyToManyField(Quest, blank=True)
    tips = models.ManyToManyField(Tip, blank=True)
    level_image = CloudinaryField(
        'levels/',
        blank=True,
        null=True,
        default='https://res.cloudinary.com/dvo1jlfym/image/upload/v1740378324/level_default_w5guht.jpg'
    )

    def __str__(self):
        return f'{self.level_number}. {self.name}'
