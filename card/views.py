from rest_framework import viewsets, generics, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from card.card import Card
from card.serializers import CardSerializer
from store.discount import Discount
from store.errors import handleError


class CardAPI(viewsets.ViewSet, generics.GenericAPIView):
    serializer_class = CardSerializer

    def __init__(self, *args, **kwargs):
        self.discount = Discount()
        super(CardAPI, self).__init__(*args, **kwargs)

    def retrieve(self, request, pk=None):
        pass

    def list(self, request):
        card_object = Card()
        return Response(self.get_serializer_class()(card_object.selectByUser(request.user),many = True).data)


    def create(self, request):
        pass

    @action(detail=False)
    def discount_validation(self, request):
        code = request.GET.get('code')
        if self.discount.validate(self.request.user, code=code):
            return Response({'status': True})

    def get_permissions(self):
        if self.action == 'list':
            self.permission_classes = [permissions.IsAuthenticated]
        return super(CardAPI, self).get_permissions()