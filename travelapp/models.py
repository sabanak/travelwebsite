from django.db import models



# Create your models here.
#creating table place
class place(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='picture')
    desc=models.TextField()
    price=models.IntegerField()
    offer=models.BooleanField(default=False)

#creating table new
class new(models.Model):
    blog_date=models.DateField()
    heading=models.TextField()
    sub=models.TextField()
    details=models.TextField()
    imag=models.ImageField(upload_to='pic')



    # class Meta:
    #     ordering=['-date',]

#STATIC PAGE
# class place:
#     id:int
#     name:str
#     img:str
#     desc:str
#     price:str
#
# class news:
#     id:int
#     date_time:int
#     date_ti:str
#     imag:str
#     heading:str
#     sub:str
#     details:str

