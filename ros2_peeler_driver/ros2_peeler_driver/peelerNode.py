from .drivers.peeler_client import BROOKS_PEELER_CLIENT
peeler = BROOKS_PEELER_CLIENT("/dev/ttyUSB0")
def main():
    peeler.check_status()

if __name__ == '__main__':

    main()
