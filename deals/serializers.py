from rest_framework.serializers import Serializer, FileField, CharField, IntegerField, ListField


class UploadedDataSerializer(Serializer):
    file_uploaded = FileField()

    class Meta:
        fields = ['file_uploaded']


class TopCustomerSerializer(Serializer):
    username = CharField()
    spent_money = IntegerField()
    #gems = ListField()

    class Meta:
        fields = ['username', 'spent_money']
