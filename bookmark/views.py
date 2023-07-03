from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from bookmark.models import Bookmark
from mysite.views import OwnerOnlyMixin

# Create your views here.
class BookmarkLV(ListView):
    model = Bookmark

class BookmarkDV(DetailView):
    model = Bookmark

class BookmarkCreateView(LoginRequiredMixin, CreateView):
    pass

class BookmarkChangeLV(LoginRequiredMixin, ListView):
    pass

class BookmarkUpdateView(OwnerOnlyMixin, UpdateView):
    pass

class BookmarkDeleteView(OwnerOnlyMixin, DeleteView):
    pass