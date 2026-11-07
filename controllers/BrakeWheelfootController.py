from controllers.WheelfootController import WheelfootController


class BrakeWheelfootController(WheelfootController):
    """Brake policy: command is always zero; joystick cannot override velocity."""

    def sensor_joy_callback(self, sensor_joy):
        # Allow start/stop via joystick but never accept velocity commands.
        if not self.start_controller and self.calibration_state == 0 and sensor_joy.buttons[4] == 1 and sensor_joy.buttons[3] == 1:
            print("L1 + Y: start_controller...")
            self.start_controller = True
        if self.start_controller and sensor_joy.buttons[4] == 1 and sensor_joy.buttons[2] == 1:
            print("L1 + X: stop_controller...")
            self.start_controller = False
        # self.commands stays at [0, 0, 0] — intentional
