# Generated by Django 4.2.1 on 2023-10-15 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='notes',
            name='notes',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
