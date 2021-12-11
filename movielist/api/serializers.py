from rest_framework import serializers

from movielist.models import Watchlist, StreamPlatform


class WatchlistSerializer(serializers.ModelSerializer):
    """Add a custom field. this field is not in the Movie model"""
    # len_name = serializers.SerializerMethodField()

    class Meta:
        model = Watchlist
        fields = '__all__'
        # fields = ['id', 'name', 'description']
        # exclude = ['active']

    # def get_len_name(self, object):
    #     length = len(object.title)
    #     return length
    #     # return len(object.name)
    #
    # def validate(self, data):
    #     """Object level validation"""
    #     if data['title'] == data['description']:
    #         raise serializers.ValidationError("Title and Description can't be the same")
    #     else:
    #         return data
    #
    # def validate_name(self, value):
    #     """Field level validation"""
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name should be more that 3 characters")
    #     else:
    #         return value


class StreamPlatformSerializer(serializers.ModelSerializer):

    class Meta:
        model = StreamPlatform
        fields = '__all__'

# def name_length(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("Name should be more that 3 characters")
#
#
# class WatchlistSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()
#
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         # instance = old and validated_data = new
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
#
#     def validate(self, data):
#         """Object level validation"""
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("Title and Description can't be the same")
#         else:
#             return data

# def validate_name(self, value):
#     """Field level validation"""
#     if len(value) < 2:
#         raise serializers.ValidationError("Name should be more that 3 characters")
#     else:
#         return value
