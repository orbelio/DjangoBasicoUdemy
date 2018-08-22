from django.shortcuts import render
from datetime import datetime

from .models import Transacao

def home(request):
    data = {}
    data['transacoes'] = ['t1', 't2', 't3']
    data['now'] = datetime.now()
    #html = "<html><body>Agora é %s.</body></html>" % now
    #return HttpResponse(html)
    return render(request, 'contas\home.html', data)

def listagem(request):
    data = {}
    data['transacoes'] = Transacao.objects.all()
    return render(request, 'contas\listagem.html', data)