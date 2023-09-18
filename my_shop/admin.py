from django.contrib import admin
from .models import Category, Product, Client, Order
from .forms import ProductForm

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug',]
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductForm
    list_display = ['name', 'slug', 'description', 'price', 'available', 'created', 'updated', ]
    list_filter = ['name', 'available', 'created', 'updated', ]
    list_editable = ['price', 'available',]
    prepopulated_fields = {'slug': ('name',)}
    def change_view(self, request, object_id, form_url='', extra_context=None):
        self.fields = ['id', 'name', 'slug', 'category', 'description', 'price', 'available', 'created', 'updated']
        return super(ProductAdmin, self).change_view(request, object_id, form_url, extra_context)

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'address', 'registration_date']
    list_filter = ['name', 'address', 'phone']
    list_editable = ['address']
    list_display_links = ['name']
    def change_view(self, request, object_id, form_url='', extra_context=None):
        self.fields = ['id', 'name', 'email', 'phone', 'address', 'registration_date']
        return super(ClientAdmin, self).change_view(request, object_id, form_url, extra_context)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['client', 'total_amount', 'order_date']
    def change_view(self, request, object_id, form_url='', extra_context=None):
        self.fields = ['id', 'client', 'product', 'total_amount', 'order_date']
        return super(OrderAdmin, self).change_view(request, object_id, form_url, extra_context)
