# Generated by Django 4.1.7 on 2023-02-23 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('bio', models.TextField()),
                ('image', models.ImageField(upload_to='authors/')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('cover_image', models.ImageField(upload_to='covers/')),
                ('pdf_file', models.FileField(upload_to='books/')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Books.author')),
            ],
        ),
    ]
