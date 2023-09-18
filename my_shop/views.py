from django.shortcuts import render
from django.views.generic import ListView
from .models import Client, Order

class YearProducts(ListView):
    template_name = 'my_shop/yearly_orders.html'
    context_object_name = 'orders'

    def get_queryset(self):
        client = Client.objects.get(pk=self.kwargs['pk'])
        orders = Order.objects.filter(client=client).order_by('-order_date')
        return orders

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['client'] = Client.objects.get(pk=self.kwargs['pk'])
        return context


class MonthProducts(ListView):
    template_name = 'my_shop/monthly_orders.html'
    context_object_name = 'orders'

    def get_queryset(self):
        client = Client.objects.get(pk=self.kwargs['pk'])
        year = self.kwargs['year']
        month = self.kwargs['month']
        orders = Order.objects.filter(client=client, order_date__year=year, order_date__month=month).order_by('-order_date')
        return orders

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['client'] = Client.objects.get(pk=self.kwargs['pk'])
        return context


class WeekProducts(ListView):
    template_name = 'my_shop/weekly_orders.html'
    context_object_name = 'orders'

    def get_queryset(self):
        client = Client.objects.get(pk=self.kwargs['pk'])
        year = self.kwargs['year']
        week = self.kwargs['week']
        orders = Order.objects.filter(client=client, order_date__year=year, order_date__week=week).order_by('-order_date')
        return orders

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['client'] = Client.objects.get(pk=self.kwargs['pk'])
        return context
