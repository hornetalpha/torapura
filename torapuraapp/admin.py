from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.formats import base_formats
from .models import Post
from .models import Plan

class PlanResource(resources.ModelResource):
    # Modelに対するdjango-import-exportの設定
    class Meta:
        model = Plan
        fields = ('id', 'place', 'done', 'person', 'day', 'plan_name', 'plan_detail', 'typeno')
        import_id_fields = ['id']

class PlanAdmin(ImportExportModelAdmin):
    # ImportExportModelAdminを利用するようにする
    list_display = ('place', 'done', 'person', 'day', 'plan_name', 'plan_detail', 'typeno')
    # django-import-exportsの設定
    resource_class = PlanResource
    formats = [base_formats.CSV]

admin.site.register(Post)
admin.site.register(Plan, PlanAdmin)
