# Generated by Django 5.0 on 2024-10-05 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_rename_blog_catgory_blog_blog_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_first_name', models.CharField(max_length=50)),
                ('author_last_name', models.CharField(max_length=50)),
                ('author_country', models.CharField(max_length=50)),
                ('joined_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
