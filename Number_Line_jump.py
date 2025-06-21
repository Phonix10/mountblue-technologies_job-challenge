def kangaroo(x1, v1, x2, v2):
    # If they start at the same place and jump same distance
    if x1 == x2 and v1 == v2:
        return "YES"
    
    # Prevent division by zero and check if the positions converge after same number of jumps
    if v1 != v2:
        n = (x2 - x1) / (v1 - v2)
        # They meet if n is a positive integer
        if n >= 0 and n.is_integer():
            return "YES"
    
    return "NO"