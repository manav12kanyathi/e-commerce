# Generated by Django 4.2.3 on 2023-08-31 12:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project', '0009_wish'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('productid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.descri')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='custcheckout',
            name='userid',
        ),
        migrations.DeleteModel(
            name='checkout',
        ),
        migrations.DeleteModel(
            name='custcheckout',
        ),
    ]
