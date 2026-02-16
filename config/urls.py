from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from bots.views import BotViewSet, ScenarioViewSet, StepViewSet

router = DefaultRouter()
router.register(r"bots", BotViewSet, basename="bot")
router.register(r"scenarios", ScenarioViewSet, basename="scenario")
router.register(r"steps", StepViewSet, basename="step")

urlpatterns = [
    path("admin/", admin.site.urls),

    # Nested CRUD for steps inside a scenario
    path(
        "scenarios/<int:scenario_id>/steps/",
        StepViewSet.as_view({"get": "list", "post": "create"}),
        name="scenario-steps",
    ),
    path(
        "scenarios/<int:scenario_id>/steps/<int:pk>/",
        StepViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="scenario-step-detail",
    ),

    # Router CRUD endpoints
    path("", include(router.urls)),
]