from .drivers.sealer_client import A4S_SEALER_CLIENT
sealer = A4S_SEALER_CLIENT("/dev/ttyUSB0")

def main():
    # Run commands if manager sends corresponding command
    manager_command = "test_command"
    print('Hi from ros2_sealer_driver.')
    match manager_command:
        case "test_command":
            sealer.reset()

if __name__ == '__main__':
    main()
