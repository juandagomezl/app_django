# Generated by Django 3.1.2 on 2021-02-15 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.TextField()),
                ('ciudad', models.TextField()),
                ('descripcion', models.TextField()),
            ],
        ),
    ]
