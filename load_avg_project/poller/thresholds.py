from datetime import datetime, timedelta
from models import LoadAvgEvent

class LoadThreshold:

    def __init__(self):
        self.threshold_start_time = datetime.utcnow()
        self.threshold_time_limit = self.threshold_start_time + timedelta(minutes=2)
        self.is_thresholding = False

    def check_limit(self, time, value):
        if value < 1:
            if self.is_thresholding:
                self.is_thresholding = False
                local_time = datetime.now()
                threshold_event = LoadAvgEvent(message="High load threshold recovered at {0}".format(local_time.strftime('%m/%d/%Y  at %I:%M:%S')), timestamp=time, type=1)
                threshold_event.save()

            self.__update_threshold_limit(time)
        elif value >= 1:
            if time >= self.threshold_time_limit:
                if not self.is_thresholding:
                    self.is_thresholding = True
                    local_time = datetime.now()
                    threshold_event = LoadAvgEvent(message="High load generated an alert - load = {0}, triggered at {1}".format(value, local_time.strftime('%m/%d/%Y  at %I:%M:%S')), timestamp=time, type=0)
                    threshold_event.save()


    def is_exceeded(self):
        return self.is_thresholding

    def __update_threshold_limit(self, time):
        self.threshold_start_time = time
        self.threshold_time_limit = self.threshold_start_time + timedelta(minutes=2)

    def get_current(self):
        return (self.current_time, self.current_value)