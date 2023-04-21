from rest_framework import generics

from .models import Post
from .serializers import PostSerializer
from .permissions import IsAuthorOrStaffOrReadOnly


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrStaffOrReadOnly,]


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrStaffOrReadOnly,]
