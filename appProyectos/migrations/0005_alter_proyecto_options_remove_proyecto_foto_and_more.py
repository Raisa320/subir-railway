# Generated by Django 4.1.4 on 2022-12-08 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appProyectos', '0004_alter_proyecto_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='proyecto',
            options={'verbose_name': 'Proyecto', 'verbose_name_plural': 'Proyectos'},
        ),
        migrations.RemoveField(
            model_name='proyecto',
            name='foto',
        ),
        migrations.AddField(
            model_name='proyecto',
            name='foto_img',
            field=models.ImageField(blank=True, upload_to='proyect_file'),
        ),
        migrations.AddField(
            model_name='proyecto',
            name='foto_url',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
