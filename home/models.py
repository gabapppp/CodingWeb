from django.db import models
from django.contrib.auth.models import User


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'media/user_{0}/{1}'.format(instance.author.id, filename)


LANGUAGE_CHOICE = [
    ('CPP', 'C++'),
    ('JS', 'JavaScript'),
    ('JAV', 'Java'),
    ('PY', 'Python')
]


class Source(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    filename = models.CharField(max_length=100, blank=True)
    file = models.FileField(upload_to=user_directory_path)
    language = models.CharField(
        choices=LANGUAGE_CHOICE, max_length=100, default='PY')
    created = models.DateTimeField(auto_now_add=True)
