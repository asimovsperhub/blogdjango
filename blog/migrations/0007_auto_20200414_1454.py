# Generated by Django 2.2.5 on 2020-04-14 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200414_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='tags',
            field=models.ManyToManyField(related_name='Tag', to='blog.Tag', verbose_name='标签'),
        ),
    ]
