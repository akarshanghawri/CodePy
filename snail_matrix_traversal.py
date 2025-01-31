def snail(snail_map):
    if not snail_map or not snail_map[0]:
        return []
    
    l = []  
    n = 0  # Start index
    m = len(snail_map)  # Size of the square matrix

    def right(n, m):
        for i in range(n, n + 1):  
            for j in range(n, m):  
                l.append(snail_map[i][j])

    def down(n, m):
        for i in range(n + 1, m):  
            for j in range(m - 1, m):  
                l.append(snail_map[i][j])

    def left(n, m):
        for i in range(m - 1, m):  
            for j in range(m - 2, n - 1, -1):  
                l.append(snail_map[i][j])

    def up(n, m):
        for i in range(m - 2, n, -1):  
            for j in range(n, n + 1):  
                l.append(snail_map[i][j])

    def recursive(n, m):
        if n >= m:  #stops recursion
            return
        right(n, m)  
        down(n, m)   
        left(n, m)   
        up(n, m)     
        recursive(n + 1, m - 1)  

    recursive(n, m)
    return l