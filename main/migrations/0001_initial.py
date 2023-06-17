# Generated by Django 4.2.2 on 2023-06-16 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book_A_Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=120, verbose_name='ФИО')),
                ('email', models.EmailField(max_length=120, verbose_name='Email')),
                ('phone', models.CharField(max_length=12, verbose_name='Мобильный телефон')),
                ('date', models.DateField(verbose_name='Дата')),
                ('time', models.TimeField(verbose_name='Время')),
                ('people', models.PositiveIntegerField(verbose_name='Количество людей')),
                ('message', models.TextField(max_length=400, verbose_name='Сообщение')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Book a table',
            },
        ),
        migrations.CreateModel(
            name='Breakfast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='breakfast/', verbose_name='Изображение')),
                ('title', models.CharField(max_length=120, verbose_name='Название блюда')),
                ('description', models.TextField(max_length=400, verbose_name='Ингридиенты')),
                ('price', models.PositiveIntegerField(default=100, verbose_name='Цена')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Menu Breakfast',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=120, verbose_name='ФИО')),
                ('email', models.EmailField(max_length=120, verbose_name='Email')),
                ('subject', models.CharField(max_length=120, verbose_name='Тема')),
                ('message', models.TextField(max_length=400, verbose_name='Сообщение')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
            },
        ),
        migrations.CreateModel(
            name='Dinner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='dinner/', verbose_name='Изображение')),
                ('title', models.CharField(max_length=120, verbose_name='Название блюда')),
                ('description', models.TextField(max_length=400, verbose_name='Ингридиенты')),
                ('price', models.PositiveIntegerField(default=100, verbose_name='Цена')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Menu Dinner',
            },
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='events/', verbose_name='Изображение')),
                ('title', models.CharField(max_length=120, verbose_name='Название блюда')),
                ('description', models.TextField(max_length=400, verbose_name='Ингридиенты')),
                ('price', models.PositiveIntegerField(default=100, verbose_name='Цена')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='gallery/', verbose_name='Изображение')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Gallery',
                'verbose_name_plural': 'Gallery',
            },
        ),
        migrations.CreateModel(
            name='Lunch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='lunch/', verbose_name='Изображение')),
                ('title', models.CharField(max_length=120, verbose_name='Название блюда')),
                ('description', models.TextField(max_length=400, verbose_name='Ингридиенты')),
                ('price', models.PositiveIntegerField(default=100, verbose_name='Цена')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Menu Lunch',
            },
        ),
        migrations.CreateModel(
            name='Starters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='starters/', verbose_name='Изображение')),
                ('title', models.CharField(max_length=120, verbose_name='Название блюда')),
                ('description', models.TextField(max_length=400, verbose_name='Ингридиенты')),
                ('price', models.PositiveIntegerField(default=100, verbose_name='Цена')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Menu Starters',
            },
        ),
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='testimonials/', verbose_name='Изображение')),
                ('first_name', models.CharField(max_length=120, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=120, verbose_name='Фамилия')),
                ('description', models.TextField(max_length=120, verbose_name='Тематика')),
                ('profession', models.CharField(max_length=120, verbose_name='Профессия')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Testimonial',
                'verbose_name_plural': 'Testimonials',
            },
        ),
    ]
