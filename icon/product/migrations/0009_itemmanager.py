# Generated by Django 3.1 on 2020-09-02 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_item_featured_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
