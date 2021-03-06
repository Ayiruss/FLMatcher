from rest_framework import viewsets
from imageupload_rest.serializer import UploadImageSerializer
from imageupload.models import UploadImage

class UploadImageViewSet(viewsets.ModelViewSet):
    queryset = UploadImage.objects.all()
    serializer_class = UploadImageSerializer
