from django.urls import path

from .views import ManagerSignupView,ManagerLoginView
from .views import EmployeeListView,AddEmployeeView,UpdateEmployeeView,DeleteEmployeeView

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Manager Employee Assignment API DOCUMENTATION",
        default_version='v1',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns=[
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('register/',ManagerSignupView.as_view()),
    path('login/',ManagerLoginView.as_view()),
    path('getEmployees/',EmployeeListView.as_view()),
    path('addEmployee/',AddEmployeeView.as_view()),
    path('updateEmployee/',UpdateEmployeeView.as_view()),
    path('deleteEmployee/<str:pk>/', DeleteEmployeeView.as_view())
]
