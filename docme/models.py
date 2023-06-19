from django.db import models
from django.dispatch import receiver
from django.db.models import signals
from django.utils.text import slugify
from mdeditor.fields import MDTextField


class PostGroup(models.Model):
    title = models.CharField(max_length=1024)

    def __str__(self):
        return self.title


class Post(models.Model):
    group = models.ForeignKey(
        PostGroup, on_delete=models.CASCADE, related_name="posts")
    header = models.CharField(max_length=1024, blank=True)
    body = MDTextField(blank=True)
    slug = models.SlugField(max_length=1024, blank=True)
    order = models.IntegerField(default=1)

    def __str__(self):
        return self.header


class DocsSetting(models.Model):
    TEXT_SIZES = (
        ('sm', 'text-sm'),
        ('md', 'text-md'),
        ('lg', 'text-lg'),
        ('xl', 'text-xl'),
    )
    show_line_number = models.BooleanField(default=False)
    text_size = models.CharField(
        max_length=128, default="text-sm", choices=TEXT_SIZES)
    blur = models.CharField(max_length=128, blank=True)
    shadow = models.CharField(max_length=128, default="shadow")

    def __str__(self):
        return "Docs Website settings"


@receiver(signals.pre_save, sender=Post)
def populate_slug(sender, instance, **kwargs):
    instance.slug = slugify(instance.header)
    return
