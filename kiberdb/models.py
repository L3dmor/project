from django.db import models


class School(models.Model):
    WORKING_DAYS_CHOICES = [
        ('SS', 'Сб-Вс'),
        ('MTWTF', 'Пн-Вт-Ср-Чт-Пт')
    ]
    WORKING_TIME_CHOICES = [
        ('Earlier', '10:00-18:00'),
        ('Later', '11:00-19:00')
    ]
    Address = models.CharField('Адрес', max_length=255)
    Name_School = models.CharField('Название школы', max_length=30)
    Telephone = models.CharField('Номер телефона', max_length=20)
    Email = models.CharField('Электронная почта', max_length=30)
    Working_days = models.CharField('Дни работы', choices=WORKING_DAYS_CHOICES, max_length=7, default='SS')
    Working_time = models.CharField('Время работы', choices=WORKING_TIME_CHOICES, max_length=10, default='Earlier')

    def __str__(self):
        return f'{self.Name_School}'

    class Meta:
        verbose_name = "Школы"
        verbose_name_plural = "Школы"


class Staff(models.Model):
    POST_CHOICES = [
        ('T', 'Тьютор'),
        ('A', 'Ассистент'),
        ('I', 'Стажёр')
    ]
    Surname = models.CharField('Фамилия', max_length=40)
    Name = models.CharField('Имя', max_length=40)
    Patronymic = models.CharField('Отчество', max_length=40)
    Date_of_birth = models.DateField('Дата рождения', auto_now_add=True)
    Post = models.CharField('Должность', choices=POST_CHOICES, max_length=2, default='I')
    Telephone = models.CharField('Номер телефона', max_length=20)
    Email = models.CharField('Электронная почта', max_length=30)
    Login = models.CharField('Логин', max_length=30)
    Password = models.CharField('Пароль', max_length=30)

    def __str__(self):
        return f'{self.Surname} {self.Name} {self.Patronymic}'

    class Meta:
        verbose_name = "Сотрудники"
        verbose_name_plural = "Сотрудники"


class Group(models.Model):
    AGE_CHOICES = [
        ('Junior', 'Младшая'),
        ('Meduim', 'Средняя'),
        ('Adults', 'Взрослая')
    ]
    YOS_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6')
    ]
    Title = models.CharField('Название', max_length=40)
    Age = models.CharField('Возраст', choices=AGE_CHOICES, max_length=10)
    School = models.ForeignKey('School', on_delete=models.CASCADE)
    Year_of_study = models.PositiveIntegerField('Год обучения', choices=YOS_CHOICES)
    Created = models.DateTimeField('Группа создалась', auto_now_add=True)

    def __str__(self):
        return f'{self.Title}'

    class Meta:
        verbose_name = "Группы"
        verbose_name_plural = "Группы"


class Student(models.Model):
    Surname = models.CharField('Фамилия', max_length=40)
    Name = models.CharField('Имя', max_length=40)
    Patronymic = models.CharField('Отчество', max_length=40)
    Parent = models.ForeignKey('Parent', on_delete=models.CASCADE)
    Date_of_birth = models.DateField('Дата рождения', auto_now_add=True)
    Telephone = models.CharField('Номер телефона', max_length=20, blank=True)
    Group = models.ForeignKey('Group', on_delete=models.CASCADE)
    Start_of_training = models.DateField('Начало обучения', auto_now=True)

    def __str__(self):
        return f'{self.Surname} {self.Name} {self.Patronymic}'

    class Meta:
        verbose_name = "Ученики"
        verbose_name_plural = "Ученики"


class Parent(models.Model):
    Surname = models.CharField('Фамилия', max_length=40)
    Name = models.CharField('Имя', max_length=40)
    Patronymic = models.CharField('Отчество', max_length=40)
    Telephone = models.CharField('Номер телефона', max_length=20)
    Email = models.CharField('Электронная почта', max_length=30)
    Social_network = models.CharField('Социальная сеть', max_length=150, blank=True)
    Login = models.CharField('Логин', max_length=30)
    Password = models.CharField('Пароль', max_length=30)

    def __str__(self):
        return f'{self.Surname} {self.Name} {self.Patronymic}'

    class Meta:
        verbose_name = "Родители"
        verbose_name_plural = "Родители"


class Module(models.Model):
    NOC_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10')
    ]
    Title = models.CharField('Название', max_length=60)
    Number_of_classes = models.PositiveIntegerField('Количество занятий', choices=NOC_CHOICES)
    Files_to_download = models.CharField('Файлы для скачивания', max_length=255, blank=True)

    def __str__(self):
        return f'{self.Title}'

    class Meta:
        verbose_name = "Модули"
        verbose_name_plural = "Модули"


class Schedule(models.Model):
    Group = models.ForeignKey('Group', on_delete=models.CASCADE)
    Module = models.ForeignKey('Module', on_delete=models.CASCADE)
    Date = models.DateTimeField('Дата занятия')

    def __str__(self):
        return f'{self.Group} {self.Date}'

    class Meta:
        verbose_name = "Расписание"
        verbose_name_plural = "Расписание"
