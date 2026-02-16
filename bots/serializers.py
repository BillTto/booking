from rest_framework import serializers

from .models import Bot, Scenario, Step


class BotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bot
        fields = "__all__"


class ScenarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scenario
        fields = "__all__"


class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = "__all__"


class ScenarioRunInputSerializer(serializers.Serializer):
    """Payload for POST /scenarios/{id}/run/"""

    input = serializers.CharField(required=False, allow_blank=True, allow_null=True)