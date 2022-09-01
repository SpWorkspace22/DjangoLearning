from django.db import models

# Create your models here.

class Projects(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    role = models.CharField(max_length=100,null=True)
    start_date = models.DateField(blank=True,null=True)
    end_date = models.DateField(blank=True,null=True)
    project_link = models.URLField(null=True)

    def __str__(self):
        return self.title


class Skill_Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category


class Skills(models.Model):
    skill_type = models.ForeignKey(Skill_Category,on_delete=models.CASCADE)
    skill = models.CharField(max_length=100)

    def __str__(self):
        return self.skill
