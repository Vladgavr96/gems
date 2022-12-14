import operator

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from .serializers import UploadedDataSerializer
import csv
import io
from .models import Deal
from django.db.models import Sum, F


class FileUploadAPIView(ViewSet):
    serializer_class = UploadedDataSerializer

    def create(self, request, *args, **kwargs):
        try:
            file = request.data['file_uploaded']
            decoded_file = file.read().decode()
            io_string = io.StringIO(decoded_file)
            reader = csv.reader(io_string)
            next(reader)
            for row in reader:
                Deal.objects.get_or_create(customer=row[0], item=row[1], total=row[2], quantity=row[3],
                                           deal_date=row[4])
            return Response('OK', status=status.HTTP_200_OK)
        except UnicodeDecodeError:
            return Response('Неверный тип файла', status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response('Непредвиденная ошибка', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request, *args, **kwargs):
        queryset = Deal.objects.values(username=F('customer')).annotate(spent_money=(Sum('total')))
        ordered_queryset = queryset.order_by('-spent_money')[:5]
        top5 = []
        top5_all_gems = []

        for i in ordered_queryset:
            top5.append(i)
            gems = Deal.objects.all().values('item').filter(customer=i['username']).distinct()
            for gem in gems:
                top5_all_gems.append(gem['item'])

        for i in top5:
            i.update({'gems': set()})
            gems = Deal.objects.all().values('item').filter(customer=i['username']).distinct()
            for gem in gems:
                count = 0
                for j in top5_all_gems:
                    if gem['item'] == j:
                        count += 1
                if count >= 2:
                    i['gems'].add(gem['item'])
        return Response(top5, status=status.HTTP_200_OK)
