"""Prints the palm position of each hand, every frame. When a device is
connected we set the tracking mode to desktop and then generate logs for
every tracking frame received. The events of creating a connection to the
server and a device being plugged in also generate logs.
"""

import leap
import time


class Listener(leap.Listener):
    def on_connection_event(self, event):
        print("Connected")

    def on_device_event(self, event):
        print(f"Device event: {event.type}")
        try:
            with event.device.open():
                info = event.device.get_info()
                print(f"Device info: {info.serial} {info.status}")
        except leap.LeapCannotOpenDeviceError:
            info = event.device.get_info()

        print(f"Found device {info.serial}")

    def on_tracking_event(self, event):
        # print(f"Tracking event: {event.type}")
        # print(f"Frame {event.tracking_frame_id} with {len(event.hands)} hands.")
        for hand in event.hands:
            hand_type = "left" if str(hand.type) == "HandType.Left" else "right"
            print(hand.pinch_distance, hand.pinch_strength)
            # print(
            #     f"Hand id {hand.id} is a {hand_type} hand with position ({hand.palm.position.x}, {hand.palm.position.y}, {hand.palm.position.z})."
            # )


def main():
    connection = leap.Connection()
    connection.add_listener(Listener())

    running = True

    with connection.open():
        connection.set_tracking_mode(leap.TrackingMode.Desktop)
        while running:
            # for device in connection.get_devices():
            #     print(f"Device {device.get_info().serial} connected")
            time.sleep(1)


if __name__ == "__main__":
    main()
