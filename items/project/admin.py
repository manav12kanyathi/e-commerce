from django.contrib import admin

# Register your models here.
from . models import descri,createacc,wish,cart,checkout
class curs(admin.ModelAdmin):
    list_display = ('photo','product_name','product_price','product_descrition')
admin.site.register(descri,curs)
admin.site.register(createacc)
admin.site.register(wish)
admin.site.register(cart)
admin.site.register(checkout)