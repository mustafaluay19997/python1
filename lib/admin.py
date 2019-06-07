from django.contrib import admin
from lib.models import BookMust
# Register your models here.


class BooksAdmin(admin.ModelAdmin):
    list_display = ('Book_Name', 'Auther_Name', 'Number_page',
                    'date_Publish', 'Publisher', 'Book_Pictuer', 'Book_File')



admin.site.register(BookMust, BooksAdmin)
