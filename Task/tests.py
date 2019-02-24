from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.test import APITestCase
import json
from Task.models import MissouriData
from Task.serializers import MissouriSerializer, MissouriNonIdSerializer


class MissouriDataTests(APITestCase):
    """ Unit Test for Missouri Data APIs"""

    def getTestObj(self):
        return MissouriData(county="1", est_name="test_est_name", est_addr="test_est_addr",
                            est_city="test_est_city", est_state="test_est_state", est_zip="91776",
                            est_number="1234567890", app_apr_code="TST",
                            date_lic="2019-11-20")

    def test_missouri_post(self):

        testObj = self.getTestObj()
        testObj.clean()
        url = reverse('missouri-data')
        serializer = MissouriNonIdSerializer(testObj)
        response = self.client.post(url, json.loads(JSONRenderer().render(serializer.data)), format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(MissouriData.objects.count(), 1)

    def test_missouri_get(self):
        testObj = self.getTestObj()
        testObj.clean()
        testObj.save()

        url = reverse('missouri-data')
        response = self.client.get(url, format='json')
        serializer = MissouriSerializer(data=response.data, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        if serializer.is_valid():
            self.assertGreaterEqual(JSONRenderer().render(serializer.data).count(), 1)

    def test_missouri_get_id(self):
        testObj = self.getTestObj()
        testObj.clean()
        testObj.save()

        url = reverse('missouri-details', args=[testObj.id])
        response = self.client.get(url, format='json')
        serializer = MissouriSerializer(data=response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        if serializer.is_valid():
            self.assertEqual(serializer.data['id'], testObj.id)

    def test_missouri_put(self):
        testObj = self.getTestObj()
        testObj.clean()
        testObj.save()

        testObj.est_number = "0987654321"

        serializer = MissouriSerializer(testObj)

        url = reverse('missouri-details', args=[testObj.id])
        response = self.client.put(url, json.loads(JSONRenderer().render(serializer.data)), format='json')
        serializer = MissouriSerializer(data=response.data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(serializer.data['est_number'], "0987654321")

    def test_missouri_delete(self):
        testObj = self.getTestObj()
        testObj.clean()
        testObj.save()

        url = reverse('missouri-details', args=[testObj.id])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(MissouriData.objects.filter(id=testObj.id).count(), 0)
