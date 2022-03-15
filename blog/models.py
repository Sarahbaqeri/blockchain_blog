from django.db import models
from django.shortcuts import reverse


class PostBlog(models.Model):
    STATUS_CHOISES = (
        ('pub', 'published'),
        ('drf', 'draft'),
    )

    author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOISES, max_length=10)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_id', args=[self.id])
