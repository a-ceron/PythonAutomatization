from apscheduler.schedulers.background import BackgroundScheduler
from database import utils as dbutils

scheduler = BackgroundScheduler()

def create_schedule(minutes=10):
    """Crea un nuevo trabajo programado para ejecutar la función de verificación de tickets."""
    scheduler.add_job(dbutils.check_tickets, 'interval', minutes=minutes)
    scheduler.start()
    return scheduler

def stop_schedule():
    """Detiene el trabajo programado."""
    scheduler.shutdown()
    return scheduler

def get_schedule_status():
    """Obtiene el estado del trabajo programado."""
    return scheduler.state

def get_schedule_jobs():
    """Obtiene los trabajos programados."""
    return scheduler.get_jobs()

def update_jobs():
    """Actualiza los trabajos programados."""
    active_tickets = dbutils.get_active_tickets()
    for job in scheduler.get_jobs():
        if job.id not in active_tickets:
            scheduler.remove_job(job.id)

