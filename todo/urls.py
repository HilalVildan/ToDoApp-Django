from django.urls import path, include
from .views import (
        home,
        todo_list_create,
        todo_get_del_upd,
        Todos,
        TodoDetail,
        TodoMVS
        )



from rest_framework import routers

router = routers.DefaultRouter()
router.register('todo', TodoMVS)

urlpatterns = [
        path('', home),

        #fbv urls(functionbase)
        path('todos/', todo_list_create),
        path('todos/<int:pk>/', todo_get_del_upd),
        
        #cbv urls (classbase)       
        path('todo_cls/', Todos.as_view()),
        path('todo_cls/<int:pk>/', TodoDetail.as_view()),

       path('', include(router.urls))
]