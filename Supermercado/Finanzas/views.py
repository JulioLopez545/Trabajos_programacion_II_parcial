from django.shortcuts import render
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.views import View
from .models import*
from .forms import*

class ObtenerFacturas(View):
    def get(self, request):
        facturas = Factura.objects.all()

        return render(request, 'facturas/listar_facturas.html',{'facturas': facturas})

class AgregarFacturas(View):
    def get(self,request):
        form = AddFacturaForm()
        

    
        return render(request, 'facturas/agregar_facturas.html',{'form':form})

    def post(self, request):
        form = AddFacturaForm(request.POST)

        if(form.is_valid()):
            obj = Factura()
            obj.client= form.cleaned_data['client']
            obj.rtn= form.cleaned_data['rtn']
      
            obj.save()

        return HttpResponseRedirect(reverse('listar_facturas'))       



class ActualizarFacturas(View):
    def get(self,request, uuid):
        producto= Factura.objects.get(uuid=uuid)
        form = UpdateFacturaForm(instance=producto)

        return render(request, 'facturas/agregar_facturas.html', {'form':form})
        
    def post(self, request, uuid):
            obj = Factura.objects.get(uuid=uuid)
            form= UpdateFacturaForm(request.POST, instance=obj)
            if(form.is_valid()):
                obj = form.save(commit=False)
                obj.save()
                return HttpResponseRedirect(reverse('listar_facturas'))

            
            return render(request, 'facturas/actualizar_facturas.html', {'form': form})
