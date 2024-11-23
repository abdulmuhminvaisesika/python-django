from django.urls import path



from .views import SubcriptionCrudOperation, SubcriptionCrudOperationWithSubcriptionType, SubcriptionList


urlpatterns= [
    path('subcription/', SubcriptionCrudOperation.as_view(), name='subcriptions'),
    path('subcription/<str:subcription_type>/', SubcriptionCrudOperationWithSubcriptionType.as_view(), name='subcriptions'),
    path('subcription_list/', SubcriptionList.as_view(), name='subcription_list')

]
