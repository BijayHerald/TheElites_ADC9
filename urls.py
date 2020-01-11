from django.conf.urls import url
from . import views
from django.urls import path
from .views import *
from django.conf import settings 
from django.conf.urls.static import static 


app_name = 'mobile_store'

urlpatterns = [

	path('mobile/', index_page),
	path('mobile/form', view_add_product_form),

	path('mobile/save', product_image_view, name = 'image_upload'), 
	path('mobile/search/',product_list_search),
	path('mobile/edit/<int:ID>', update_dataform),
	path('mobile/edit/Update/<int:ID>', update_data),
]
