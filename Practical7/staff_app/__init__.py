
# Make these classes available from the staff_app package

from .department import Department
from .people import Person, Employee, Developer

__all__ = ["Department", "Person", "Employee", "Developer"]
