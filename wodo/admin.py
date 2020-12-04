from django.contrib import admin

# Register your models here.
from wodo.models import *
# Register your models here.

admin.site.register(workers)
admin.site.register(transaction)
admin.site.register(hired)
admin.site.register(workRating)
admin.site.register(saved)
admin.site.register(filterCache)
admin.site.register(reportWorker)
admin.site.register(appUser)
admin.site.register(dutyDenials)