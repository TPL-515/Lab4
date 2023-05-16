##########################################################
################# Insert Code Below ######################
##########################################################
from dagster import Definitions, load_assets_from_modules
from lab4.assets import cwr
from lab4.jobs import cwr_job, cwr_schedule

cwr = load_assets_from_modules([cwr])

all_assets = cwr

defs = Definitions(
    assets=all_assets,
    jobs=[cwr_job],
    schedules=[cwr_schedule]
)