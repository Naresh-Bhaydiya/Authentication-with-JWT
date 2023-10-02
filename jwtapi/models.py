from django.db import models
from django.contrib.auth.models import User


class RegisterUser(User):
    mobileNo = models.CharField(max_length=15)
    city = models.CharField(max_length=80)
    
    
    class Meta:
        db_table = 'UserReg'
    
    def __str__(self) -> str:
        return self.username
    
class Book(models.Model):
   book_name = models.CharField(max_length=80)
   book_title = models.CharField(max_length=80)
   book_lesson = models.CharField(max_length=80)
   book_price = models.CharField(max_length=80)
   
   class Meta:
       db_table = 'Book'
       
   def __str__(self) -> str:
       return self.book_name
    