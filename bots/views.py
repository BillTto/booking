from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Bot, Scenario, Step
from .serializers import (
    BotSerializer,
    ScenarioSerializer,
    StepSerializer,
    ScenarioRunInputSerializer,
)


class BotViewSet(viewsets.ModelViewSet):
    queryset = Bot.objects.all().order_by("id")
    serializer_class = BotSerializer


class ScenarioViewSet(viewsets.ModelViewSet):
    queryset = Scenario.objects.all().order_by("id")
    serializer_class = ScenarioSerializer

    @action(detail=True, methods=["get"], url_path="steps")
    def steps(self, request, pk=None):
        qs = Step.objects.filter(scenario_id=pk).order_by("order", "id")
        return Response(StepSerializer(qs, many=True).data)

    @action(detail=True, methods=["post"], url_path="run", serializer_class=ScenarioRunInputSerializer)
    def run(self, request, pk=None):
        serializer = ScenarioRunInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user_input = serializer.validated_data.get("input")

        steps_qs = Step.objects.filter(scenario_id=pk).order_by("order", "id")
        messages = [{"role": s.role, "content": s.content} for s in steps_qs]

        if user_input:
            messages.append({"role": "user", "content": user_input})

        return Response({"messages": messages})


class StepViewSet(viewsets.ModelViewSet):
    serializer_class = StepSerializer

    def get_queryset(self):
        qs = Step.objects.all()
        scenario_id = self.kwargs.get("scenario_id")
        if scenario_id is not None:
            qs = qs.filter(scenario_id=scenario_id)
        return qs.order_by("order", "id")

    def perform_create(self, serializer):
        scenario_id = self.kwargs.get("scenario_id")
        if scenario_id is not None:
            serializer.save(scenario_id=scenario_id)
        else:
            serializer.save()