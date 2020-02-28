from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'app'

urlpatterns = [
	url(r'^$', views.view_calendar, name='view_calendar'),
	url(r'^profile/$', views.profile, name='profile'),
	url(r'^blank/$', views.get_excursion_form, name='get_excursion_form'),
	url(r'^send_application/$', views.send_application, name='send_application'),
	url(r'^get_all_areas/$', views.get_all_areas_by_facility_id, name='get_all_areas_by_facility_id'),
	url(r'^get_selected_areas/$', views.get_selected_areas_by_excursion_id, name='get_selected_areas_by_excursion_id'),
	url(r'^schedule/$', views.view_excursions, name='view_excursions'),
	url(r'^schedule/get_excursion/(\d+)/$', views.get_excursion),
	url(r'^schedule/get_excursion/(\d+)/change_confirmed/$', views.change_confirmed),
	url(r'^schedule/get_excursion/(\d+)/mark_as_not_held/$', views.mark_as_not_held),
	url(r'^schedule/get_excursion/(\d+)/send_message/(\d+)/$', views.send_message),
	url(r'^change_excursion/(\d+)/$', views.change_excursion, name='change_excursion'),
	url(r'^schedule/get_excursion/(\d+)/create_chat/(\d+)/$', views.create_chat),
	url(r'^facilities/', views.view_facilities_attendace, name='view_facilities_attendace'),
	url(r'^areas/', views.view_areas_attendace, name='view_areas_attendace'),
	url(r'^guides/', views.view_guide_statistics, name='view_guide_statistics'),
	url(r'^get_guide_statistics/', views.get_guide_statistics, name='get_guide_statistics'),
	url(r'^calendar/', views.view_calendar, name='view_calendar'),
	url(r'^get_excursions_to_calendar/', views.get_excursions_to_calendar, name='get_excursions_to_calendar')
]
