#Thaveesha Weerakkody 

from django.urls import path
from . import views  #Importing views from the same directory(assuming views.py)

#Namespace for the app,used to differentiate    URLs in templates
app_name = "store"

#URL pattern used for storing.
urlpatterns = [
    #Path for listing all stores,mapped to StoreCreateView.
    path(
        '',
        views.StoreCreateView.as_view(),
        name='list'),
    #Path for creating a new store,mapped to StoreCreativeView
    path(
        'create/',
        views.StoreCreateView.as_view(),
        name='create'),

    #Path for viewing details of  a specific store.
    path(
        '<pk>/details/',
        views.StoreDetailView.as_view(),
        name='details'),

    #Path for deleting a specific store, mapped to StoreDeleteView.    
    path(
        '<pk>/delete/',
        views.StoreDeleteView.as_view(),
        name='delete'),
]
