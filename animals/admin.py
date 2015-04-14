from django.contrib import admin

from animals.models import Animal, Breed, Pet


class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name', 'scientific_name',)
    search_fields = ('name', 'scientific_name',)
    ordering = ('name',)


class BreedAdmin(admin.ModelAdmin):
    list_display = ('name', 'animal',)
    search_fields = ('name',)
    list_filter = ('animal__name',)
    ordering = ('name',)


class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'animal', 'breed', 'birthday',)
    search_fields = ('name', 'birthday', 'breed__name', 'breed__animal__name')
    list_filter = ('breed__animal__name',)
    ordering = ('name',)

    def animal(self, obj):
        return obj.breed.animal
    animal.admin_order_field  = 'breed__animal'


admin.site.register(Animal, AnimalAdmin)
admin.site.register(Breed, BreedAdmin)
admin.site.register(Pet, PetAdmin)
