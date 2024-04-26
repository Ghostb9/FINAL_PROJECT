#######################
#####
##### URLs code that allows for the urls to be displayed 
#####
#######################


#imports needed functions
from django.urls import path
from .views import html_view, homepage_view, exhibits, about, moreinfo, play, feedback, submit_feedback
from django.conf import settings
from django.conf.urls.static import static

#url patterns for web app
urlpatterns = [
    path('exhibit/<int:pk>/', html_view, name='html_view'),
    path('', homepage_view, name='homepage_view'),  
    path('exhibits', exhibits, name='exhibits'),# Set as the root of the app
    path('play', play, name='play'),
    path('moreinfo', moreinfo, name='moreinfo'),
    path('about', about, name='about'),
    path('feedback', feedback, name='feedback'),
    path('submit_feedback/', submit_feedback, name='submit_feedback'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)