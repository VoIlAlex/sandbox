import notify2
import pyudev


def main():
    context = pyudev.Context()
    monitor = pyudev.Monitor.from_netlink(context)
    monitor.filter_by(subsystem='usb')

    for device in iter(monitor.poll, None):
        print('Something happed: {}'.format(device.action))
        if device.action == 'add':
            print('{} connected'.format(device))


if __name__ == "__main__":
    main()
