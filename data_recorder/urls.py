from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_data, name='db-form'), # "views.home" means that the "home" method is referenced from the views.py script
                                            # the '' means that we should see the result on the 
                                            # homepage path with what is defined in:
                                            # J_And_B_webapp\urls.py
    path('about/', views.about, name='about-home'),
    path('home/', views.home, name='data-home'),
]
