# Generated by Django 4.2.2 on 2023-06-19 14:51

from django.db import migrations, models
import main.utils


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_chefs_facebook_alter_chefs_instagram_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_a_table',
            name='phone',
            field=models.CharField(max_length=12, validators=[main.utils.validate_phone_number], verbose_name='Мобильный телефон'),
        ),
        migrations.AlterField(
            model_name='chefs',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='shefs/', verbose_name='Изображение'),
        ),
    ]
