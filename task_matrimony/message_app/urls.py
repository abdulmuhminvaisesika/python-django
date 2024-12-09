from django.urls import path
from .views import MessageCrudOperation, TotalMessagesOnReceiver, GetAllMessageHistoryOfTwoUsers


urlpatterns=[
    path('message/<str:receiver_id>/', MessageCrudOperation.as_view(), name='messages'),
    path('total_messages/', TotalMessagesOnReceiver.as_view(), name='get_messages_by_receiver'),
    path('all_messages/<str:receiver_id>/', GetAllMessageHistoryOfTwoUsers.as_view(), name='get_all_messages')


]