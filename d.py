from abc import ABC, abstractmethod
from loguru import logger

class LoggerInterface(ABC): 
    @abstractmethod
    def info(self, message):
        print("base message")

class LoguruLogger(LoggerInterface): #concrete implementation 
    def info(self, message):
        logger.info(f"Loguru {message}")

def main():
    loguru_logger = LoguruLogger()
    logger.info("info message1") #works normally
    loguru_logger.info("info message2") #works with loguru 


if __name__ == "__main__":
    main()
