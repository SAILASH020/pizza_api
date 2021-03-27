from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.

types = (('Regular', 'Regular'),
              ('Square', 'Square'))

size = (('Small', 'Small'),('Mediam','Mediam'),('Large','Large'))              

toppings = (("Onion", "Onion" ), 
            ("Tomato", "Tomato"), 
            ('Corn', 'Corn'), 
            ('Capsicum', 'Capsicum'), 
            ('Cheese', 'Cheese'), 
            ('Jalapeno', 'Jalapeno'))




class pizza(models.Model):
    Types = MultiSelectField(choices=types, max_length= 10, default="", editable=True)
    # name = models.CharField(max_length=100)
    Size = MultiSelectField(choices=size, default='')
    Toppings = MultiSelectField(choices=toppings, default='')


    def __str__(self):
        return self.name
    