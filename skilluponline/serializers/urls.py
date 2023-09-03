from django.urls import path

urlpatterns = [
    path('', LessonListView.as_view()),
    path('', )
]

router = routers.SimpleRouter()
router.register('lesson', )