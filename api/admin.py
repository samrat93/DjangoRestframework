from django.contrib import admin
from api.models import Company, Employee, User

# Register your models here.


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('companyName', 'location', 'type')


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'address', 'position', 'company')


admin.site.register(Company, CompanyAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(User)
