from django.db import models

# Create your models here.
class project(models.Model):
  projectname = models.CharField(max_length=255)
  from_date = models.DateField(null=True)
  end_date = models.DateField(null=True)
  description = models.CharField(max_length=255)
  image = models.ImageField(upload_to="img/")

  def __str__(self):
    return f"{self.projectname}"