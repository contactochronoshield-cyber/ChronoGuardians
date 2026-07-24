import logging
import sys
from logging.handlers import RotatingFileHandler

def setup_logger():
    logger = logging.getLogger("ChronoGuardians")
    logger.setLevel(logging.INFO)
    
    formatter = logging.Formatter(
        '%(asctime)s [%(levelname)s] %(name)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Consola
    ch = logging.StreamHandler(sys.stdout)
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    
    # Archivo rotativo (máx 5MB por archivo, guarda hasta 3 respaldos)
    fh = RotatingFileHandler("chronoguardians.log", maxBytes=5*1024*1024, backupCount=3)
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    
    return logger
