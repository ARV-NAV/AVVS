"""Python function that is able to calculate the angle in degrees of an object from the visual
   censor. The function requires the height and width in pixels, the degrees the visual sensor covers as well as the position of the object in pixel coordinates."""
import math

def calculate_angle(width, height, viewport_angle, object_x, object_y):
    diagonal = math.sqrt(height**2 + width**2)
    degree_per_pixel = viewport_angle/diagonal
    distance_from_center = abs(object_x - width/2)
    angle_of_object = degree_per_pixel * distance_from_center
    return angle_of_object
