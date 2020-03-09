import time
import datetime
import logging
import threading


class TimeBased():

    def __init__(self):
        self.interval = 3
        self.decision = False
        self.logger = logging.getLogger(__name__)
        self.thread = threading.Thread(target=self.self_evaluation, args=())
        self.thread.start()

    def self_evaluation(self):
        temp_msg = f"Timeout set to {self.interval} seconds."
        self.logger.info(temp_msg)
        self.counter = 0
        while True:
            time.sleep(1)
            self.counter = self.counter + 1
            if self.counter >= self.interval:
                self.logger.info("Timeout reached.")
                self.decision = True
                break
    
    def dummy(self):
        print("dummy")

    def check_state(self):
        return self.decision

