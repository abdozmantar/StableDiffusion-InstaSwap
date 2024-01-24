#----------------------------------------------#
# INSTASWAP FAST FACE SWAPPER NODE FOR COMFYUI #
#                                              #
#                         by abdozmantar       #
#                             2024             #
#                                              #
#         GNU GENERAL PUBLIC LICENSE           #
#----------------------------------------------#

app_title = "InstaSwap"
version_flag = "v0.1.4"

from scripts.logger import logger, get_Run, set_Run
from scripts.globals import DEVICE

is_run = get_Run()

if not is_run:
    logger.job(f"Running {version_flag} on Device: {DEVICE}")
    set_Run(True)
