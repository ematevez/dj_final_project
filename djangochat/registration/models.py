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
    avatar = models.ImageField(upload_to=custom_upload_to, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    link = models.URLField(max_length=200, null=True, blank=True)
    job = models.TextField(max_length=200, null=True, blank=True)
<<<<<<< HEAD
    name = models.TextField(max_length=100, null=True, blank=True)
    last_name = models.TextField(max_length=100, null=True, blank=True)
    # pic = models.ImageField(upload_to="img", blank=True, null=True)
    friends = models.ManyToManyField('Friend', related_name = "my_friends")
    
    def __str__(self):
        return self.user + ' ' + self.name + ' ' + self.last_name
=======
>>>>>>> f849a777eae18a9012c715445b23a6cf2612f120

    class Meta:
        ordering = ['user__username']

class Friend(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    id_friend  = models.ForeignKey(User, null=True, blank=False, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.profile.name

@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, **kwargs):
    if kwargs.get('created', False):
        Profile.objects.get_or_create(user=instance)
        # print("Se acaba de crear un usuario y su perfil enlazado")