# REDIRECCIONAR
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

# CRUD
from django.views.generic import CreateView, View
from django.views.generic.list import ListView
from django.db.models import Q
from django.db import transaction

# MODELOS
from .models import Invoice, DetailInvoice
from apps.products.models import Product
from apps.customers.models import Customer

# FORMULARIOS
from .forms import InvoiceForm

# JSON
import json
from django.http import JsonResponse

# Decorador
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# BREADCRUMB
from .utils import breadcrumb

# GENERADOR
from .generador import ArchivoFacturas as archivo

# PDF
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders

# SETTINGS OF PROJECT
from project_archivos.settings import MEDIA_URL, STATIC_URL,MEDIA_ROOT,STATIC_ROOT
from django.conf import settings

# Create your views here.


###-- CREACION DE FACTURAS --###
class CreateInvoice(CreateView):
    model = Invoice
    form_class = InvoiceForm
    template_name = 'invoices/create.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_products':
                data = []
                prods = Product.objects.filter(title__icontains=request.POST['term'])[0:10]
                for i in prods:
                    item = i.toJSON()
                    item['value'] = i.title
                    item['text'] = i.title
                    data.append(item)
            elif action == 'add':
               
                with transaction.atomic():
                    
                    vents = json.loads(request.POST['vents'])
                    

                    cliente = vents['customer']
                    fecha = vents['created_at']
                    subtotal = float(vents['subtotal'])
                    iva = float(vents['iva'])
                    total = float(vents['total'])
                    cl = get_object_or_404(Customer,id = cliente)
                    

                    invoice = Invoice()
                    invoice.customer = cl
                    invoice.created_at = fecha
                    invoice.subtotal = subtotal
                    invoice.iva = iva
                    invoice.total = total                  
                    
                    invoice.save()

                    for i in vents['products']:
                        fact = invoice.id
                        fact_id = get_object_or_404(Invoice,id = fact)

                        prodcuto = i['id']
                        prod_id = get_object_or_404(Product,id = prodcuto)

                        cantidad = int(i['quantity'])
                        precio = float(i['price'])
                        d_subtotal = float(i['subtotal'])

                        detail = DetailInvoice(invoice=fact_id, product=prod_id,quantity=cantidad,price=precio,subtotal=d_subtotal)
                        detail.save()

            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Nueva Factura'
        context['action'] = 'add'
        context['message'] = 'Nueva Factura'
        context['det'] = []
        context['factura'] = True

        return context
    success_url = reverse_lazy('invoices:list')


###-- ENLISTAR FACTURAS --###
class ListInvoice(ListView):

    template_name = 'invoices/list.html'
    queryset = Invoice.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        archivo.subir(Invoice,DetailInvoice)

        context = super().get_context_data(**kwargs)
        context['title'] = 'FACTURAS'
        context['message'] = 'Listado de Facturas'
        context['breadcrumb'] = breadcrumb()
        return context


###-- DETALLES DE UNA FACTURA --###
def detailInvoice(request, pk):
    invoices = Invoice.objects.get(pk=pk)
    filtro = DetailInvoice.objects.filter(Q(invoice=pk))
    context ={
        'invoice':invoices,
        'title': 'Detalle de la factura',
        'detailinvoice_list': filtro


    }
    return render(request, 'invoices/detail.html', context)


###-- ELIMINACION DE ALGUNA FACTURAS --###
def deleteInvoice(request,pk):
    if request.user.is_superuser:
        invoice = get_object_or_404(Invoice, pk=pk)
        if invoice:
            invoice.delete()
        return redirect('invoices:list')

    else:
        return redirect('index')


###-- CREACION DE PDFS PARA ALGUNA FACTURA --###
class InvoicePDF(View):
    template_name = 'invoices/pdf.html'
    def link_callback(self,uri, rel):
            """
            Convert HTML URIs to absolute system paths so xhtml2pdf can access those
            resources
            """
            result = finders.find(uri)
            if result:
                    if not isinstance(result, (list, tuple)):
                            result = [result]
                    result = list(os.path.realpath(path) for path in result)
                    path=result[0]
            else:
                    sUrl = settings.STATIC_URL        # Typically /static/
                    sRoot = settings.STATIC_ROOT      # Typically /home/userX/project_static/
                    mUrl = settings.MEDIA_URL         # Typically /media/
                    mRoot = settings.MEDIA_ROOT       # Typically /home/userX/project_static/media/

                    if uri.startswith(mUrl):
                            path = os.path.join(mRoot, uri.replace(mUrl, ""))
                    elif uri.startswith(sUrl):
                            path = os.path.join(sRoot, uri.replace(sUrl, ""))
                    else:
                            return uri

            # make sure that file exists
            if not os.path.isfile(path):
                    raise Exception(
                            'media URI must start with %s or %s' % (sUrl, mUrl)
                    )
            return path

    def get(self, request, *args, **kwargs):
        try:
            template = get_template(self.template_name)
            context = {
                'invoice': Invoice.objects.get(pk = self.kwargs['pk']),
                'detailinvoice_list': DetailInvoice.objects.filter(Q(invoice=self.kwargs['pk']))
            }
            html = template.render(context)
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="Factura.pdf"'
            pisa_status = pisa.CreatePDF(
            html, dest=response, link_callback=self.link_callback)

            return response
        except:
            pass
        return HttpResponseRedirect(reverse_lazy('invoices:list'))
