# Previously, you wrote a class called ExerciseSession that
# had three attributes: an exercise name, an intensity, and a
# duration.
#
# Add a new method to that class called calories_burned.
# calories_burned should have no parameters (besides self, as
# every method in a class has). It should return an integer
# representing the number of calories burned according to the
# following formula:
#
# - If the intensity is "Low", 4 calories are burned per
#   minute.
# - If the intensity is "Medium", 8 calories are burned
#   per minute.
# - If the intensity is "High", 12 calories are burned per
#   minute.
#
# You may copy your class from the previous exercise and just
# add to it.


# Add your code here!
class ExerciseSession:
    def __init__(self, exercise, intensity, duration):
        self.exercise = exercise
        self.intensity = intensity
        self.duration = duration

    def get_exercise(self):
        return self.exercise

    def get_intensity(self):
        return self.intensity

    def get_duration(self):
        return self.duration

    def set_exercise(self, newExercise):
        self.name = newExercise

    def set_intensity(self, newIntensity):
        self.intensity = newIntensity

    def set_duration(self, newDuration):
        self.duration = newDuration

    def calories_burned(self):
        number = 0
        if self.intensity == 'Low':
            number = self.duration * 4
        elif self.intensity == 'High':
            number = self.duration * 12

        return number


# If your code is implemented correctly, the lines below
# will run error-free. They will result in the following
# output to the console:
# 240
# 360
new_exercise = ExerciseSession("Running", "Low", 60)
print(new_exercise.calories_burned())
new_exercise.set_exercise("Swimming")
new_exercise.set_intensity("High")
new_exercise.set_duration(30)
print(new_exercise.calories_burned())



