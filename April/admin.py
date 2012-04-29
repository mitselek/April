from bubble.models import BubbleDefinition
from django.contrib import admin


class BubbleDefinitionAdmin(admin.ModelAdmin):
    fields = ['label', 'allowed_subbubbles']
admin.site.register(BubbleDefinition, BubbleDefinitionAdmin)

admin.site.register(Bubble)
admin.site.register(Relation)
admin.site.register(BubblePropertyDefinition)
admin.site.register(BubbleProperty)