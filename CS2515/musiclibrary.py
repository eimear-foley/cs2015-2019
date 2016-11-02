"""Design and implement a class MusicLibrary that will mimic the
   functionality of a typical music library using the data structure
   doubly linked list.

   Design and implement a class Track which will contain the details of
   the music track and can be added to your music library."""

class DLLNode(object):

    #### Doubly Linked List Node class ####
    
    # Contains the instance variables: 'element', 'prev' and 'next'
    # Which describe the details of the music track and the next and
    # previous music track

    def __init__(self, item, prevnode, nextnode):
        self._element = item
        self._next = nextnode
        self._prev = prevnode

class List(object):

    #### Doubly Linked List class ####

    def __init__(self):

        # Initializes DLL with head and tail using DLLNode class
        
        self._head = DLLNode(None, None, None)
        self._tail = DLLNode(None, self._head, None)
        self._head._next = self._tail
        self._size = 0 # sets size of list to zero
        self._first = None # pointer to first node in list
        self._last = None # pointer to last node in list
        self._cursor = self._head # pointer to current node in list

    def get_first(self):

        # Returns first node in list i.e. first track in music library or None

        if self._size == 0:
            return None
        else:
            return self._first

    def add_first(self, item):

        # Adds first node to list
        
        node = DLLNode(item, self._head, self._tail)
        self._first = node
        self._last = node
        self._size += 1

    def add_last(self, item):

        # Adds node to end of the list 
        if self._first == None:
            self.add_first(item)
        else:
            newnode = DLLNode(item, None, self._tail)
            self._last._next = newnode
            newnode._prev = self._last
            self._last = newnode
        self._size += 1             

    def remove_node(self, node):

        # Removes node and sets the prev node and next node to connect to each other

        before = node._prev
        after = node._next
        if node == self._first:
            self._first = node._next
        if node == self._last:
            self._last = before   
        self._cursor = after
        before._next = after
        after._prev = before
        self._size -= 1 # Decrement size of list
        node = DLLNode(None, None, None) #Set node to None
        
    def swap_adjacent(self, n1, n2):

        # Swap adjacent nodes i.e. when sorting music library

        if n2 == self._last:
            self._last = n1

        if n1 == self._first:
            self._first = n2

        before = n1._prev
        after = n2._next

        before._next = n2
        after._prev = n1
        n2._prev = before
        n1._next = after
        n1._prev = n2
        n2._next = n1

class Track(object):

    #### Track class ####

    # Initializes Track with instance variables: 'name', 'artiste', 'timesplayed'
    
    def __init__(self, name, artiste, timesplayed):
        self._name = name
        self._artiste = artiste
        self._timesplayed = timesplayed

    def play(self):

        self._timesplayed += 1

    def __str__(self):

        return ("%s, %s, Times Played: %i" % (self._name, self._artiste, self._timesplayed))

class MusicLibrary(object):

    #### MusicLibrary class ####
    
    def __init__(self):
        self._tracks = List() #Initializes music library using DLL

    def play(self):

        # Plays current track or displays messages if at list head or list tail

        if self._tracks._cursor == self._tracks._head:
            print("Please move to the next track in your music library from the list head.\n")
        elif self._tracks._cursor == self._tracks._tail:
            print("Please move to the prev track in your music library from the list tail.\n")
        else:
            Track.play(self._tracks._cursor._element)
            print("Currently playing: %s\n" % self._tracks._cursor._element)

    def add_track(self, track):

        # Adds track to music library calling DLL class implementation of addding a node

        if self._tracks._size == 0:
            self._tracks.add_first(track)
            self._tracks._cursor = self._tracks._head
        else:
            self._tracks.add_last(track)

    def get_current(self):

        # Returns current track or displays message if at list head or tail

        if self._tracks._cursor == self._tracks._head:
            print("Current Track: List Head\n")
        elif self._tracks._cursor == self._tracks._tail:
            print("Current Track: List Tail\n")
        else:
            print("Current Track: %s\n" % self._tracks._cursor._element)

    def reset(self):

        # Resets current track to list head

        self._tracks._cursor = self._tracks._head
        
    def next_track(self):

        # Move to next track in music library
        # If at list tail, remain at list tail and display message
        # If moved to list tail, display message

        if self._tracks._cursor == self._tracks._head:
            self._tracks._cursor = self._tracks._first
        elif self._tracks._cursor == self._tracks._tail:
            print("Current Track: List Tail\n")
            return
        else:
            self._tracks._cursor = self._tracks._cursor._next
        if self._tracks._cursor == self._tracks._last._next:
            print("Current Track: List Tail\n")
            return
        return ("Current Track: %s\n" % (self._tracks._cursor._element))

    def prev_track(self):

        # Move to previous track in music library
        # If at list head, remain at list head and display message
        # If moved to list head, display message

        if self._tracks._cursor == self._tracks._head:
            print("Current Track: List Head\n")
            return
        self._tracks._cursor = self._tracks._cursor._prev
        if self._tracks._cursor == self._tracks._head:
            print("Current Track: List Head\n")
        else:
            print("Current Track: %s\n" % self._tracks._cursor._element)

    def remove_current(self):

        # Remove current track if track in music library
        
        if self._tracks._size == 0:
            return ("No track to remove.\n")
        else:
            removed = self._tracks._cursor
            self._tracks.remove_node(self._tracks._cursor)
            print("%s has been removed from your music library.\n" % removed._element)
            

    def print_tracks(self):

        # Helper function for __str__

        print("Music Library:")
        track = self._tracks.get_first()
        while track._next:
            
            print("%s" % track._element)
            track = track._next

    def sort_by_name(self):

        # Sort tracks by name - bubble sort

        for _ in range(self._tracks._size):
            node = self._tracks.get_first()
            while node._next:
                nextnode = node._next
                if node._next == self._tracks._last._next: 
                    break
                if node._element._name > nextnode._element._name:
                    self._tracks.swap_adjacent(node, nextnode)
                node = nextnode
        self.print_tracks()

    def sort_by_artiste(self):

        # Sort track by artiste - bubble sort

        for _ in range(self._tracks._size):
            node = self._tracks.get_first()
            while node._next:
                nextnode = node._next
                if node._next == self._tracks._last._next: 
                    break
                if node._element._artiste > nextnode._element._artiste:
                    self._tracks.swap_adjacent(node, nextnode)
                node = nextnode
        self.print_tracks()

    def search(self, substring):

        # Search for track in library by substring
        # NOT case sensitive

        track = self._tracks._cursor
        current = track
        wraparound = False
        while track._next:
            if track == current and wraparound == True:
                return False
            if substring.lower() in track._element._name.lower():
                self._tracks._cursor = track
                print("New Current Track: %s\n" % self._tracks._cursor._element)
                return True
            elif substring.lower() in track._element._artiste.lower():
                self._tracks._cursor = track
                print("New Current Track: %s" % self._tracks._cursor._element)
                return True
            elif track._next._element == None:
                track = self._tracks._first
                wraparound = True
            else:
                track = track._next
        return False
        
    def __str__(self):

        self.print_tracks()

        if self._tracks._cursor._element != None:
            return ("\nCurrent Track: %s\n" % (self._tracks._cursor._element))
        else:
            if self._tracks._cursor == self._tracks._head:
                return ("\nCurrent Track: List Head\n")
            else:
                return ("\nCurrent Track: List Tail\n")

def main():

    # Test block, only executed if program run not imported

    library = MusicLibrary()
    t1 = Track("Say you wont let go","James Arthur",0)
    t2 = Track("The Greatest","Sia feat. Kendrick Lamar",0)
    t3 = Track("Closer","Chainsmokers feat. Halsey", 0)
    t4 = Track("My way","Calvin Harris",0)
    library.add_track(t1)
    library.add_track(t2)
    library.add_track(t3)
    print(library)
    library.next_track()
    library.play()
    library.sort_by_name()
    library.next_track()
    library.get_current()
    library.prev_track()
    library.prev_track()
    library.play()
    library.remove_current()
    print(library)
    library.add_track(t4)
    print(library)
    library.sort_by_artiste()
    library.prev_track()
    library.play()
    print(library)
    print(library.search("ken"))

if __name__ == "__main__":
    main()
