from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=150)
    preview = models.ImageField(upload_to='course_previews/')
    description = models.TextField
    
    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        
    
    
class Lesson(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    preview = models.ImageField(upload_to='lesson_preview/')
    video_link = models.URLField()
    
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
        