from rest_framework import viewsets, mixins


class CreateListDestroyViewSet(viewsets.GenericViewSet,
                               mixins.CreateModelMixin,
                               mixins.ListModelMixin,
                               mixins.DestroyModelMixin):
    pass
