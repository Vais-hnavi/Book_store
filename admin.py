from django.contrib import admin
from .models import Book,Author
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    #readonly_fields=('slug',)
    prepopulated_fields={'slug':('title',)}

admin.site.register(Book,BookAdmin)
admin.site.register(Author)