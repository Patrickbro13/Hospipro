# Generated by Django 2.2.5 on 2019-09-24 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20190924_2036'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='email',
            field=models.EmailField(default='nishit@gmail.com', max_length=250),
        ),
    ]
