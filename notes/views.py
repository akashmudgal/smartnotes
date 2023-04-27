from django.shortcuts import render
from .models import Note
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .forms import NotesForm

class NoteCreateView(CreateView):
    model = Note
    form_class=NotesForm
    success_url = '/smart/notes'

class NoteUpdateView(UpdateView):
    model = Note
    form_class=NotesForm
    success_url = '/smart/notes'

class NoteDeleteView(DeleteView):
    model = Note
    success_url = '/smart/notes'
    context_object_name = 'note'

class NoteListView(ListView):
    model = Note
    context_object_name='notes'

class NoteDetailView(DetailView):
    model= Note
    context_object_name= 'note'