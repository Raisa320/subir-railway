from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.urls  import reverse
from io import BytesIO
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage as storage   
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

    def save(self,*args, **kwargs):
        super(Proyecto,self).save(*args, **kwargs)
        if self.foto_img:
            # After save, read the file
            image_read = storage.open(self.foto_img.name, "r")
            image = Image.open(image_read)
            if image.height > 300 or image.width > 300:
                size = 300, 300
                # Create a buffer to hold the bytes
                imageBuffer = BytesIO()
                # Resize  
                image.thumbnail(size, Image.ANTIALIAS)
                # Save the image as jpeg to the buffer
                image.save(imageBuffer, image.format)
                # Save the modified image
                proyecto = Proyecto.objects.get(pk=self.pk)
                proyecto.foto_img.save(self.foto_img.name, ContentFile(imageBuffer.getvalue()))

                image_read = storage.open(proyecto.foto_img.name, "r")
                image = Image.open(image_read)
            image_read.close()
