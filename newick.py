class Tree:
    def __init__(self, name, children):
        self.name = name
        self.children = children

def modifiedSplit(string):
        result = []
        curr = ""
        inside = 0
        commas = 0
        for i in range(len(string)):
            c = string[i]
            if c == ',' and not inside:
                commas += 1
            else:
                if c == "(":
                    inside += 1
                if c == ")":
                    inside -= 1
        numberOfChildren = commas + 1
        for i in range(len(string)):
            c = string[i]
            if i == len(string) - 1 and c != ",":
                 curr += c
                 result.append(curr)
                 continue
            if c == ',' and not inside:
                result.append(curr)
                curr = ""
            else:
                curr += c
                if c == "(":
                    inside += 1
                if c == ")":
                    inside -= 1
        childrenToAdd = numberOfChildren - len(result)
        for _ in range(childrenToAdd):
            result.append(str(Tree.tree_id))
            Tree.tree_id += 1
        return result

def buildTree(tree):
        childrenStart = tree.find("(")
        childrenEnd = tree.rfind(")")
        # single node tree
        if childrenStart == -1:
            treeName = tree
            if not treeName:
                treeName = None
            return Tree(treeName, [])
        
        rootName = tree[childrenEnd + 1:].replace(";", "")
        if not rootName:
            rootName = None
        root = Tree(rootName, None)
        children = [buildTree(child) for child in modifiedSplit(tree[childrenStart + 1:childrenEnd])]
        root.children = children
        return root

def preorder(tree):
    print(tree.name)
    if not tree.children:
        return
    for child in tree.children:
        preorder(child)

# preorder(buildTree("(dog,((elephant,mouse),robot),cat);"))