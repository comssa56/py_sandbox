from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField

from .models import Memo, Tips

import logging

class TipsSerializer(serializers.ModelSerializer):
    class Meta:
        model= Tips
#        fields = ('memo', 'tips_text')
        fields = ('id', 'tips_text')

class MemoSerializer(serializers.ModelSerializer):
    tips = SerializerMethodField()
    class Meta:
        model = Memo
        fields = ['id', 'memo_text', 'tips']

    def get_tips(self, obj):
        try:
            memo = Memo.objects.get(id=obj.id)
            tips = TipsSerializer(Tips.objects.all().filter(memo = memo), many=True).data
            return tips
        except:
            return None




