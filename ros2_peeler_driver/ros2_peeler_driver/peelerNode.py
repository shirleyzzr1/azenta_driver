from .drivers.peeler_client import BROOKS_PEELER_CLIENT
peeler = BROOKS_PEELER_CLIENT("/dev/ttyUSB0")
def main():
    print('Hi from ros2_peeler_driver.')
    peeler.check_status()

if __name__ == '__main__':

    main()
