from django.db import models

# Create your models here.
class trips(models.Model):
     location_name=models.TextField()
     tour_dates=models.CharField(max_length=100)
     preferences= models.TextField()
     image=models.ImageField(upload_to='images')

     def __str__(self):
        return self.location_name
   

class locs(models.Model):
    location_name=models.TextField()
    tour_dates=models.CharField(max_length=100)
    preferences= models.TextField()

    add_date=models.DateTimeField()
    image=models.ImageField(upload_to='images')
    cate=models.ForeignKey(trips,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

