import time
import random

class TrafficLight:
    def __init__(self, name):  # Corrected: __init__ method
        self.name = name
        self.green_time = 10  # Default green light duration (in seconds)
        self.traffic_density = 0  # Initialize traffic density

    def update_traffic_density(self):
        """Simulate random traffic density."""
        self.traffic_density = random.randint(0, 100)
        print(f"Traffic density on {self.name}: {self.traffic_density}%")

    def calculate_green_time(self):
        """Adjust green light duration based on traffic density."""
        if self.traffic_density > 50:
            self.green_time = 30
        elif self.traffic_density > 30:
            self.green_time = 20
        else:
            self.green_time = 10

    def show_status(self):
        """Display the current state of the traffic light."""
        print(f"{self.name} green light duration: {self.green_time} seconds")
        print("." * 30)

def traffic_flow_optimization():
    """Simulate a basic traffic flow optimization system."""

    # Create traffic lights for four intersections
    traffic_lights = [
        TrafficLight("North-South"),
        TrafficLight("East-West"),
        TrafficLight("Diagonal-NE-SW"),
        TrafficLight("Diagonal-NW-SE")
    ]

    # Simulate traffic flow optimization
    while True:
        for light in traffic_lights:
            light.update_traffic_density()  # Update traffic density
            light.calculate_green_time()    # Adjust the green light duration
            light.show_status()             # Show status of the traffic light

            # Simulate the green light being on for the calculated time
            print(f"{light.name} is GREEN for {light.green_time} seconds.\n")
            time.sleep(light.green_time)

# Entry point
if __name__ == "__main__":
    traffic_flow_optimization()
