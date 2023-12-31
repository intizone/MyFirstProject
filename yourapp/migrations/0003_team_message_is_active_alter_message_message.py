# Generated by Django 5.0.1 on 2024-01-04 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yourapp', '0002_alter_message_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='message',
            field=models.TextField(),
        ),
    ]
