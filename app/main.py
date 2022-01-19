import threading
from models.sincornização_model import verify_master_file

threading.Thread(target=verify_master_file).start()