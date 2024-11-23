from django.urls import path


from .views import NotificationCrudOperation, NotificationCrudOperationByType, GetNotificationByReceiver


urlpatterns = [
    path('notification/', NotificationCrudOperation.as_view(), name='notifications'),
    path('notification/<str:notification_type>/', NotificationCrudOperationByType.as_view(), name='notifications_by_type'),
    path('new_notification/<str:receiver_id>/', GetNotificationByReceiver.as_view(), name='notifications_by_receiver')
]
