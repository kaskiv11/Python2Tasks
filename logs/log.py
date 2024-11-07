import logging


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', filename='process.log')


def progress_data(data):
    try:
        logging.info("Start progress data")
        result = [d * 2 for d in data]
        logging.info("Data progress success")
    except Exception as e:
        logging.error(f"Error progress: {e}")
        return None
    finally:
        logging.info("Finish progress data")

    return result


data = [1, 3, 3, None]

print(progress_data(data))

logging.critical("Critical error")



import hashlib


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


print(hash_password("password_123456"))
