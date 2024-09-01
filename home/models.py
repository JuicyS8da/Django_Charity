from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

class Information(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    email = models.EmailField(blank=True)
    contact_email = models.EmailField()
    adress = models.TextField(blank=True)
    socials = models.ManyToManyField("Socials", blank=True)
    
    class Meta:
        verbose_name = 'Information'
        verbose_name_plural = 'Information'
    
    def __str__(self) -> str:
        return 'Information'

    def save(self, *args, **kwargs):
        self.__class__.objects.exclude(id=self.id).delete()
        super(Information, self).save(*args, **kwargs)

class Socials(models.Model):
    name = models.CharField(max_length=50, null=True)
    icon = models.ImageField(null=True)
    url = models.URLField(null=True)
    
    class Meta: 
        verbose_name = 'Socials'
        verbose_name_plural = 'Socials'
    
    def __str__(self) -> str:
        return self.name
    
    def clean(self):
        if Socials.objects.count() >= 5:
            raise ValidationError('You can\'t create more than 5 socials.')
    
class Volunteers(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=100)
    cv = models.FileField()
    comment = models.TextField()
    
    class Meta: 
        verbose_name = 'Volunteer'
        verbose_name_plural = 'Volunteers'
    
    def __str__(self) -> str:
        return self.name