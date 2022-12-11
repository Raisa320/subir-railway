from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.urls  import reverse
# Create your models here.


class Proyecto(models.Model):
    """Model definition for Proyecto."""

    # TODO: Define fields here
    title = models.CharField(max_length=100)
    descripcion = models.TextField()
    foto_img = models.ImageField(upload_to="proyect_file",blank=True,null=True)
    foto_url = models.CharField(max_length=500,blank=True)
    git = models.CharField(max_length=500)
    tags = models.CharField(max_length=500)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Proyecto."""

        # db_table = "proyectos"
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"

    def __str__(self):
        """Unicode representation of Proyecto."""
        return self.title

    def get_absolute_url(self):
        return reverse("proyecto-ver", kwargs={"pk": self.pk})

    def save(self):
        super().save()
        if self.foto_img:
            foto_img = Image.open(self.foto_img.path)
            if foto_img.height > 300 or foto_img.width > 300:
                output_size = (300, 300)
                foto_img.thumbnail(output_size)
                foto_img.save(self.foto_img.path)
