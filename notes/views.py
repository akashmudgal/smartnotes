from django.http import Http404
from django.shortcuts import render
from .models import Note
from django.views.generic import ListView,DetailView,CreateView
from .forms import NotesForm
class NotesCreateView(CreateView):
    model = Note
    form_class=NotesForm
    template_name = 'notes/notes_form.html'
    success_url = '/smart/notes'

class NotesListView(ListView):
    model = Note
    template_name='notes/notes_list.html'
    context_object_name='notes'

class NotesDetailView(DetailView):
    model= Note
    context_object_name= 'note'
    template_name='notes/notes_detail.html'