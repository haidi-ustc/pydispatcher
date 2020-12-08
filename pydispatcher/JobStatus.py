from enum import Enum

class JobStatus (Enum) :
    unsubmitted = 1
    waiting = 2
    running = 3
    terminated = 4
    finished = 5
    completing = 6
    unknown = 100

def get_job_status(status):
    if status==JobStatus.unsubmitted:
       return "unsubmitted"
    elif status==JobStatus.waiting:
       return "waiting"
    elif status==JobStatus.running:
       return "running"
    elif status==JobStatus.terminated:
       return "terminated"
    elif status==JobStatus.finished:
       return "finished"
    elif status==JobStatus.completing:
       return "completing"
    else:
       return "unknown"
