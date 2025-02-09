# Generated by Django 5.0.3 on 2024-03-24 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_remove_item_added_by_remove_item_date_removed_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='cpu',
            field=models.CharField(choices=[('I7-7700HQ', 'I7-7700HQ'), ('I7-8750H', 'I7-8750H'), ('M2 10C', 'M2 10C'), ('BCM2711C0', 'BCM2711C0'), ('6-Core Intel Core I5', '6-Core Intel Core I5')], max_length=100, null=True, verbose_name='CPU'),
        ),
        migrations.AlterField(
            model_name='item',
            name='gpu',
            field=models.CharField(choices=[('GTX 1070', 'GTX 1070'), ('RTX 2070', 'RTX 2070')], max_length=100, null=True, verbose_name='GPU'),
        ),
        migrations.AlterField(
            model_name='item',
            name='ram',
            field=models.CharField(choices=[('32', '32'), ('16', '16')], max_length=100, null=True, verbose_name='RAM'),
        ),
        migrations.AlterField(
            model_name='item',
            name='type',
            field=models.CharField(choices=[('Mobile Device', 'Mobile Device'), ('Non-Portable PC', 'Non-Portable PC'), ('Laptop', 'Laptop'), ('Standalone Headset', 'Standalone Headset')], max_length=100, null=True, verbose_name='Device type'),
        ),
    ]
