# Generated by Django 4.1.4 on 2022-12-22 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=40, verbose_name='Название')),
                ('Age', models.CharField(choices=[('Junior', 'Младшая'), ('Meduim', 'Средняя'), ('Adults', 'Взрослая')], max_length=10, verbose_name='Возраст')),
                ('Year_of_study', models.PositiveIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6')], verbose_name='Год обучения')),
                ('Created', models.DateTimeField(auto_now_add=True, verbose_name='Группа создалась')),
            ],
            options={
                'verbose_name': 'Группы',
                'verbose_name_plural': 'Группы',
            },
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=60, verbose_name='Название')),
                ('Number_of_classes', models.PositiveIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], verbose_name='Количество занятий')),
                ('Files_to_download', models.CharField(blank=True, max_length=255, verbose_name='Файлы для скачивания')),
            ],
            options={
                'verbose_name': 'Модули',
                'verbose_name_plural': 'Модули',
            },
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Surname', models.CharField(max_length=40, verbose_name='Фамилия')),
                ('Name', models.CharField(max_length=40, verbose_name='Имя')),
                ('Patronymic', models.CharField(max_length=40, verbose_name='Отчество')),
                ('Telephone', models.CharField(max_length=20, verbose_name='Номер телефона')),
                ('Email', models.CharField(max_length=30, verbose_name='Электронная почта')),
                ('Social_network', models.CharField(blank=True, max_length=150, verbose_name='Социальная сеть')),
                ('Login', models.CharField(max_length=30, verbose_name='Логин')),
                ('Password', models.CharField(max_length=30, verbose_name='Пароль')),
            ],
            options={
                'verbose_name': 'Родители',
                'verbose_name_plural': 'Родители',
            },
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Address', models.CharField(max_length=255, verbose_name='Адрес')),
                ('Name_School', models.CharField(max_length=30, verbose_name='Название школы')),
                ('Telephone', models.CharField(max_length=20, verbose_name='Номер телефона')),
                ('Email', models.CharField(max_length=30, verbose_name='Электронная почта')),
                ('Working_days', models.CharField(choices=[('SS', 'Сб-Вс'), ('MTWTF', 'Пн-Вт-Ср-Чт-Пт')], default='SS', max_length=7, verbose_name='Дни работы')),
                ('Working_time', models.CharField(choices=[('Earlier', '10:00-18:00'), ('Later', '11:00-19:00')], default='Earlier', max_length=10, verbose_name='Время работы')),
            ],
            options={
                'verbose_name': 'Школы',
                'verbose_name_plural': 'Школы',
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Surname', models.CharField(max_length=40, verbose_name='Фамилия')),
                ('Name', models.CharField(max_length=40, verbose_name='Имя')),
                ('Patronymic', models.CharField(max_length=40, verbose_name='Отчество')),
                ('Date_of_birth', models.DateField(auto_now_add=True, verbose_name='Дата рождения')),
                ('Post', models.CharField(choices=[('T', 'Тьютор'), ('A', 'Ассистент'), ('I', 'Стажёр')], default='I', max_length=2, verbose_name='Должность')),
                ('Telephone', models.CharField(max_length=20, verbose_name='Номер телефона')),
                ('Email', models.CharField(max_length=30, verbose_name='Электронная почта')),
                ('Login', models.CharField(max_length=30, verbose_name='Логин')),
                ('Password', models.CharField(max_length=30, verbose_name='Пароль')),
            ],
            options={
                'verbose_name': 'Сотрудники',
                'verbose_name_plural': 'Сотрудники',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Surname', models.CharField(max_length=40, verbose_name='Фамилия')),
                ('Name', models.CharField(max_length=40, verbose_name='Имя')),
                ('Patronymic', models.CharField(max_length=40, verbose_name='Отчество')),
                ('Date_of_birth', models.DateField(auto_now_add=True, verbose_name='Дата рождения')),
                ('Telephone', models.CharField(blank=True, max_length=20, verbose_name='Номер телефона')),
                ('Start_of_training', models.DateField(auto_now=True, verbose_name='Начало обучения')),
                ('Group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kiberdb.group')),
                ('Parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kiberdb.parent')),
            ],
            options={
                'verbose_name': 'Ученики',
                'verbose_name_plural': 'Ученики',
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateTimeField(verbose_name='Дата занятия')),
                ('Group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kiberdb.group')),
                ('Module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kiberdb.module')),
            ],
            options={
                'verbose_name': 'Расписание',
                'verbose_name_plural': 'Расписание',
            },
        ),
        migrations.AddField(
            model_name='group',
            name='School',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kiberdb.school'),
        ),
    ]