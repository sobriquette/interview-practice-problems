class Solution:
    def find_sources(self, grid):
        """
            Get list of food locations and Ben's location
        """
        sources = set()
        front = None
        
        for r in grid:
            for c in r:
                if c == '*':
                    front = (r, c)
                elif c == '#':
                    sources.add((r, c))
        
        return [sources, front]
    
    def is_valid_move(self, r, c, grid):
        """
            Check if we can move here later
        """
        if r < 0 or r >= len(grid) or \
            c < 0 or c >= len(grid[0]):
                return False
        if grid[r][c] == 'X':
            return False
        
        return True
        
    def get_paths(self, front, grid):
        """
            Get the next set of paths to check
        """
        next_front = set()
        r, c = front[0], front[1]
        if self.is_valid_move(r + 1, c, grid):
            next_front.add(r + 1, c)
        if self.is_valid_move(r - 1, c, grid):
            next_front.add(r - 1, c)
        if self.is_valid_move(r, c + 1, grid):
            next_front.add(r, c + 1, grid)
        if self.is_valid_move(r, c - 1, grid):
            next_front.add(r, c - 1, grid)
        
        return next_front
    
    def getFood(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # get list of locations of food sources and ben
        source_locs, front = self.find_sources(grid).split()
        min_path = float('inf')
        
        # from each food location and from Ben's location
        # do a bidirectional BFS to see if both ever meet
        # if they do, we have a valid path
        # get the length of the path and see if it's the smallest
        for source in source_locs:
            front_paths = get_paths(front, grid)
            source_paths = get_paths(source, grid)
            path_len = 0
            while len(front_paths) and len(source_paths):
                if front_paths & source_paths:
                    path_len = len(front_paths & source_paths)
                else:
                    pass
        
        
        
        
        
        
        
        
        