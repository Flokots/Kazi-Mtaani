# Generated by Django 4.0.5 on 2022-06-22 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kazimtaani', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsLetterRecipients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
