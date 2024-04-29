# Generated by Django 4.2.11 on 2024-04-29 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.PositiveIntegerField()),
                ('quantity', models.PositiveIntegerField()),
                ('category', models.CharField(choices=[('F', 'Food'), ('E', 'ElectronicProducts'), ('C', 'Clothing'), ('O', 'Other')], max_length=1)),
            ],
        ),
    ]