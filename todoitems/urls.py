from django.urls import path,include
from rest_framework import routers
from todoitems.views import TodoItemsView,TodoCommentsView
router = routers.DefaultRouter()
router.register(r'todoitems', TodoItemsView)
router.register(r'todocomments', TodoCommentsView)

urlpatterns = [
    path("",include(router.urls) ),
]
