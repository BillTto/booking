from django.contrib import admin

from .models import Bot, Scenario, Step


@admin.register(Bot)
class BotAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at")
    search_fields = ("name",)


@admin.register(Scenario)
class ScenarioAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "bot", "is_active", "created_at")
    list_filter = ("is_active", "bot")
    search_fields = ("title",)


@admin.register(Step)
class StepAdmin(admin.ModelAdmin):
    list_display = ("id", "scenario", "order", "role")
    list_filter = ("role", "scenario")
    search_fields = ("content",)
    ordering = ("scenario", "order")
