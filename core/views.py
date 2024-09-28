from django.shortcuts import render
from .forms import RastarantForm


# Create your views here.
def index(request):
  if request.method == 'POST':
    form = RastarantForm(request.POST or None)
    if form.is_valid():
      # form.save()
      print(form.cleaned_data)
    else:
      return render(request, 'core/index.html', {'form': form})

  context = {'form': RastarantForm()}
  return render(request, 'core/index.html', context)
