import requests
from django.http import JsonResponse
from django.urls import reverse_lazy, reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator

# Create your views here.
from back import load_csv
from back.forms import CityForm, ChildFormset, TestForm
from back.load_csv import *
from back.models import City, Hotel


class CityList(ListView):
    model = City
    template_name = 'city/list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        load_csv_city()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = [{'id': '', 'text': '--------------'}]
        try:
            action = request.POST['action']
            if action == 'search_product_id':
                data = []
                for i in Hotel.objects.filter(categ_id=request.POST['id']):
                    data.append({'id': i.id, 'text': i.name, 'data': i.categ.toJSON()})
            elif action == 'autocomplete':
                data = []
                for i in City.objects.filter(name__icontains=request.POST['term'])[0:10]:
                    item = i.toJSON()
                    item['text'] = i.name
                    data.append(item)
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'City List'
        context['list_url'] = reverse_lazy('city_list')
        context['entity'] = 'City'
        return context


class CityCreate(CreateView):
    model = City
    form_class = CityForm
    template_name = "city/create.html"

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No value has been entered'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_success_url(self):
        return reverse("city_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create City'
        context['entity'] = 'City'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        print(context)
        return context


class CityUpdate(UpdateView):
    model = City
    form_class = TestForm
    template_name = 'city/create.html'
    success_url = reverse_lazy('city_list')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit City'
        context['entity'] = 'City'
        context['list_url'] = reverse_lazy('citylist')
        context['action'] = 'edit'
        return context


class CityDelete(DeleteView):
    model = City
    form_class = CityForm
    template_name = 'city/delete.html'
    success_url = reverse_lazy('city_list')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Delete City'
        context['entity'] = 'City'
        context['list_url'] = reverse_lazy('erp:product_list')
        return context
