# Generated by Django 3.2.5 on 2021-07-23 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lenderBorrower', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lenderborrower',
            name='borrowerEnddate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lenderborrower',
            name='borrowerStartdate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lenderborrower',
            name='lenderEnddate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lenderborrower',
            name='lenderStartdate',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
