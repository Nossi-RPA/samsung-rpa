# 변수: 기본 최고속도
DEFAULT_MAX_SPEED = 100  # km/h


# 함수: 주행 함수
def drive(distance, hours):
    speed = distance / hours
    if speed > DEFAULT_MAX_SPEED:
        return f"Too fast! You drove at {speed} km/h!"
    return f"You drove at {speed} km/h."


# 클래스: 차량 클래스
class Car:
    def __init__(self, brand, model, max_speed=DEFAULT_MAX_SPEED):
        self.brand = brand
        self.model = model
        self.max_speed = max_speed
        self.current_speed = 0

    def accelerate(self, amount):
        self.current_speed += amount
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed

    def brake(self, amount):
        self.current_speed -= amount
        if self.current_speed < 0:
            self.current_speed = 0

    def status(self):
        print(f"{self.brand} {self.model} is running at {self.current_speed} km/h.")
