from django.urls import path

from seva_app import views, api_views

urlpatterns = [
    path('', views.login_view, name='login_view'),
    path('logout_view', views.logout_view, name='logout_view'),
    path('home', views.home, name='home'),
    path('officer_add', views.officer_add, name='officer_add'),
    path('staff_add', views.tstaff_add, name='staff_add'),
    path('officer_view', views.officer_view, name='officer_view'),
    path('update_officer/<int:id>/', views.officer_edit, name='update_officer'),
    path('delete_officer/<int:id>/', views.delete_officer, name='delete_officer'),
    path('staff_view', views.staff_view, name='staff_view'),
    path('sent_notification', views.sentnotification, name='sent_notification'),
    path('view_notification', views.viewnotification, name='view_notification'),
    path('delete_notification/<int:id>/', views.delete_notification, name='delete_notification'),
    path('staff_edit/<int:id>/', views.staff_edit, name='staff_edit'),
    path('staff_delete/<int:id>/', views.staff_delete, name='staff_delete'),
    path('feedback_view', views.feedback_view, name='feedback_view'),

    path('farmer_reg', api_views.farmer_reg, name='farmer_reg'),
    path('login_view_api', api_views.login_view_api, name='login_view_api'),
    path('market_ADD', api_views.Market_api.as_view(),name='market_ADD'),

]
