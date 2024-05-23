from django.urls import path
from .import views





urlpatterns = [

    path('home/',views.home_page),
    path('addp/',views.product_add),
    path('book/', views.book_event),
    # path('book/(?P<pk>\w+)/', views.book_event),
    # path('confirmation/', views.confirmation, name='confirmation'),
    path('log/',views.user_log , name='login_data')  
    
]
