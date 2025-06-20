class Tree:
    def __init__(self, name, children, parent):
        self.name = name
        self.children = children
        self.parent = parent # tuple (pointerToParent, edgeWeightToParent)

    nameToNode = {}
    ids = 0

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

def buildTree(tree: str, parent):
        childrenStart = tree.find("(")
        childrenEnd = tree.rfind(")")
        # single node tree
        if childrenStart == -1:
            treeName = tree
            if not treeName:
                treeName = str(Tree.ids)
                Tree.ids += 1
            newTree = Tree(treeName, [], parent)
            Tree.nameToNode[treeName] = newTree
            return newTree
        
        rootName = tree[childrenEnd + 1:].replace(";", "")
        if not rootName:
            rootName = str(Tree.ids)
            Tree.ids += 1
        root = Tree(rootName, None, parent)
        if rootName is not None:
            Tree.nameToNode[rootName] = root
        # children = [buildTree(child) for child in modifiedSplit(tree[childrenStart + 1:childrenEnd])]
        children = []
        for child in modifiedSplit(tree[childrenStart + 1:childrenEnd]):
            childStr, weight = child.rsplit(":", 1)
            children.append((buildTree(childStr, (root, float(weight))), float(weight)))   
        # children = [
        #     (buildTree(childStr), float(weight))
        #     for child in modifiedSplit(tree[childrenStart + 1:childrenEnd])
        #     for childStr, weight in [child.split(":")]
        # ]
        root.children = children
        return root

def find(name: str):
    return Tree.nameToNode[name]


def preorder(tree):
    print(tree.name)
    if not tree.children:
        return
    for child in tree.children:
        print(child[1])
        preorder(child[0])

# preorder(buildTree("(dog:42,cat:33);", (None, 0)))