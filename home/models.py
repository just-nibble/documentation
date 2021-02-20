from django.db import models

# Create your models here.


class Project(models.Model):
    topic = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.topic

    class Meta:
        ordering = ('topic',)


class Documentation(models.Model):
    project = models.ForeignKey(
        Project, blank=True,
        null=True, on_delete=models.CASCADE
        )
    topic = models.CharField(max_length=200, blank=True, null=True)
    body = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.topic

    class Meta:
        ordering = ('topic',)
