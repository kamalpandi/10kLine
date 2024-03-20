import time

def connect() -> None:
    print('connecting to internet...')
    time.sleep(3)
    print('you are connected')

if __name__ == 'main':
    connect()