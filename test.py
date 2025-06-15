def modifiedSplit(string):
        result = []
        curr = ""
        inside = 0
        for i in range(len(string)):
            c = string[i]
            if i == len(string) - 1:
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
        return result

print(modifiedSplit("A,(B,(C,(D,E)de)cde)bcde"))