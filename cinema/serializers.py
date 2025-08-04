from rest_framework import serializers

from .models import Movie, Genre


class MovieModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class MovieSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField()
    genre = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all())
    image = serializers.ImageField()
    start_date = serializers.DateField()
    end_date = serializers.DateField()

    def validate_title(self, value):
        banned_words = ["bad word", "bad"]
        if value.lower() in banned_words:
            raise serializers.ValidationError("Заголовок содержит нецензурную лексику!")
        return value
    
    def validate(self, attrs):
        if attrs['start_date'] > attrs['end_date']:
            raise serializers.ValidationError("Дата окончания должна быть позже даты начала.")
        return attrs
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        instance.genre = validated_data.get("genre", instance.genre)
        instance.image = validated_data.get("image", instance.image)
        instance.start_date = validated_data.get("start_date", instance.start_date)
        instance.end_date = validated_data.get("end_date", instance.end_date)
        instance.save()
        return instance

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
    

class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password1 = serializers.CharField()
    password2 = serializers.CharField()

    def validate(self, attrs):
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError("Пароли должны совпадать")
        return attrs

