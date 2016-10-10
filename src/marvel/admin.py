from django.contrib import admin
import marvel.models


class RoleInline(admin.TabularInline):
    model = marvel.models.Role


class CreatorAdmin(admin.ModelAdmin):
    inlines = (RoleInline,)


class ComicAdmin(admin.ModelAdmin):
    inlines = (RoleInline,)


admin.site.register(marvel.models.Character)
admin.site.register(marvel.models.Creator, CreatorAdmin)
admin.site.register(marvel.models.Comic, ComicAdmin)
admin.site.register(marvel.models.Event)
admin.site.register(marvel.models.Series)
