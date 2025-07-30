import logging
import azure.functions as func

def main(myblob: func.InputStream, resultdoc: func.Out[func.DocumentList]):
    logging.info("=== BLOB TRIGGER FIRED ===")
    logging.info(f"File: {myblob.name}, Size: {myblob.length}")
    return