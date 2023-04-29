from django.http import HttpResponseRedirect
from .models import Note
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .forms import NotesForm
from django.contrib.auth.mixins import LoginRequiredMixin

class NoteCreateView(LoginRequiredMixin,CreateView):
    model = Note
    form_class=NotesForm
    success_url = '/smart/notes'

    def form_valid(self, form):
        self.object=form.save(commit=False)
        self.object.user=self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class NoteUpdateView(LoginRequiredMixin,UpdateView):
    model = Note
    form_class=NotesForm
    success_url = '/smart/notes'

class NoteDeleteView(LoginRequiredMixin,DeleteView):
    model = Note
    success_url = '/smart/notes'
    context_object_name = 'note'

class NoteListView(LoginRequiredMixin,ListView):
    model = Note
    context_object_name='notes'
    login_url= '/login'

    def get_queryset(self):
        return self.request.user.notes.all()

class NoteDetailView(LoginRequiredMixin,DetailView):
    model= Note
    context_object_name= 'note'