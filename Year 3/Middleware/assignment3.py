class Event:
    def __init__(self, event_type):
        self._type = event_type
        self._notification = ""
        self._alert = False

    def setNotification(self, message, alert):
        if alert == True:
            self._alert = True
            self._notification = ("ALERT: %s" % message)
        else:
            self._notification = ("%s" % message)
        
    def getNotification(self):
        if self._notification == "":
            return "No notification."
        else:
            return ("%s" % self._notification)

class Subscriber:
    def __init__(self, usr):
        self._username = usr
        self._notifications = []

    def subscribeTo(self, event):
        print("Subscribing '%s' to '%s'.\n" % (self._username, event._type))
        notification_mngr.manageSubscribers(self, event)

    def unsubscribeFrom(self, event):
        print("Unsubscribing '%s' from '%s'.\n" % (self._username, event._type))
        notification_mngr.removeEvent(self, event)

    def turnOffNotifications(self, event):
        if self._notifications == []:
            self._notifications = [event]
        else:
            self._notifications.append(event)
        print("'%s' has turned off notifications for '%s'.\n" % (self._username, event._type))
        
    def turnOnNotifications(self, event):
        self._notifications.remove(event)
        print("'%s' has turned on notifications for '%s'.\n" % (self._username, event._type))

    def checkEvent(self, event):
        print("Checking '%s' notifications..." % event._type)
        print("Current notification: %s" % event.getNotification())

class Publisher:
    def createEvent(self, event_type):
        new_event = Event(event_type)
        print("New event type '%s' created." % event_type)
        return new_event

    def createNewNotification(self, message, event, alert=False):
        event.setNotification(message, alert)
        print("Notifying subscribers...")
        notification_mngr.sendNotifications(event)

class NotificationManager:
    def __init__(self):
        self._subscribers = {}

    def sendNotifications(self, event):
        found = False
        for subscriber in self._subscribers:
            if event._alert == True:
                if event in self._subscribers[subscriber]:
                    found = True
                    print("Subscriber '%s' has a new notification:\n%s: %s\n" % (subscriber._username, event._type, event.getNotification()))
            else:
                if (event in self._subscribers[subscriber]) and (event not in subscriber._notifications):
                    found = True
                    print("Subscriber '%s' has a new notification:\n%s: %s\n" % (subscriber._username, event._type, event.getNotification()))
        if not found:
            print("No subscribers to '%s'.\n" % event._type)

    def manageSubscribers(self, subscriber, event):
        if subscriber not in self._subscribers:
            self._subscribers[subscriber] = [event]
        else:
            self._subscribers[subscriber].append(event)
    
    def removeEvent(self, subscriber, event):
        to_remove = self._subscribers[subscriber]
        j = 0
        for i in to_remove:
            if i._type == event._type:
                to_remove.pop(j)
            j += 1

if __name__ == "__main__":
    notification_mngr = NotificationManager()
    publisher = Publisher()
    s1 = Subscriber('user24')
    s2 = Subscriber('middleware2')
    s3 = Subscriber('cats4lyf')
    weather = publisher.createEvent("Weather")
    publisher.createNewNotification("Cloudy tomorrow.", weather)
    news = publisher.createEvent("News")
    cat_memes = publisher.createEvent("Cat Memes")
    technology = publisher.createEvent("Technology")
    s1.subscribeTo(weather)
    s1.subscribeTo(news)
    s1.subscribeTo(technology)
    s2.subscribeTo(news)
    s2.subscribeTo(technology)
    s3.subscribeTo(cat_memes)
    s3.subscribeTo(technology)
    s3.subscribeTo(weather)
    publisher.createNewNotification("Sunny tomorrow and 24 degrees.", weather)
    s1.turnOffNotifications(news)
    s2.unsubscribeFrom(technology)
    publisher.createNewNotification("Fatal crash on M8.", news, True)
    s3.turnOffNotifications(cat_memes)
    publisher.createNewNotification("PIC: CAT SLEEPING.", cat_memes)
    publisher.createNewNotification("New iPhone 11.", technology)