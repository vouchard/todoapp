from rest_framework import serializers
from todoitems.models import TodoItems,TodoComments
from todoitems.models import TodoItems

class TodoItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItems
        fields = '__all__'
    def to_internal_value(self, data):
        user =  self.context['request'].user
        data['user'] = user.id
        return super().to_internal_value(data)

class TodoCommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoComments
        fields = '__all__'
