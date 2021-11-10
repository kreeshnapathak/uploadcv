from django.db import models

STATE_CHOICE=(
    ('Pradesh 1','Pradesh 1'),
    ('Pradesh 2','Pradesh 2'),
    ('Pradesh 3','Pradesh 3'),
    ('Pradesh 4','Pradesh 4'),
    ('Pradesh 5','Pradesh 5'),
)

# Create your models here.
class Resume(models.Model):
    name= models.CharField(max_length=100)
    dob= models.DateField(auto_now=False,auto_now_add=False)
    gender = models.CharField(max_length=100)
    locality = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pin = models.PositiveIntegerField()
    state = models.CharField(choices=STATE_CHOICE,max_length=50)
    mobile = models.PositiveIntegerField()
    email = models.EmailField(max_length=100)
    job_city = models.CharField(max_length=50)
    profile_image = models.ImageField(upload_to='profileimg',blank=True)
    my_file= models.FileField(upload_to='doc',blank=True)

