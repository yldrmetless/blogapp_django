from rest_framework import serializers
from .models import Category, Post, Comment

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class PostSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    category = serializers.ListField(
        write_only=True,
        child=serializers.CharField()
    )
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'categories', 'category', 'created_at', 'updated_at']

    def create(self, validated_data):
        category_names = validated_data.pop('category', [])
        post = Post.objects.create(**validated_data)
        categories = Category.objects.filter(name__in=category_names)
        post.categories.set(categories)
        return post
    
    def update(self, instance, validated_data):
        category_names = validated_data.pop('category', [])
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        categories = Category.objects.filter(name__in=category_names)
        instance.categories.set(categories)
        return instance

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'content', 'created_at']

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)
