from django.contrib import admin
import marvel.models


class CreatorComicInline(admin.TabularInline):
    model = marvel.models.CreatorComic
    # extra = 1


class CreatorEventInline(admin.TabularInline):
    model = marvel.models.CreatorEvent
    # extra = 1


class CreatorSeriesInline(admin.TabularInline):
    model = marvel.models.CreatorSeries
    # extra = 1


class SeriesEventInline(admin.TabularInline):
    model = marvel.models.SeriesEvent
    # extra = 1


class CharacterEventInline(admin.TabularInline):
    model = marvel.models.CharacterEvent
    # extra = 1


class CharacterSeriesInline(admin.TabularInline):
    model = marvel.models.CharacterSeries
    # extra = 1


class ComicEventInline(admin.TabularInline):
    model = marvel.models.ComicEvent
    # extra = 1


class ComicSeriesInline(admin.TabularInline):
    model = marvel.models.ComicSeries
    # extra = 1


class ComicCharacterInline(admin.TabularInline):
    model = marvel.models.ComicCharacter
    # extra = 1


class CharacterAdmin(admin.ModelAdmin):
    inlines = (
        ComicCharacterInline,
        CharacterSeriesInline,
        CharacterEventInline,
        )


class CreatorAdmin(admin.ModelAdmin):
    inlines = (
        CreatorSeriesInline,
        CreatorEventInline,
        CreatorComicInline,
        )


class ComicAdmin(admin.ModelAdmin):
    inlines = (
        ComicCharacterInline,
        ComicSeriesInline,
        ComicEventInline,
        CreatorComicInline,
        )


class EventAdmin(admin.ModelAdmin):
    inlines = (
        ComicEventInline,
        CharacterEventInline,
        SeriesEventInline,
        CreatorEventInline,
        )


class SeriesAdmin(admin.ModelAdmin):
    inlines = (
        CreatorSeriesInline,
        SeriesEventInline,
        CharacterSeriesInline,
        ComicSeriesInline,
        )


admin.site.register(marvel.models.Character, CharacterAdmin)
admin.site.register(marvel.models.Creator, CreatorAdmin)
admin.site.register(marvel.models.Comic, ComicAdmin)
admin.site.register(marvel.models.Event, EventAdmin)
admin.site.register(marvel.models.Series, SeriesAdmin)
