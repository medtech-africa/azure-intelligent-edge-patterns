"""App API serializers.
"""

import logging

from rest_framework import serializers

from ..models import TrainingStatus

logger = logging.getLogger(__name__)


class TrainingStatusSerializer(serializers.ModelSerializer):
    """TrainingStatusSerializer."""

    class Meta:
        model = TrainingStatus
        fields = "__all__"
