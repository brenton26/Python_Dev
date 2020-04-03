from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our API Views"""

    # this is saying that whenever there is a POST, PUT, or PATCH request, to expect an input called name
    name = serializers.CharField(max_length=10)
