from rest_framework import viewsets
from rest_framework import permissions
from .models import Category, Post, Comment
from .serializers import CategorySerializer, PostSerializer, CommentSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return [permissions.AllowAny()]
        return [IsAuthenticated()]

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return [IsAuthenticated()]
        return [AllowAny()]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        user = self.request.user
        queryset = Post.objects.all()

        category_name = self.request.query_params.get('category', None)
        if category_name:
            categories = Category.objects.filter(name=category_name)
            queryset = queryset.filter(categories__in=categories)
            
        if user.is_authenticated:
            queryset = queryset.filter(author=user)

        return queryset

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        if post_id:
            return Comment.objects.filter(post_id=post_id)
        return Comment.objects.all()

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        try:
            post = Post.objects.get(id=post_id)
            serializer.save(author=self.request.user, post=post)
        except Post.DoesNotExist:
            raise Response({"detail": "Post not found."}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request, *args, **kwargs):
        post_id = self.kwargs.get('post_id')
        data = {
            'content': request.data.get('content')
        }
        serializer = self.get_serializer(data={**data, 'post': post_id})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)