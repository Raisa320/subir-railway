from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage as storage    

# Create your models here.
class Profile(models.Model):
    """Model definition for Profile."""

    # TODO: Define fields here
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=254)
    phone = models.CharField(max_length=9, blank=True)
    about = models.TextField(blank=True)
    pais = models.CharField(max_length=50)
    image = models.ImageField(default="default.jpg", upload_to="profile_pics")
    servicios = models.CharField(max_length=500, blank=True)
    gitPerfil = models.CharField(max_length=500, blank=True)
    linkedPerfil = models.CharField(max_length=500, blank=True)

    class Meta:
        """Meta definition for usuario."""

        verbose_name = "profile"
        verbose_name_plural = "profiles"

    def __str__(self):
        """Unicode representation of usuario."""
        return f"{self.user.username} Profile"

    def save(self, *args, **kwargs):
        super(Profile,self).save(*args, **kwargs)
        if self.image:
            # After save, read the file
            image_read = storage.open(self.image.name, "r")
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
                user = User.objects.get(pk=self.pk)
                user.profile.image.save(self.image.name, ContentFile(imageBuffer.getvalue()))

                image_read = storage.open(user.profile.image.name, "r")
                image = Image.open(image_read)
            image_read.close()



class VisitanteGeneral(models.Model):
    """Model definition for Visitante."""
    # TODO: Define fields here
    ipVisitante= models.GenericIPAddressField()
    #protafolioVisitado = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Visitante."""

        verbose_name = 'Visitante'
        verbose_name_plural = 'Visitantes'

    def __str__(self):
        """Unicode representation of Visitante."""
        return self.ipVisitante

class VisitantePortafolio(models.Model):
    """Model definition for Visitante."""
    # TODO: Define fields here
    ipVisitante= models.GenericIPAddressField()
    protafolioVisitado = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Visitante."""

        verbose_name = 'Visitante'
        verbose_name_plural = 'Visitantes'

    def __str__(self):
        """Unicode representation of Visitante."""
        return self.ipVisitante
