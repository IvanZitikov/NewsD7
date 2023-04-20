from django.db import models
# Post.objects.order_by('-rating')[0].comment_set.all().values('dateCreation', 'commentUser__username', 'rating', 'text')
full_name = models.CharField(max_length=256, unique=True)
age = models.IntegerField(blank=True)
email = models.CharField(blank=True, max_length=128)


class User(models.Model):
    user_name = models.CharField(max_length=255)
    user_password = models.CharField(max_length=255)
    user_email = models.EmailField()
    user_activity = models.CharField(max_length=255)
    user_date_registration = models.DateField(auto_now_add=True)
    user_access = models.BooleanField(default=True)
