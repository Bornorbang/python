# Generated by Django 5.0 on 2024-10-03 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_faq'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactFormLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('action_time', models.DateTimeField(blank=True, null=True)),
                ('is_success', models.BooleanField(default=False)),
                ('is_error', models.BooleanField(default=False)),
                ('error_message', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
