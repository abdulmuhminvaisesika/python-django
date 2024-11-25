from django.urls import path


from .views import NotificationCrudOperation, GetNotificationByReceiver


urlpatterns = [
    path('notification/', NotificationCrudOperation.as_view(), name='notifications'),
    path('new_notification/<str:receiver_id>/', GetNotificationByReceiver.as_view(), name='notifications_by_receiver')
]
