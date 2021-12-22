from django.db import models

   



class Person(models.Model):
    gender_choices = (
        ('male','Male'),
        ('female','Female')
    )
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=120,unique=True)
    password = models.CharField(max_length=150)
    contact_no = models.CharField(max_length=15)
    gender = models.CharField(max_length=10,choices=gender_choices,default=gender_choices[0][0])
    date_of_birth = models.DateField()
    blood_group = models.CharField(max_length=10)
    avatar = models.ImageField(upload_to="avatar/",blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    
    class Meta:
        abstract=True
    


