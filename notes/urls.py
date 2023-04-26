from django.urls import path
from . import views

urlpatterns = [
    path('notes/',views.NotesListView.as_view(),name='notes.list'),
    path('notes/new',views.NotesCreateView.as_view(),name='notes.new'),
    path('notes/<str:pk>',views.NotesDetailView.as_view(),name='notes.detail'),
]