# Generated by Django 4.2.17 on 2024-12-23 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=6)),
                ('size', models.DecimalField(decimal_places=2, max_digits=6)),
                ('description', models.TextField()),
                ('age_limited', models.BooleanField(default=False)),
                ('buyer', models.ManyToManyField(related_name='games', to='m19_task1.buyer')),
            ],
        ),
    ]
