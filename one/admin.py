from django.contrib import admin
from one.models import User1

# Register your models here.


class User1Admin(admin.ModelAdmin):

    search_fields=['full_name','last_name','email','mobile_no']
    list_filter=['full_name','last_name','email','mobile_no']


admin.site.register(User1,User1Admin)
