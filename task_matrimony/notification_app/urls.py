from django.urls import path


from .views import NotificationCrudOperation, GetNotificationByReceiver, UnreadNotificationCount


urlpatterns = [
    path('notification/', NotificationCrudOperation.as_view(), name='notifications'),
    path('new_notification/', GetNotificationByReceiver.as_view(), name='notifications_by_receiver'),
    path('unreadnotifications/', UnreadNotificationCount.as_view(), name='unread_notifications')
]
