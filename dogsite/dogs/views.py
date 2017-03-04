from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView, CreateView
from dogs.models import Dog


class DogCreateView(CreateView):
    template_name = 'dogs/dog_create.html'
    model = Dog
    fields = ['name', 'owner', 'photo']

    def get_success_url(self):
        return reverse('dogs:dog-success', kwargs={"dog": self.object.pk})


class DogListView(ListView):
    template_name = 'dog_list.html'
    model = Dog


class DogDetailView(DetailView):
    template_name = 'dogs/dog_detail.html'
    model = Dog


def index(request):
    object_list = Dog.objects.all()
    return render(request, 'dogs/index.html', {'object_list': object_list})


def success(request, dog=None):
    dog_object = Dog.objects.get(pk=dog)
    return render(request, 'dogs/success.html', {'dog': dog_object})


def search_form(request):
    return render(request, 'dogs/search_form.html')


def search(request):
    if 'q' in request.GET:
        q = request.GET['q']
        if q:
            dog_names = Dog.objects.filter(name__icontains=q)
            owner_names = Dog.objects.filter(owner__icontains=q)
        else:
            dog_names = None
            owner_names = None
        return render(request, 'dogs/search.html', {'dog_names': dog_names,
                                                    'owner_names': owner_names,
                                                    'query': q})
    else:
        message = 'Please submit a search term'
        return render(request, 'dogs/search_form', {'message': message})

    return render(request, 'dogs/search.html')
