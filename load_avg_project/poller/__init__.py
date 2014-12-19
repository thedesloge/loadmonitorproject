from datetime import datetime
from subprocess import check_output
from models import *
from thresholds import LoadThreshold
import logging

from apscheduler.schedulers.background import BackgroundScheduler

loadThreshold = LoadThreshold()

def poll_load():
    ret_val = check_output(['uptime']).split(' ')
    one_min_avg, five_min_avg, fifteen_min_avg = ret_val[-3:]

    logging.info('min: {0} avg: {1} max: {2}'.format(one_min_avg, five_min_avg, fifteen_min_avg))

    dt = datetime.utcnow()
    sample = LoadAvgSample(timestamp=dt,
                           one_minute=one_min_avg,
                           five_minute=five_min_avg,
                           fifteen_minute=fifteen_min_avg)

    sample.save()

    loadThreshold.check_limit(dt, one_min_avg)

try:
    scheduler = BackgroundScheduler()
    scheduler.add_job(poll_load, 'interval', seconds=10)
    scheduler.start()
except:
    scheduler.shutdown()
