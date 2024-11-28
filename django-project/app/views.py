from django.views.generic import TemplateView

from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from .data import RECIPE


class IndexView(TemplateView):
    template_name = 'app/index.html'


class GoodsView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'app/goods.html'
    serializer_class = GoodSerializer
    queryset = Good.objects.all()

    def get(self, request, *args, **kwargs):
        return Response(data={'data': RECIPE})
