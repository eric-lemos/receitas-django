from django.shortcuts import get_object_or_404, render
from app.models import Receita

def index(request):
    receitas = Receita.objects.order_by('-data_receita').filter(publicada=True)
    dados = {'receitas': receitas}
    return render(request, 'index.html', dados)

def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    receita_item = {'receita': receita}
    return render(request, 'receita.html', receita_item)

def buscar(request):
    lista_receitas = Receita.objects.order_by('-data_receita').filter(publicada=True)

    if 'buscar' in request.GET:
        item_procurado = request.GET['buscar']
        lista_receitas = lista_receitas.filter(nome_receita__icontains=item_procurado)
    dados = {'receitas': lista_receitas}

    return render(request, 'buscar.html', dados)