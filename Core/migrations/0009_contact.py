# Generated by Django 4.0.5 on 2022-06-12 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0008_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('message', models.TextField(max_length=4000)),
                ('email', models.CharField(max_length=50)),
            ],
        ),
    ]