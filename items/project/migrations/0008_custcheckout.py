# Generated by Django 4.2.3 on 2023-08-17 05:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0007_checkout'),
    ]

    operations = [
        migrations.CreateModel(
            name='custcheckout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.createacc')),
            ],
        ),
    ]
