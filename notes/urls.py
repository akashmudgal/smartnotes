from django.urls import path
from . import views

urlpatterns = [
    path('notes/',views.NoteListView.as_view(),name='notes.list'),
    path('notes/new',views.NoteCreateView.as_view(),name='notes.new'),
    path('notes/<str:pk>',views.NoteDetailView.as_view(),name='notes.detail'),
    path('notes/<str:pk>/edit',views.NoteUpdateView.as_view(),name='notes.update'),
    path('notes/<str:pk>/delete',views.NoteDeleteView.as_view(),name='notes.delete'),
]
