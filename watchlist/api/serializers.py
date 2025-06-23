from rest_framework import serializers

from watchlist.models import WatchList,StreamList,Review


# class WatchlistSerializer(serializers.Serializer):
#     id=serializers.IntegerField(read_only=True)
#     title= serializers.CharField(max_length=100)
#     description = serializers.CharField(max_length=255)
#     active = serializers.BooleanField(default=True)

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    

#     def update(self, instance, validated_data):
#         instance.title=validated_data.get('title',instance.title)
#         instance.description=validated_data.get('description',instance.description)
#         instance.active=validated_data.get('active',instance.active)
#         instance.save()
#         return instance
    

#     def validate_title(self,value):
#         if len(value)<2:
#             return serializers.ValidationError("Too short")
#         else:
#             return value
class ReviewSerializer(serializers.ModelSerializer):
    review_user=serializers.StringRelatedField(read_only=True)
    class Meta:
        model=Review
        exclude=('watchlist',)

class WatchlistSerializer(serializers.ModelSerializer):
    review=ReviewSerializer(many=True,read_only=True)
    class Meta:
        model=WatchList
        fields="__all__"
    
    
    def validate_title(self,value):
        if len(value)<2:
            return serializers.ValidationError("Too short")
        else:
            return value
        
class StreamSerializer(serializers.ModelSerializer):
    watchlist=WatchlistSerializer(many=True, read_only=True)
    class Meta:
        model=StreamList
        fields="__all__"



        

