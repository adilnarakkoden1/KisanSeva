from rest_framework import serializers

from seva_app.models import market


class MarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = market
        fields = ['name','type','quantity','location','phone','amount','image']