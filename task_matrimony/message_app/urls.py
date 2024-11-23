from django.urls import path
from .views import MessageCrudOperation, GetMessagesByReceiver


urlpatterns=[
    path('message/', MessageCrudOperation.as_view(), name='messages'),
    path('new_message/<str:receiver_id>/', GetMessagesByReceiver.as_view(), name='get_messages_by_receiver'),


]