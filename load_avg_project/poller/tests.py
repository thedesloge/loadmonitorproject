from django.test import TestCase
from thresholds import LoadThreshold
from models import *
from datetime import datetime, timedelta

class LoadThresholdTests(TestCase):

    def test_threshold_exceeded(self):
        load_threshold = LoadThreshold()

        collect_time = datetime.utcnow()
        for idx in range(12):
            collect_time = collect_time + timedelta(seconds=10)
            load_threshold.check_limit(collect_time, 1.5)

        events = LoadAvgEvent.objects.all()

        self.assertEqual(1, len(events))

    def test_threshold_resolved(self):
        load_threshold = LoadThreshold()

        load_threshold.check_limit(datetime.utcnow() + timedelta(minutes=2), 1.5)
        self.assertTrue(True, load_threshold.is_exceeded())

        load_threshold.check_limit(datetime.utcnow() + timedelta(minutes=2, seconds=10), 0.5)
        self.assertFalse(False, load_threshold.is_exceeded())

    def test_bogus(self):
        start_date = datetime.utcnow()
        end_time = start_date + timedelta(minutes=2)
        test_date = datetime.utcnow() + timedelta(minutes=3)
        print((end_time - test_date).days)


