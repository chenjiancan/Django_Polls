from django.contrib import admin

# Register your models here.

from .models import Question, Choice


# class ChoiceInline(admin.StackedInline):  # 堆叠方式
class ChoiceInline(admin.TabularInline):    # 横向表格
    model = Choice
    extra = 3  # 多3个空的


class QuestionAdmin(admin.ModelAdmin):
    # 设置显示格式，可折叠，分组
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline] # 关联选项Choice model

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)