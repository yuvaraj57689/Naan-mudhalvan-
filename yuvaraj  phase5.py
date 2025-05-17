import random
import time

class TrafficSignal:
    def __init__(self, id):  # Corrected: __init__ and assignment syntax
        self.id = id
        self.vehicle_count = 0
        self.signal_time = 30  # Default green light duration in seconds

    def update_vehicle_count(self):
        # Simulate real-time vehicle count (e.g., from sensors/CMNS)
        self.vehicle_count = random.randint(5, 50)  # Corrected: randint(5, 50)

    def adjust_signal_time(self):
        # Reinforcement Learning logic simulated as simple rule-based logic
        if self.vehicle_count > 40:
            self.signal_time = 60
        elif self.vehicle_count > 25:
            self.signal_time = 45
        else:
            self.signal_time = 30

    def __str__(self):
        return f"Signal [{self.id}]: Vehicles ({self.vehicle_count}), Green Time ({self.signal_time}s)"

# Simulate a traffic network
signals = [TrafficSignal(i) for i in range(1, 5)]

print("AI-Powered Traffic Signal Optimization ---")
for _ in range(3):  # Simulate 3 cycles
    for signal in signals:
        signal.update_vehicle_count()
        signal.adjust_signal_time()
        print(signal)
    print("---")
    time.sleep(1)  # Wait to simulate real-time cycle
