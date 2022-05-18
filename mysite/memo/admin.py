from django.contrib import admin

from .models import Memo, Tips

class TipsInline(admin.StackedInline):
    model = Tips
    extra = 3

class MemoAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['memo_text']}),
        ('Date information', {'fields': ['insert_date'], 'classes': ['collapse']}),
    ]
    inlines = [TipsInline]

admin.site.register(Memo, MemoAdmin)
