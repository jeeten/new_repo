# Generated by Django 2.2.1 on 2019-05-14 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=125)),
                ('Price', models.FloatField(max_length=20)),
                ('CreatedDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]