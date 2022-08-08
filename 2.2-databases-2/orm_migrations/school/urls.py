from django.urls import path
from django.conf.urls import include
from django.conf import settings
from school.views import StudentListView

urlpatterns = [
    path('', StudentListView.as_view()),
]
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
