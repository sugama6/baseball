# Generated by Django 3.0.4 on 2020-05-11 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0008_auto_20200510_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='img',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
