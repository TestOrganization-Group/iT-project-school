from django.db import models


class SelectionCourse(models.Model):  #выбор курса
    name_course = models.CharField(max_length=50, db_index=True, verbose_name='Название Курсов')

    class Meta:
        verbose_name_plural = 'Выбор курса'
        verbose_name = 'Выбор кусров'


class Course(models.Model):  #Сам курс
    title = models.CharField(max_length=50, db_index=True, verbose_name='Название')
    price = models.FloatField(verbose_name='Цена')
    language = models.CharField(max_length=30, db_index=True, verbose_name='Язык')
    duration = models.CharField(max_length=50, verbose_name='Длительность')
    content = models.ForeignKey('CourseOutline', null=True, blank=True, on_delete=models.PROTECT, verbose_name= 'Описание')
    teacher = models.ForeignKey('Teacher', max_length=30, db_index=True, on_delete=models.PROTECT, verbose_name= 'Преподаватель')
    requirement = models.TextField(null=True, blank=True, verbose_name='Требование к курсу')
    sale = models.IntegerField(default=0, verbose_name='Скидка в %')
    feedback = models.ForeignKey('Feedback', null=True, on_delete=models.PROTECT, verbose_name='Отзывы')
    updated = models.DateTimeField(auto_now_add=True, verbose_name='Изменено')
    img = models.ImageField(upload_to='images/',
                            height_field=100, width_field=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Курсы'
        verbose_name = 'Курс'
        ordering = ['feedback__rate']


class CourseOutline(models.Model): #Программа курса
    introduction = models.TextField(null=True, blank=True, verbose_name='Введение')
    body = models.TextField(null=True, blank=True, verbose_name='Описание ')
    additional_information = models.TextField(null=True, blank=True, verbose_name='Дополнительная информация ')

    class Meta:
        verbose_name_plural = 'Программа курса'
        verbose_name = 'Программы кусров'


class Video(models.Model): #Видео курсы
    title = models.CharField(max_length=50, verbose_name='Название')
    order_number = models.IntegerField(verbose_name='Порядковый номер')
    link = models.TextField(verbose_name='Название')
    published = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Видео'
        verbose_name = 'Видео'
        ordering = ['order_number']


class Feedback(models.Model): #Отзывы
    name = models.CharField(max_length=30, verbose_name='Имя ')
    content = models.TextField(verbose_name='Описание')
    rate = models.IntegerField(verbose_name='Оценка')
    published = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')

    class Meta:
        verbose_name_plural = 'Отзывы'
        verbose_name = 'Отзыв'
        ordering = ['-published']


class Teacher(models.Model): #Препод
    first_name = models.CharField(max_length=30, verbose_name='Имя преподавателя')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия преподавателя')
    experience = models.TextField(max_length=150, verbose_name='Опыт')

    def __str__(self):
        return self.last_name

    class Meta:
        verbose_name_plural = 'Преподаватель '
        verbose_name = 'Преподаватели'
