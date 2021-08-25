from django.db import models

# Create your models here.

# City Model

class City(models.Model):
    code = models.CharField(max_length=3, verbose_name='Code', unique=True)  # city Code
    name = models.CharField(max_length=150, verbose_name='city')  # city Name

    class Meta:
        verbose_name = "city"
        verbose_name_plural = "Citys"
        ordering = ['code']  # Ordering by city Code

    def __str__(self):
        return self.name


    # Get full city
    def get_full_city(self):
        return '{} : {}'.format(self.code, self.name)  # Return complete city ( Code : Name )


# Hotel Model
class Hotel(models.Model):
    cit = models.ForeignKey(City, on_delete=models.CASCADE)  # Relationship with city
    hotel_code = models.CharField(max_length=5, verbose_name='Hotel Code', unique=True)  # Hotel Code
    hotel_name = models.CharField(max_length=150, verbose_name='Hotel Name')  # Hotel Name

    class Meta:
        verbose_name = "Hotel"
        verbose_name_plural = "Hotels"
        ordering = ['cit']  # Ordering by city Code

    def __str__(self):
        return self.hotel_name

    # Get full Hotel
    def get_full_hotel(self):
        return '{} : {} : {}'.format(self.cit, self.hotel_name, self.hotel_name)  # Return complete Hotel ( city : Code : Name )


