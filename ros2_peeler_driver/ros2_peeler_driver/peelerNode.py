from .drivers.peeler_client import BROOKS_PEELER_CLIENT
peeler = BROOKS_PEELER_CLIENT("/dev/ttyUSB0")
def main():
    # Run commands if manager sends corresponding command
    manager_command = "test_command"
    print('Hi from ros2_peeler_driver.')

    if manager_command == "test_command":
        peeler.check_status()
        peeler.check_version()
        peeler.reset()

    print(peeler.peeler_output)

if __name__ == '__main__':

    main()
