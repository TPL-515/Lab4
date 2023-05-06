from dagster import define_asset_job, ScheduleDefinition
from lab4.assets.cwr import *
from lab4.assets.rwc import *
##########################################################
################# Insert Code Below ######################
##########################################################

cwr_job = define_asset_job(name="crawl_walk_run", selection=['crawl', 'walk', 'run'])

cwr_schedule = ScheduleDefinition(
    job=cwr_job,
    cron_schedule="* * * * *",  # every minute
)
