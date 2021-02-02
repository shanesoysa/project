from django.contrib import admin
from .models import AllRecords,Wolinktable,Comments,ItemMaster,ProductionSchedule

# Register your models here.


admin.site.register(AllRecords)
admin.site.register(Comments)
admin.site.register(ItemMaster)
admin.site.register(ProductionSchedule)
admin.site.register(Wolinktable)
