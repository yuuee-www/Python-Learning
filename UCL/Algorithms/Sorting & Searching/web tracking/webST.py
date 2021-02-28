'''
We maintain a symbol table of symbol tables. 
In the first ST, we store users as keys. Associated to each user is another symbol table, 
where we store visited websites as keys, and number of past visits as values. We use our
previous BST realisation of a symbol table
'''

class BSTNode: 
    def __init__(self, key, value): 
        self.key = key
        self.value = value
        self.left = None 
        self.right = None 


    def get(self, key):
        if self.key == key: 
            return self.value 
        elif key < self.key and self.left != None:
            return self.left.get(key) 
        elif key > self.key and self.right != None: 
            return self.right.get(key) 
        else: 
            return None

    def put(self, key, value):
        if key == self.key:
            self.value = value
        elif key < self.key:
            if self.left is None:
                self.left = BSTNode(key, value)
            else:
                self.left.put(key, value)
        elif key > self.key:
            if self.right is None:
                self.right = BSTNode(key, value)
            else:
                self.right.put(key, value) 

class WebTracker:
    def __init__(self, user, website):
        webST = BSTNode(website,1)
        self.wt = BSTNode(user, webST)
    
    def recordVisit(self, user, website):
        webST = self.wt.get(user)
        if webST == None:
            webST = BSTNode(website, 1)
            self.wt.put(user, webST)
        else:
            freq = webST.get(website)
            if freq is None:
                webST.put(website, 1)
            else:
                webST.put(website, freq+1)
            
            
    def hasVisited(self, user, website):
        webST = self.wt.get(user)
        if webST== None:
            return False
        else:
            return (webST.get(website) is not None)
        
    def getVisitFrequency(self, user, website):
        webST = self.wt.get(user)
        if webST == None:
            return 0
        else:
            return webST.get(website)

with open('3-webtrack.txt','r') as f:
    line = f.readline().rstrip("\n")
    trackedVisit = line.split(",")
    webTracker = WebTracker(trackedVisit[0], trackedVisit[1])

    line = f.readline().rstrip("\n")
    while line != '':
        trackedVisit = line.split(",")
        webTracker.recordVisit(trackedVisit[0], trackedVisit[1])         
        line = f.readline().rstrip("\n")
        
print("Number of visists of user 1 to url 1 (should be 2)", webTracker.getVisitFrequency("user 1", "url 1"))
print("Number of visists of user 1 to url 2 (should be 5)", webTracker.getVisitFrequency("user 1", "url 2"))
print("Number of visists of user 1 to url 3 (should be 3)", webTracker.getVisitFrequency("user 1", "url 3"))