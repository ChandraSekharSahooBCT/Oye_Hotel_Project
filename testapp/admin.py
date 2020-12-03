from django.contrib import admin
from testapp.models import Prod
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
	list_display=['prodname','prodprice','prodimage','prodimage1','proddesc']
admin.site.register(Prod,ProductAdmin)


