from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

from .models import Entry
from .forms import Entryform


# Create your views here.

def base(request):
    entries = Entry.objects.order_by('-date_posted')
    context = {'entries': entries}
    return render(request, 'diary/base.html', context)


def store(request):
    if request.method == 'POST':
        form = Entryform(request.POST)

        if form.is_valid():
            form.save()
            return redirect('base')
    else:
        form = Entryform()

    context = {'form': form}

    return render(request, 'diary/str.html', context)


def draft_list(request):
    entries = Entry.objects.order_by('Entry #{}')
    return render(request, 'drafts.html', {'entries': entries})


class AuthorDelete(DeleteView):
    model = Entry
    success_url = reverse_lazy('text')


def delete_entry(request, pk):
    if request.method == "POST":
        if form.is_valid():
            entry = form.delete(commit=False)
            entry.delete()
            return redirect('deete.html', pk=product.pk)