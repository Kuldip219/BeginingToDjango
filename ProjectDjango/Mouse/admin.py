from django.contrib import admin
from .models import variety, ProjectReview, Project, ProjectDetail

# Register your models here.
class ProjectReviewInLine(admin.TabularInline):
    model = ProjectReview
    extra = 2

class varietyadmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'date_created']
    inlines = [ProjectReviewInLine]

class projectDetailadmin(admin.ModelAdmin):
    list_display = ['mice', 'detail_info', 'date_added']
    filter_horizontal = ['mice']

class projectadmin(admin.ModelAdmin):
    list_display = ['name', 'description']


admin.site.register(variety, varietyadmin)
admin.site.register(ProjectDetail, projectDetailadmin)
admin.site.register(Project, projectadmin)