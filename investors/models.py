from django.db import models
from django.shortcuts import reverse

# Create your models here.
class investor_type(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return str(self.category)

class investor(models.Model):
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=10)
    logo = models.ImageField(upload_to='investors',default='no_picture.png')
    reg_no = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    post_code = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    key_contact = models.CharField(max_length=100)
    contact_email = models.EmailField(max_length=100, default="")
    category = models.ForeignKey(investor_type, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('investors:detail', kwargs={'pk':self.pk})

    
class investor_contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=15,null=True)
    main_contact = models.BooleanField(default=False)
    adv_board_rep = models.BooleanField(default=False)
    inv_comm_rep = models.BooleanField(default=False)
    reports = models.BooleanField(default=True)
    contact_investor = models.ForeignKey(investor,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)

class investor_file(models.Model):
    description = models.CharField(max_length=100)
    inv_file = models.FileField(upload_to='investors/')
    investor = models.ForeignKey(investor,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.description)
