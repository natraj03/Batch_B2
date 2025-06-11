# reverse of a strring

def reverse_str(inp1):
    result = ""
    for char in str(inp1):
        result = char + result
    return result

def palendrome(inp1):
    revStr = reverse_str(inp1)
    if revStr == inp1:
        return True
    else:
        return  False
