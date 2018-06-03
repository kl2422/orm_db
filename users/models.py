from django.db import models
from uuslug import slugify

# Create your models here.

class UserInfo(models.Model):
    userName = models.CharField(unique=True, db_column="user_name", max_length=20)
    password = models.CharField(max_length=20)
    slug = models.SlugField(editable=False, default='')

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.url_slug = slugify(self.userName)
        super(UserInfo, self).save(force_insert, force_update, using, update_fields)


class UserContract(models.Model):
    userInfo = models.OneToOneField(UserInfo, on_delete=models.CASCADE)
    phone = models.CharField(max_length=18, unique=True, null=True)