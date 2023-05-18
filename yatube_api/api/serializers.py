from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from posts.models import User, Post, Group, Comment, Follow


class GroupSerializer(serializers.ModelSerializer):
    """Сереализатор групп."""

    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')


class PostSerializer(serializers.ModelSerializer):
    """Сереализатор постов."""

    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        model = Post
        fields = (
            'id', 'author', 'text', 'pub_date', 'image', 'group'
        )


class CommentSerializer(serializers.ModelSerializer):
    """Сереализатор комментариев."""

    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        model = Comment
        fields = ('id', 'author', 'text', 'created', 'post')
        read_only_fields = ('post',)


class FollowSerializer(serializers.ModelSerializer):
    """Сереализатор подписчиков."""

    user = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username',
        default=serializers.CurrentUserDefault()
    )
    following = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username'
    )

    class Meta:
        model = Follow
        fields = ('user', 'following')
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following'),
                message='Подписаться на одного автора можно только один раз'
            )
        ]

    def validate_user(self, value):
        if self.initial_data.get('following') == value.username:
            raise serializers.ValidationError('Нельзя подписаться на себя')
        return value
