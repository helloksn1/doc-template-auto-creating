from django.urls import path

from . import views


urlpatterns = [
    path('', views.Index.as_view(), name='list'),
    path('detail/<int:pk>', views.PlaceHolderDetail.as_view(), name='detail'),
    # path('create/', views.PlaceHolderCreate.as_view(), name='create'),
    path('create/', views.PlaceHolderCreateNew, name='create'),
    # path('update/<int:pk>', views.PlaceHolderUpdate.as_view(), name='update'),
    path('update/<int:pk>', views.PlaceHolderUpdateNew, name='update'),
    path('delete/<int:pk>', views.PlaceHolderDelete.as_view(), name='delete'),
    path('docx/<int:pk>', views.GetDocx, name='docx'),
    path('docxlist', views.GetDocxList, name='docxlist'),
    path('login', views.UserLogin, name='login'),
    path('logout', views.UserLogout, name='logout'),
    path('register', views.UserRegister, name='register'),
    path('changepass', views.ChangePass, name='changepass')
]
