# Generated by Django 3.0.3 on 2020-05-20 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppTwo', '0002_auto_20200517_1215'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfileInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profolio', models.URLField(blank=True)),
                ('picture', models.ImageField(upload_to='profile_pics')),
                ('user', models.OneToOneField(on_delete=AttributeError, to='AppTwo.User')),
            ],
        ),
    ]
