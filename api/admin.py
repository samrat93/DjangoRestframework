from django.contrib import admin
from api.models import Company, Employee, User

# Register your models here.


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('companyName', 'location', 'type')


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'address', 'position', 'company')


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'gender', 'state', 'pimage', 'docs')


admin.site.register(Company, CompanyAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(User, UserAdmin)
