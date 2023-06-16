from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# from mychatapp.models import Friend

def custom_upload_to(instance, filename):
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return 'profiles/' + filename

# Create your models here.
class Profile(models.Model):
    # id_profile  = models.ForeignKey(User, null=True, blank=False, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # numero_ID = models.AutoField(primary_key=True, editable=False)
    avatar = models.ImageField(upload_to=custom_upload_to, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    link = models.URLField(max_length=200, null=True, blank=True)
    name = models.TextField(max_length=100, null=True, blank=True)
    last_name = models.TextField(max_length=100, null=True, blank=True)
    job = models.TextField(max_length=10, null=True, blank=True)
    unidad = models.TextField(max_length=10, null=True, blank=True)
    # pic = models.ImageField(upload_to="img", blank=True, null=True)
    friends = models.ManyToManyField('Friend', related_name = "my_friends")
    
    def __str__(self):
        return self.user
    
    class Meta:
        ordering = ['user__username']
        # ordering = ['profile_ID']

class Friend(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    # id_friend  = models.ForeignKey(User, null=True, blank=False, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.profile.name

@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, **kwargs):
    if kwargs.get('created', False):
        Profile.objects.get_or_create(user=instance)
        # print("Se acaba de crear un usuario y su perfil enlazado")