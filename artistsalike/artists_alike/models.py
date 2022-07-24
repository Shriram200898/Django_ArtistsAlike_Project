from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Users(models.Model):
    User_id= models.BigAutoField(auto_created=True, primary_key=True, serialize=False)
    Email = models.EmailField()
    Username = models.CharField(max_length=150)
    Firstname=models.CharField(max_length=150)
    Lastname = models.CharField(max_length=150)
    Password=models.CharField(max_length=150)
    Cpassword=models.CharField(max_length=150)
    DOB=models.DateField()
    Gender=models.CharField(max_length=150)
    Mobileno=models.CharField(max_length=10)
    Address=models.TextField()
    Profile_Photo=models.ImageField(upload_to="image")


class Artists(models.Model):
    Artist_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False)
    Artist_Email = models.EmailField()
    Artist_Firstname = models.CharField(max_length=150)
    Artist_Lastname = models.CharField(max_length=150)
    Artist_Category = models.CharField(max_length=150)
    Category_Price = models.CharField(max_length=150)
    Artist_Password = models.CharField(max_length=150)
    Artist_Cpassword = models.CharField(max_length=150)
    Artist_DOB = models.DateField()
    Artist_Gender=models.CharField(max_length=150)
    Artist_Mobileno=models.CharField(max_length=10)
    Artist_Address=models.TextField()
    Artist_Photo=models.ImageField(upload_to="image")
    Avg_Rating = models.FloatField(default=0.0)
    is_active = models.BooleanField(default=False)

class Category(models.Model):
    Category_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False)
    Category_Name = models.CharField(max_length=100)
    Category_Description = models.CharField(max_length=2000)

class Order(models.Model):
    Order_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False)
    Artist = models.ForeignKey(Artists,default=1,on_delete=models.SET_DEFAULT)
    User = models.ForeignKey(Users,default=1,on_delete=models.SET_DEFAULT)
    Order_Date = models.DateField(auto_now_add=True)
    User_Name = models.CharField(max_length=150)
    Artist_Name = models.CharField(max_length=150)
    Artist_Email = models.EmailField()
    O_Category = models.CharField(max_length=150)
    Price = models.IntegerField()
    Order_Description = models.TextField()
    Mobile_No = models.CharField(max_length=10)
    User_Email = models.EmailField()
    Upload_File = models.FileField(upload_to='UploadedFile')
    Edited_File = models.FileField(upload_to='EditedFile/')
    Order_Status = models.BooleanField(default=False)
    Payment_Status = models.BooleanField(default=False)

class Feedback(models.Model):
    Feedback_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False)
    Order = models.ForeignKey(Order, default=1, on_delete=models.SET_DEFAULT)
    Artist = models.ForeignKey(Artists,default=1,on_delete=models.SET_DEFAULT)
    Artist_Email = models.EmailField()
    User = models.ForeignKey(Users,default=1,on_delete=models.SET_DEFAULT)
    Feedback_Date = models.DateField(auto_now_add=True)
    User_Name = models.CharField(max_length=150)
    User_Email = models.EmailField()
    Description = models.CharField(max_length=2000, default='Did you got what you are looking for? = ')
    Suggestions = models.TextField()
    Rating = models.IntegerField()


class Admin(models.Model):
    Admin_id= models.BigAutoField(auto_created=True, primary_key=True, serialize=False)
    Admin_Email = models.EmailField()
    Admin_Password=models.CharField(max_length=150)



