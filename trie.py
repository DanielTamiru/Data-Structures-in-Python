output = ""

class Trie :
    def __init__(self):
        self.children = {}
        self.is_complete_word = False
    def __repr__(self):
        """
        Prints a visual representation of Trie - *'s indicate a complete word
        """
        printTrie_to_output_var(self, "", "", True)
        photocopy = output
        reset_output_var()
        return photocopy
    
    def insert(self, word) :
        """
        Insterts string into trie
        """
        new_suffix = False # assume false to start
        for c in word :
            if new_suffix :
                child = False # no child already in trie
            else :
                child = self.children.get(c, False)
            if not child :
                self.children[c] = Trie()
                child = self.children[c]
                new_suffix = True
            self = child
        self.is_complete_word = True

    def contains(self, word) :
        """
        Returns whether the string exists in the trie and the trie-node where the search failed/succeeded
        """
        for c in word :
            child = self.children.get(c, False)
            if not child :
                return False, self
            else :
                self = child
        return True, self

    def longest_common_prefix(self) : 
        """
        Accumelate characters unitl trie branches off into multiple paths
        """
        prefix = ""
        while len(self.children) == 1 :
            prefix += list(self.children.keys())[0] #only key (character)
            self = list(self.children.values())[0]  #only value (Trie node)
        return prefix

#_The following two functions and the global variable output are a work-around for
# printing a tree. I couldn't think of a better recursive algorithm at the time so
# I had to work with what I had and in doing so, I learned a little bit more about
# python variable scope and namespace
def printTrie_to_output_var(node, indent, char, last_child) :
    global output
    output += indent + "+- " + char + "\n"
    if last_child :
        indent += "  "
    else :
        indent += "|  "
    last_child = False

    for i, (c, child) in enumerate(node.children.items()) :
        if i == len(node.children) - 1 :
            last_child = True
        if child.is_complete_word :
            c += '*'
        printTrie_to_output_var(child, indent, c, last_child)
def reset_output_var() :
    global output
    output = ""

#----Practice Tries to play around with----
# cars = Trie()
# cars.insert("Toyota")
# cars.insert("Honda")
# cars.insert("Ford")
# cars.insert("Tesla")
# cars.insert("Audi")
# cars.insert("Acura")
# cars.insert("Buick")
# cars.insert("Fiat")
# cars.insert("Hyundai")
# cars.insert("Chevrolet")
# cars.insert("Nissan")
# cars.insert("Volkswagen")
# cars.insert("Chrysler")
# cars.insert("Ferrari")
# cars.insert("Jeep")
# cars.insert("Mazda")
# cars.insert("Lexus")
# cars.insert("Infiniti")
# cars.insert("Ferrari")
# cars.insert("Jaguar")  
# print(cars)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
#---------------------------------------

if __name__ == '__main__' :
    print("Input Strings (type stop to stop): ")
    word = input()
    user_trie = Trie()
    while word.lower() != "stop" :
        user_trie.insert(word)
        word = input()

    print("\nYour Trie: ")
    print(user_trie)
    print("Longest Common Prefix: {}".format(user_trie.longest_common_prefix()))