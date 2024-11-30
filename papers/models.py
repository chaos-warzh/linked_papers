from django.db import models

# Create your models here.


class Paper(models.Model):
    title = models.CharField(max_length=255)
    abstract = models.TextField()
    category = models.CharField(max_length=255)
    year = models.IntegerField()

    def __str__(self):
        return self.title


class Citation(models.Model):
    citing_paper = models.ForeignKey(Paper, related_name='citing_papers', on_delete=models.CASCADE)
    cited_paper = models.ForeignKey(Paper, related_name='cited_papers', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.citing_paper.title} citing {self.cited_paper.title}"
