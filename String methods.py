course = "Python for Beginners"
print(len(course))
print(course.upper())
print(course.find("P"))
# You get 0 here as this is the position of P in the string
print(course.find("z"))
# Negative 1 is if not found
print(course.replace("Beginners", "Absolute Beginners"))
print(course)
print("Python" in course)
# All case sensitive
print(course.title())