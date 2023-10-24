# Generated by Django 4.2.6 on 2023-10-24 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_comunicado_detalle_alter_comunicado_titulo'),
    ]

    operations = [
        migrations.AddField(
            model_name='comunicado',
            name='TIPO_CHOICES',
            field=models.CharField(choices=[('S', 'Suspension de actividades'), ('C', 'Suspension de clases'), ('I', 'Informacion')], default='S', max_length=1),
        ),
    ]
