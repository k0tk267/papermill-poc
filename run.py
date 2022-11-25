import papermill as pm
from dotenv import load_dotenv
import os
from datetime import datetime as dt

load_dotenv()
PROJECT_PATH=os.environ["PROJECT_PATH"]

timestamp = dt.now().strftime('%Y-%m-%d-%Hh-%Mm')

pm.execute_notebook(
    f"{PROJECT_PATH}/notebooks/input/input.ipynb",
    f"{PROJECT_PATH}/notebooks/output/output_{timestamp}.ipynb",
    parameters=dict(alpha=5, delta=7)
)
