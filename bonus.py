#SRP is satisfied by having separate classes for User, Activity, ActivityMonitor, 
#DataStorage, and Display. Each focus on a single functional element.
    #User class - represents a user
    #Activity class - represents an activity. Its subclasses handle specific activities
    #ActivityMonitor class - monitors and collects data about user activities. Initiates data storage and notification
    #DataStorage Interface - abstracts the behavior for saving data
    #FileDataStorage class - concrete implementation of DataStorage. Saves data to a file
    #Display class - implements Observer and displays data

#OCP is satisfied by using the Observer pattern, which allows for
#new activity types without modifying existing classes.
    #the activity moniter class is open for extenton since new activity types can be added by creating new subclasses of Activity
    #however it is also closed for modification because existing classes are not modified when new activities are added

#LSP is satisfied by having the Activity class and its subclasses adhere to the 
#observer pattern's contracts, making them compatible with the notification mechanism.
    #subclasses of Activity such as walking and swimming can be used interchangeably with the base class without affecting the program's functionality.

#ISP is satisfied by defining separate interfaces for data
#collection and display (Observer interface and DataStorage interface).
    #the ObserverDisplay interface abstracts the behavior for an observer whereas the DataStorage interface abstracts the behavior for saving data
    #since each handle distinct concerns there are no dependencies

#DIP is satisfied by injecting dependencies like DataStorage and Display 
#into the ActivityMonitor constructor for loose coupling and easier testing.
    #the ActivityMonitor class accepts dependencies (DataStorage, Display) through its constructor

from abc import ABC, abstractmethod

class User:
    def __init__(self, name):
        self.name = name

class Activity(ABC): #base class
    @abstractmethod
    def perform_activity(self):
        print("performing")

class Walking(Activity): #concrete
    def perform_activity(self):
        print("Walking!")

class Swimming(Activity): #concrete
    def perform_activity(self):
        print("Swimming!")

class ActivityMonitor:
    def __init__(self, data_storage, display):
        self.observers = []
        self.data_storage = data_storage
        self.display = display

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self, data):
        for observer in self.observers:
            observer.update(data)

    def collect_data(self, user, activity_type, duration, intensity):
        data = {
            "user": user,
            "activity_type": activity_type,
            "duration": duration,
            "intensity": intensity
        }

        self.data_storage.save_data(data)  # SRP

        self.notify_observers(data)  # OCP


class DataStorage(ABC): #interface 
    @abstractmethod
    def save_data(self, data):
        print("save")

class FileDataStorage(DataStorage): #concrete implementation
    def save_data(self, data):
        print(f"Saving data to file: {data}")


class ObserverDisplay(ABC): #interface
    @abstractmethod
    def update(self, data):
        print("update")


class Display(ObserverDisplay): #concrete implementation
    def update(self, data):
        print(f"Displaying data: {data}")


def main():
    user = User("Jayme Greer")
    display = Display()
    data_storage = FileDataStorage()

    activity_monitor = ActivityMonitor(data_storage, display)
    activity_monitor.add_observer(display)

    walking = Walking()
    swimming = Swimming()

    walking.perform_activity()
    activity_monitor.collect_data(user, "Walking", duration=30, intensity="Moderate")

    swimming.perform_activity()
    activity_monitor.collect_data(user, "Swimming", duration=45, intensity="High")

if __name__ == "__main__":
    main()
