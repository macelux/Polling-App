from django.contrib import admin

from .models import Question, Choice

admin.site.site_header ="pollster Admin"
admin.site.site_title ="pollster Admin Area"
admin.site.index_title ="Welcome to postal admin area"

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra =3 #how many extra fields do we want 

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            "fields": [
                'question_text'
            ],
        }),
        ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']})
    ]
    inlines = [ChoiceInline]
    

# admin.site.register(Question)
# admin.site.register(Choice)
admin.site.register(Question,QuestionAdmin)

