from django.shortcuts import render
from App1.modelos import Familiar
import datetime

class Familiar_view:
    
    def autogenerar_listar_familiares(request):
        fm1 = Familiar.create('luana', 19, datetime.date(2003, 5, 17))
        fm2 = Familiar.create('leandro', 89, datetime.date(1933, 5, 30))
        fm3 = Familiar.create('mbappe', 23, datetime.date(1999, 6, 20))
        
        fm1.save()
        fm2.save()
        fm3.save()

        
        return render(request, 'autogenerar_listar_familiares.html', {'familiares': [fm1, fm2, fm3]})

