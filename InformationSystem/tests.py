from datetime import datetime

from django.test import TestCase

from django.contrib.gis.db.models import PointField
from django.db.models import Manager as GeoManager

from InformationSystem.models import Alert, AlertList


class AlertTestCase(TestCase):

    DUMMY_ALERT_TITLE = 'Test Element'


    def setUp(self):

        self.alertList = AlertList()
        self.alertList.name = 'Test Alert List'
        self.alertList.save()

        self.alertListTestElement = Alert()
        self.alertListTestElement.title = self.DUMMY_ALERT_TITLE
        self.alertListTestElement.autor = self.DUMMY_ALERT_TITLE
        self.alertListTestElement.phone = self.DUMMY_ALERT_TITLE
        self.alertListTestElement.due_date = datetime.today()
        self.alertListTestElement.location = PointField(null=True, default=None, srid=4326)
        self.alertListTestElement.objects = GeoManager()
        self.alertListTestElement.Resolue = True
        self.alertListTestElement.Encours = False
        self.alertListTestElement.list = self.alertList
        self.alertListTestElement.save()

    def test_create_alert(self):

        nbr_of_alerts_before_add = Alert.objects.count()

        new_alert = Alert()
        new_alert.title = 'Acheter de l\'eau'
        new_alert.autor = 'personne2'
        new_alert.phone = '14'
        new_alert.due_date = datetime.today()
        new_alert.location = PointField(null=True, default=None, srid=4326)
        new_alert.objects = GeoManager()
        new_alert.Resolue = True
        new_alert.Encours = False
        new_alert.list = self.alertList

        new_alert.save()

        nbr_of_alerts_after_add = Alert.objects.count()

        self.assertTrue(nbr_of_alerts_after_add == nbr_of_alerts_before_add + 1)

    def test_update_alert(self):

        self.assertEqual(self.alertListTestElement.title, self.DUMMY_ALERT_TITLE)

        self.alertListTestElement.title = 'Changed'

        self.alertListTestElement.save()

        tempElement = Alert.objects.get(pk=self.alertListTestElement.pk)

        self.assertEqual(tempElement.title, 'Changed')

    def test_delete_alert(self):

        nbr_of_alerts_before_delete = Alert.objects.count()

        self.alertListTestElement.delete()

        nbr_of_alerts_after_delete = Alert.objects.count()

        self.assertTrue(nbr_of_alerts_after_delete == nbr_of_alerts_before_delete - 1)
