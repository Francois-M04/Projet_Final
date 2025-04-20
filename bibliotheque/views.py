from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib import messages
from .forms import LivreForm
from .forms import SignUpForm
from .models import Livre

def signup(request) :
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('liste_livres') 
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form':form})

def liste_livres(request):
    query = request.GET.get('q')  
    if query:
        livres = Livre.objects.filter(titre__icontains=query).order_by('-date_ajout')
    else:
        livres = Livre.objects.all().order_by('-date_ajout')
    return render(request, 'bibliotheque/liste_livres.html', {'livres': livres})

@login_required
def livre_create(request):
    if request.method == 'POST':
        form = LivreForm(request.POST)
        if form.is_valid():
            livre = form.save(commit=False)
            livre.ajout_par = request.user
            livre.save()
            messages.success(request, "Votre livre a été créé avec succès !")
            return redirect('liste_livres')
        else:
            messages.error(request,"Erreur dans votre livre")
    else:
        form = LivreForm()
    return render(request, 'bibliotheque/livre_form.html', {'form': form})

def livre_detail(request, pk):
    livre = get_object_or_404(Livre, pk=pk)
    return render(request, 'bibliotheque/livre_detail.html', {'livre': livre})

@login_required
def livre_update(request, pk):
    livre = get_object_or_404(Livre, pk=pk)
    if livre.ajout_par != request.user:
        messages.error(request, "Vous n'êtes pas éligible à modifier ce livre.")
        return redirect('liste_livres') 
    if request.method == 'POST':
        form = LivreForm(request.POST, instance=livre)
        if form.is_valid():
            form.save() 
            messages.success(request, "Le livre a été modifié avec succès.") 
            return redirect('livre_detail', pk=livre.pk)  
    else:
        form = LivreForm(instance=livre)
    return render(request, 'bibliotheque/livre_form.html', {'form': form})

@login_required
def livre_delete(request, pk):
    livre = get_object_or_404(Livre, pk=pk)
    if livre.ajout_par != request.user:
        messages.error(request, "Vous n'êtes pas autorisé à supprimer ce livre.")
        return redirect('detail_livre', pk=pk)

    if request.method == 'POST':
        livre.delete()
        messages.success(request, "Le livre a été supprimé avec succès.")
        return redirect('liste_livres')

    return render(request, 'bibliotheque/livre_confirm_delete.html', {'livre': livre})

# Create your views here.
