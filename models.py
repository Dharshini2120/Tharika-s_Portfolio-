from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=100) # e.g., Python, React
    github_link = models.URLField(blank=True)     # Optional link

    def __str__(self):
        return self.title