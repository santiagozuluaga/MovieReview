from rest_framework import routers
from .views import UserViewSet, MovieViewSet, SerieViewSet, CommentViewSet

router = routers.SimpleRouter()
router.register(r'user',UserViewSet)
router.register(r'movie',MovieViewSet)
router.register(r'serie',SerieViewSet)
router.register(r'comment',CommentViewSet)
