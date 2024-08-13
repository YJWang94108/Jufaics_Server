from apscheduler.schedulers.background import BackgroundScheduler
import urllib

def timed_job():
    '''
    This job is run every fifteen minutes.
    '''
    url = 'https://jufaics-server.onrender.com'
    with urllib.request.urlopen(url) as conn:
        pass


def Run():

    sched = BackgroundScheduler()
    sched.add_job(timed_job, 'interval', minutes=15)
    sched.start()