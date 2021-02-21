from django.db import models
from django.utils.text import slugify

# Create your models here.


class Documentation(models.Model):
    topic = models.CharField(max_length=200, blank=True, null=True)
    body = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.topic

    class Meta:
        ordering = ('topic',)


class Project(models.Model):
    topic = models.CharField(max_length=200, blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    documentation = models.ManyToManyField(
        Documentation,
        blank=True,
    )

    def __str__(self):
        return self.topic

    def save(self, *args, **kwargs):
        self.slug = slugify(self.topic)
        super(Project, self).save()

    def get_absolute_url(self):
        return reverse('project', kwargs={
                "slug": self.slug,
                "pk": self.pk
            })

    class Meta:
        ordering = ('topic',)



