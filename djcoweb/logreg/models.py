import re, bcrypt
from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def validate(self, postData):
        errors = {}
        if postData['form'] == 'create':
            if len(postData['name']) <= 3:
                errors["name"] = 'Name must be at least 3 characters long'
            EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
            if not EMAIL_REGEX.match(postData['email']):
                errors['email'] = 'Invalid email'
            if User.objects.filter(email = postData['email']):
                errors['email'] = "Already have an existing account"
            if len(postData['number']) != 10:
                errors['number'] = 'Invalid phone number'
            if len(postData['pword']) < 8:
                errors['pword'] = 'Password must be at least 8 characters'
            return errors
        else:
            if not User.objects.filter(email = postData['lemail']):
                errors['lemail'] = "User does not exist"
                return errors
            if not bcrypt.checkpw(postData['lpword'].encode(), User.objects.get(email = postData['lemail']).password.encode()):
                errors['lpword'] = "Incorrect password"
            return errors
class User(models.Model):
    name = models.CharField(max_length = 50)
    email = models.CharField(max_length = 100)
    number = models.IntegerField()
    password = models.CharField(max_length = 200)
    objects = UserManager()

    def __str__(self):
        return self.name