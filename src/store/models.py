from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=75)
    kind = models.TextField()
    slug = models.SlugField(default='')

    class Meta:
        verbose_name = "Article"
        ordering = ['-title', '-kind']

    def __str__(self):
        return self.title

    @property
    def word_count(self):
        return len(self.slug.split('-'))