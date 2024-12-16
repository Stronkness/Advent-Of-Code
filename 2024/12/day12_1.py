from collections import defaultdict

def calculate_total_cost(regions):
    def calculate_region_area(region):
        return len(region)  # The area is the number of plots in the region

    def calculate_region_perimeter(region):
        region_set = set(region)
        perimeter = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for x, y in region:
            for dx, dy in directions:
                neighbor = (x + dx, y + dy)
                if neighbor not in region_set:  # If the neighbor is outside the region
                    perimeter += 1
        
        return perimeter

    total_cost = 0

    for _, region_list in regions.items():
        for region in region_list:
            area = calculate_region_area(region)
            perimeter = calculate_region_perimeter(region)
            total_cost += area * perimeter
    
    return total_cost

def find_regions(grid):
    rows, cols = len(grid), len(grid[0])
    visited = set()
    regions = defaultdict(list)
    
    def in_bounds(x, y):
        return 0 <= x < rows and 0 <= y < cols
    
    def dfs(x, y, indicator):
        stack = [(x, y)]
        region = []
        
        while stack:
            cx, cy = stack.pop()
            if (cx, cy) in visited:
                continue
            visited.add((cx, cy))
            region.append((cx, cy))
            
            # Check neighbors (up, down, left, right)
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = cx + dx, cy + dy
                if in_bounds(nx, ny) and (nx, ny) not in visited and grid[nx][ny] == indicator:
                    stack.append((nx, ny))
        
        return region
    
    for i in range(rows):
        for j in range(cols):
            if (i, j) not in visited:
                indicator = grid[i][j]
                region = dfs(i, j, indicator)
                regions[indicator].append(region)
    
    return regions


grid = [[p for p in patch] for patch in open("small.in").read().split("\n")]
regions = find_regions(grid)
cost = calculate_total_cost(regions)
print(cost)
