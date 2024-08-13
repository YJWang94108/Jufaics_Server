from apscheduler.schedulers.blocking import BackgroundScheduler
import urllib

def timed_job():
    '''
    This job is run every five minutes.
    '''
    url = 'https://jufaics-server.onrender.com'
    with urllib.request.urlopen(url) as conn:
        pass


def Run():
    
    sched = BackgroundScheduler()
    sched.add_job(timed_job, 'interval', minutes=20)
    sched.start()