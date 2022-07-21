from contextlib import nullcontext
from django.urls import path

from data_recorder import reportlab_script
from . import views, reportlab_script
#import .reportlab_script
from .reportlab_script import Report
from reportlab.lib.pagesizes import letter, A4, A3

urlpatterns = [
    path('', views.add_data, name='db-form'), # "views.home" means that the "home" method is referenced from the views.py script
                                            # the '' means that we should see the result on the 
                                            # homepage path with what is defined in:
                                            # J_And_B_webapp\urls.py
    path('about/', views.about, name='about-home'),
    path('home/', views.home, name='data-home'),
    # path('report_csv', views.report_csv, name='report_csv'),

  
    path('report_pdf', Report.generate, name='run_pdfgen'),
]
