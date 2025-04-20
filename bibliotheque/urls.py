from django.urls import path
from .views import signup, livre_create, liste_livres, livre_detail, livre_update, livre_delete
from django.contrib.auth import views  as auth_views

urlpatterns = [
    path('inscription/', signup, name='signup'),
    path('', liste_livres, name='liste_livres'),
    path('livre/creer/', livre_create, name='creer_livre'),
    path('livre/<int:pk>/', livre_detail, name = 'livre_detail'),
    path('livre/<int:pk>/modifier', livre_update, name='livre_update'),
    path('livre/<int:pk>/supprimer/', livre_delete, name='supprimer_livre'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
