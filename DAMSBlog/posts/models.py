from django.db import models
from django.db.models.signals import pre_save
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone

# Create your models here.
# MVC - Model View Controller


class PostManager(models.Manager):
    def all(self, *args, **kwargs):
        #  Post.objects.all() = super(PostManager, self).all()
        return super(PostManager, self).filter(draft=False).filter(publish__lte=timezone.now())


def upload_location(instance, filename):
    filebase, extention = filename.split(".")
    return "%s/%s.%s" % (instance.id, instance.id, extention)
    return "%s/%s" % (instance.id, filename)


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to=upload_location, null=True, blank=True, width_field="width_field",
                              height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    content = models.TextField()
    draft = models.BooleanField(default=False)
    publish = models.DateField(auto_now=False, auto_now_add=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts_detail", kwargs={'id': self.id})

    class Meta:
        ordering = ['-timestamp', '-updated']


def check_slug_creation(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug

    query_set = Post.objects.filter(slug=slug).order_by("-id")
    exists = query_set.exists()
    if exists:
        new_slug = "%s-%s" % (slug, query_set.first().id)
        return check_slug_creation(instance, new_slug=new_slug)
    return slug


def pre_save_post_signal_receive(sender, instance, *args, **kwargs):
    slug = slugify(instance.title)
    #  "Tesla item 1" => "tesla-item-1"
    exists = Post.objects.filter(slug=slug).exists()
    if exists:
        slug = f"{slug} {instance.id}"
    instance.slug = slug


pre_save.connect(pre_save_post_signal_receive, sender=Post)