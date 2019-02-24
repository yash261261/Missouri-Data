from rest_framework.views import APIView
from Task.models import MissouriData
from Task.serializers import MissouriSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from rest_framework.response import Response


class MissouriDataViews(APIView):

    def get(self, request, format=None):
        """Get all MissouriData objects"""

        objs = MissouriData.objects.all()
        serializer = MissouriSerializer(objs, many=True)
        return Response(JSONRenderer().render(serializer.data))

    def post(self, request, format=None):
        """Create new MissouriData object"""

        serializer = MissouriSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MissouriDetailViews(APIView):
    def get_object(self, pk):
        try:
            return MissouriData.objects.get(pk=pk)
        except MissouriData.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        """ Get Missouri Data Object by ID"""

        serializer = MissouriSerializer(self.get_object(pk))
        return Response(JSONRenderer().render(serializer.data))

    def put(self, request, pk, format=None):
        """Update Missouri Data Object """

        serializer = MissouriSerializer(self.get_object(pk), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """Delete Missouri Data Object by ID"""

        self.get_object(pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
