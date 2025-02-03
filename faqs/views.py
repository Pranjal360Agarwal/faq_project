from rest_framework.response import Response
from rest_framework import status, generics
from django.shortcuts import get_object_or_404
from .models import FAQ
from .serializers import FAQSerializer


class FAQListCreateView(generics.ListCreateAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    def get(self, request, *args, **kwargs):
        lang = request.GET.get("lang", "en")
        faqs = FAQ.objects.filter(language="en")
        data = [faq.get_translation(lang) for faq in faqs]
        return Response(data, status=status.HTTP_200_OK)
