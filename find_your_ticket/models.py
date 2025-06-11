from django.db import models

# Create your models here.
class users(models.Model):
    username=models.CharField(max_length=20,null=False)
    password=models.CharField(max_length=10,null=False)



class movie_info(models.Model):
    movie_id = models.IntegerField(null=False)
    movie_name=models.CharField(max_length=50,null=True)
    genre=models.CharField(max_length=50,null=False)
    time=models.CharField(max_length=30,null=False)
    director=models.CharField(max_length=40,null=False)

class seat_info(models.Model):
    seat_no = models.IntegerField(null=False)
    seat_type=models.CharField(max_length=20,null=False)

class theatre_info(models.Model):
    thatre_id= models.IntegerField(null=False)
    loaction=models.CharField(max_length=50,null=False)
    t_name=models.CharField(max_length=50,null=False)
    screen_no= models.IntegerField(null=False)

    
class show_info(models.Model):
    show_id = models.IntegerField(null=False)
    movie_id=models.ForeignKey(movie_info, on_delete=models.CASCADE,null=False)
    theatre_id=models.ForeignKey(theatre_info, on_delete=models.CASCADE,null=False)
    start_time=models.TimeField(max_length=10,null=False)
    date=models.DateField(max_length=10,null=False)
    end_time=models.TimeField(max_length=10,null=False)