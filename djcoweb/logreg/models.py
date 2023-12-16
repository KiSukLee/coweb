from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def validate(self, postData):
        errors = {}
        if postData['submit'] == 'create':
            if postData['name'] <= 3:
                errors["name"] = 'Name must be at least 3 characters long'
            if postData['email']:
                errors['email'] = 'Invalid email'
            if len(postData['number']) != 10:
                errors['number'] = 'Invalid phone number'
            if postData['pword'] < 8:
                errors['pword'] = 'Password must be at least 8 characters'
            return errors
        else:
            if User.objects.get['email'] != postData['name']:
                errors['email'] = "User does not exist"
            if User.objects.get['pword'] != postData['pword']:
                errors['pword'] = "Incorrect password"
            return errors
class User(models.Model):
    name = models.CharField(max_length = 50)
    email = models.CharField(max_length = 100)
    number = models.IntegerField()
    password = models.CharField(max_length = 200)
    objects = UserManager()

    def __str__(self):
        return self.name