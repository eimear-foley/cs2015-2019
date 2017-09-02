from APQ import *

class Vertex:
    """ A Vertex in a graph. """
    
    def __init__(self, element):
        """ Create a vertex, with data element. """
        self._element = element

    def __str__(self):
        """ Return a string representation of the vertex. """
        return str(self._element)

    __repr__ = __str__

    def __lt__(self, v):
        return self._element < v.element()

    def element(self):
        """ Return the data for the vertex. """
        return self._element
    
class Edge:
    """ An edge in a graph.

        Implemented with an order, so can be used for directed or undirected
        graphs. Methods are provided for both. It is the job of the Graph class
        to handle them as directed or undirected.
    """
    
    def __init__(self, v, w, element):
        """ Create an edge between vertice v and w, with label element.

            element can be an arbitrarily complex structure.
        """
        self._vertices = (v,w)
        self._element = element

    def __str__(self):
        """ Return a string representation of this edge. """
        return ('(' + str(self._vertices[0]) + '--'
                   + str(self._vertices[1]) + ' : '
                   + str(self._element) + ')')

    __repr__ = __str__

    def vertices(self):
        """ Return an ordered pair of the vertices of this edge. """
        return self._vertices

    def start(self):
        """ Return the first vertex in the ordered pair. """
        return self._vertices[0]

    def end(self):
        """ Return the second vertex in the ordered. pair. """
        return self._vertices[1]

    def opposite(self, v):
        """ Return the opposite vertex to v in this edge. """
        if self._vertices[0] == v:
            return self._vertices[1]
        elif self._vertices[1] == v:
            return self._vertices[0]
        else:
            return None

    def element(self):
        """ Return the data element for this edge. """
        return self._element

class RouteMap:   
    def __init__(self):
        """ Create an initial empty graph. """
        self._structure = dict()
        # the keys are the vertices
        # the values are the edges for the corresponding vertex
        # Each edge set is also maintained as a dictionary,
        # with opposite vertex as the key and the edge object as the value
        self._coordinates = dict() #dict, with vertices as keys, coordinates as values
        self._elements = dict() #dict, with elements as keys, vertices as values

    def __str__(self):
        """ Return a string representation of the graph. """
        if self.num_vertices() <= 100 and self.num_edges() <= 100:
            hstr = ('|V| = ' + str(self.num_vertices())
                    + '; |E| = ' + str(self.num_edges()))
            vstr = '\nVertices: '
            for v in self._structure:
                vstr += str(v) + '-'
            edges = self.edges()
            estr = '\nEdges: '
            for e in edges:
                estr += str(e) + ' '
            return hstr + vstr + estr

    #--------------------------------------------------------------------------#
    #ADT methods to query the graph
    
    def num_vertices(self):
        """ Return the number of vertices in the graph. """
        return len(self._structure)

    def num_edges(self):
        """ Return the number of edges in the graph. """
        num = 0
        for v in self._structure:
            num += len(self._structure[v])    #the dict of edges for v
        return num //2     #divide by 2, since each edege appears in the
                           #vertex list for both of its vertices

    def vertices(self):
        """ Return a list of all vertices in the graph. """
        return [key for key in self._structure]

    def get_vertex_by_label(self, element):
        """ get the first vertex that matches element. """
        if self._elements[element]:
            return self._elements[element]
        return None

    def edges(self):
        """ Return a list of all edges in the graph. """
        edgelist = []
        for v in self._structure:
            for w in self._structure[v]:
                #to avoid duplicates, only return if v is the first vertex
                if self._structure[v][w].start() == v:
                    edgelist.append(self._structure[v][w])
        return edgelist

    def get_edges(self, v):
        """ Return a list of all edges incident on v. """
        if v in self._structure:
            edgelist = []
            for w in self._structure[v]:
                edgelist.append(self._structure[v][w])
            return edgelist
        return None

    def get_edge(self, v, w):
        """ Return the edge between v and w, or None. """
        if (self._structure != None
                         and v in self._structure
                         and w in self._structure[v]):
            return self._structure[v][w]
        return None

    def degree(self, v):
        """ Return the degree of vertex v. """
        return len(self._structure[v])

    #--------------------------------------------------------------------------#
    #ADT methods to modify the graph
    
    def add_vertex(self, element, coordinates):
        """ Add a new vertex with data element.

            If there is already a vertex with the same data element,
            this will create another vertex instance.
        """
        v = Vertex(element)
        self._structure[v] = dict()
        self._coordinates[v] = coordinates
        # add vertex v with associated coordiates to dict
        self._elements[element] = v
        # add vertex v to dict with element as key
        return v

    def add_vertex_if_new(self, element):
        """ Add and return a vertex with element, if not already in graph.

            Checks for equality between the elements. If there is special
            meaning to parts of the element (e.g. element is a tuple, with an
            'id' in cell 0), then this method may create multiple vertices with
            the same 'id' if any other parts of element are different.

            To ensure vertices are unique for individual parts of element,
            separate methods need to be written.
        """
        for v in self._structure:
            if v.element() == element:
                return v
        return self.add_vertex(element)

    def add_edge(self, v, w, element):
        """ Add and return an edge between two vertices v and w, with  element.

            If either v or w are not vertices in the graph, does not add, and
            returns None.
            
            If an edge already exists between v and w, this will
            replace the previous edge.
        """
        if not v in self._structure or not w in self._structure:
            return None
        e = Edge(v, w, element)
        self._structure[v][w] = e
        self._structure[w][v] = e
        return e

    def add_edge_pairs(self, elist):
        """ add all vertex pairs in elist as edges with empty elements. """
        for (v,w) in elist:
            self.add_edge(v,w,None)

    #--------------------------------------------------------------------------#
    #Additional methods to explore the graph
        
    def highestdegreevertex(self):
        """ Return the vertex with highest degree. """
        hd = -1
        hdv = None
        for v in self._structure:
            if self.degree(v) > hd:
                hd = self.degree(v)
                hdv = v
        return hdv

    #--------------------------------------------------------------------------#
    #Depth First Search

    def depthfirstsearch(self, v):
        marked = {v:None}
        self._depthfirstsearch(v, marked)
        return marked

    def _depthfirstsearch(self, v, marked):
        for e in self.get_edges(v):
            w = e.opposite(v)
            if w not in marked:
                marked[w] = e
                self._depthfirstsearch(w, marked)

    #--------------------------------------------------------------------------#
    #Breadth First Search

    def breadthfirstsearch(self, v):
        levelnum = 1
        marked = {v:(None, 0)}
        level = [v]
        while len(level) > 0:
            nextlevel = []
            for w in level:
                for e in self.get_edges(w):
                    x = e.opposite(w)
                    if x not in marked:
                        marked[x] = (w, levelnum)
                        nextlevel.append(x)
            level = nextlevel
            levelnum += 1
        return marked
    
    #--------------------------------------------------------------------------#
    #Paths and Distances

    def pathsAndDistances(self, search):

        root = None
        for key in search:
            if search[key] == (None, 0):
                root = key

        print("Root: %s" % root)
        cur_vertex = None
        for key in search:
            path = ""
            start = key
            path += ("%s -- " % start)
            cur_vertex = start 
            while cur_vertex != root:
                cur_vertex = search[cur_vertex][0]
                path += ("%s -- " % cur_vertex)
            path += ("level number %i" % search[start][1])
            print(path)
                
    #End of class definition

    #--------------------------------------------------------------------------#
    ### Dijkstras Algorithm

    def dijkstra(self, s):

        opened = APQ()
        locs = {}
        closed = {}
        preds = {s: None}
        element = opened.add(0, s)
        locs[s] = element
        while not opened.is_empty():
            apq_elt = opened.remove_min()
            vertex = apq_elt._value
            cost = apq_elt._key
            locs.pop(vertex)
            predecessor = preds.pop(vertex)
            closed[vertex] = (cost, predecessor)
            for edge in self.get_edges(vertex):
                w = edge.opposite(vertex)
                if w not in closed:
                    new_cost = cost + edge._element
                    if w not in locs:
                        preds[w] = vertex
                        elt = opened.add(new_cost, w)
                        locs[w] = elt
                    elif new_cost < opened.get_key(locs[w]):
                        preds[w] = vertex
                        opened.update_key(locs[w], new_cost)
        return closed

    #--------------------------------------------------------------------------#
    ### New method: sp(v, w)
    # finds shortest path from vertex v to vertex w

    def sp(self, v, w):
        d = self.dijkstra(v)
        vertex = None
        path = []
        val = d[w]
        cost = val[0]
        prev = val[1]
        path += [(w, cost)]
        while vertex != v:
            vertex = prev
            val = d[prev]
            cost = val[0]
            prev = val[1]
            path += [(vertex, cost)]
        return path[::-1]

    #--------------------------------------------------------------------------#
    ### New method: printvlist(path)

    def printvlist(self, path):
        print("type\tlatitude\tlongitude\telement\t\tcost")
        outstr = ""
        for item in path:
            v = item[0]
            outstr += ("W\t%f\t%f\t%i\t%f\n" % (self._coordinates[v][0],self._coordinates[v][1], v._element, item[1]))
        return outstr
            
#------------------------------------------------------------------------------#

def graphreader(filename):
    """ Read and return the route map in filename. """
    route = RouteMap()
    file = open(filename, 'r')
    entry = file.readline() #either 'Node' or 'Edge'
    num = 0
    while entry == 'Node\n':
        num += 1
        nodeid = int(file.readline().split()[1])
        line = file.readline().split() # line with GPS details
        coords = (float(line[1]), float(line[2])) #latitude, longitude
        vertex = route.add_vertex(nodeid, coords)
        entry = file.readline() #either 'Node' or 'Edge'
    print('Read', num, 'vertices and added into the graph')
    num = 0
    while entry == 'Edge\n':
        num += 1
        source = int(file.readline().split()[1])
        sv = route.get_vertex_by_label(source)
        target = int(file.readline().split()[1])
        tv = route.get_vertex_by_label(target)
        length = float(file.readline().split()[1])
        time = float(file.readline().split()[1])
        #oneway = (file.readline().split()[1])
        edge = route.add_edge(sv, tv, time)
        file.readline() #read the one-way data
        entry = file.readline() #either 'Node' or 'Edge'
    return route
                            
#---------------------------------------------------------------------------#
#Test methods

def test():

    routemap = graphreader('corkCityData.txt')
    ids = {}
    ids['wgb'] = 1669466540
    ids['turnerscross'] = 348809726
    ids['neptune'] = 1147697924
    ids['cuh'] = 860206013
    ids['oldoak'] = 358357
    ids['gaol'] = 3777201945
    ids['mahonpoint'] = 330068634
    sourcestr = 'wgb'
    deststr='neptune'
    source = routemap.get_vertex_by_label(ids[sourcestr])    
    dest = routemap.get_vertex_by_label(ids[deststr])
    tree = routemap.sp(source,dest)
    print(routemap.printvlist(tree))
