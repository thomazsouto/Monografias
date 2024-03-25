from rest_framework import serializers

from .models import monografia

class monografiaSerializer(serializers.ModelSerializer):

    class Meta:
        model = monografia
        fields = ('id','titulo', 'autor', 'ano', 'orientador', 'resumo', 'link')