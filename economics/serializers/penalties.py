from rest_framework import serializers

from economics.models import Penalty

__all__ = (
    'PenaltyCreateInputSerializer',
    'PenaltyCreateOutputSerializer',
    'PenaltyListOutputSerializer',
    'PenaltyListInputSerializer',
)


class PenaltyCreateInputSerializer(serializers.Serializer):
    shift_id = serializers.IntegerField()
    staff_id = serializers.IntegerField()
    reason = serializers.CharField(max_length=255)
    amount = serializers.IntegerField(
        min_value=0,
        allow_null=True,
        default=None,
    )


class PenaltyCreateOutputSerializer(serializers.ModelSerializer):
    shift_id = serializers.IntegerField()

    class Meta:
        model = Penalty
        fields = (
            'id',
            'shift_id',
            'staff',
            'reason',
            'amount',
            'consequence',
            'created_at',
        )
        depth = 1


class PenaltyListInputSerializer(serializers.Serializer):
    staff_ids = serializers.ListField(
        child=serializers.IntegerField(),
        default=None,
        allow_null=True,
        allow_empty=False,
    )
    limit = serializers.IntegerField(min_value=1, max_value=1000, default=10)
    offset = serializers.IntegerField(min_value=0, default=0)


class PenaltyListOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Penalty
        fields = (
            'id',
            'staff',
            'reason',
            'amount',
            'consequence',
            'created_at',
        )
        depth = 1
