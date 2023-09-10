from rest_framework import serializers

from skilluponline.models import CourseSubscription


class CourseSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseSubscription
        fields = ['subscribed']
