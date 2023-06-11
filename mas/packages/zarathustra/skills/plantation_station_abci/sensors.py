"""
Class to interact with the sensors of the plantation station.
"""

from time import sleep

from typing import Dict, List, Optional, cast


try:
    from gpiozero import LineSensor, PWMLED
except ImportError:
    print("gpiozero not installed. Using mock instead.")
    class LineSensor:
        """Mock class for LineSensor."""
        def __init__(self, *args, **kwargs):
            self.value = 0.0

    class PWMLED:
        """Mock class for PWMLED."""
        def __init__(self, *args, **kwargs):
            self.value = 0.0

LED_ACTUATOR_PIN = 16
MOISTURE_SENSOR_PIN = 18
LOAD_SENSOR_PIN = 1



class Sensors:
    """Class to interact with the sensors of the plantation station."""

    def __init__(self):
        """Initialize the sensors."""
        self.config = {
            "led_actuator": {
                "pin": LED_ACTUATOR_PIN,
                "initial_value": 0,
            },
            "moisture_sensor": {
                "pin": MOISTURE_SENSOR_PIN,
                "queue_len": 1,
                "sample_rate": 1,
            },
            "load_sensor": {
                "pin": LOAD_SENSOR_PIN,
                "queue_len": 1,
                "sample_rate": 1,
            },

        }
        self.sensors: List[LineSensor] = []
        self.actuators: Dict[str, PWMLED] = {}
        self._setup_sensors()
        self._setup_actuators()

    def _setup_sensors(self):
        """Setup the sensors."""
        for sensor_name in self.config:
            if "sensor" in sensor_name:
                sensor = LineSensor(
                    self.config[sensor_name]["pin"],
                    queue_len=self.config[sensor_name]["queue_len"],
                    sample_rate=self.config[sensor_name]["sample_rate"],
                )
                self.sensors.append(sensor)
    
    def _setup_actuators(self):
        """Setup the actuators."""
        for actuator_name in self.config:
            if "actuator" in actuator_name:
                actuator = PWMLED(
                    self.config[actuator_name]["pin"],
                    initial_value=self.config[actuator_name]["initial_value"],
                )
                self.actuators[actuator_name] = actuator



    def read_moisture(self) -> float:
        """Read the moisture."""
        return self.sensors[0].value

    def read_load(self) -> float:
        """Read the load."""
        return self.sensors[1].value

    def set_led_actuator(self, value: float):
        """Set the led actuator."""
        self.actuators["led_actuator"].value = value

    def read_sensors(self) -> Dict[str, float]:
        """Read the sensors."""
        return {
            "moisture": self.read_moisture(),
            "load": self.read_load(),
        }


if __name__ == "__main__":
    sensors = Sensors()
    while True:
        print(sensors.read_sensors())
        sleep(1)
