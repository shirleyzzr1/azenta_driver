from .drivers.sealer_client import A4S_SEALER_CLIENT
sealer = A4S_SEALER_CLIENT("/dev/ttyUSB0")

def main():
    print('Hi from ros2_sealer_driver.')
    sealer.reset()

if __name__ == '__main__':
    main()
