# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 20:43:42 2017

@author: ariahklages-mundt
"""


n = 3
m = 9
cells = []
cells.append(list('SCSSSSSSC'))
cells.append(list('SCSCSSSSC'))
cells.append(list('SSSSSSSSC'))


def adj_cells(i,j):
    adj = []
    temp = [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]
    for cell in temp:
        if cell[0] in range(n) and cell[1] in range(m):
            adj.append(cell)
    return adj

def adj_cells_region(region):
    adj = []
    for cell in region:
        adj = adj + adj_cells(cell[0],cell[1])
    adj = list(set(adj)-set(region))
    return adj

def find_regions(cells):
    all_regions = []
    for i in range(n):
        for j in range(m):
            if cells[i][j] == 'C':
                region = []
                region.append((i,j))
                adj = adj_cells(i,j)
                for cell in adj:
                    if cells[cell[0]][cell[1]] == 'C':
                        region.append((cell[0],cell[1]))
                new = 1
                new_all_regions = []
                for region2 in all_regions:
                    if len(list(set(region2) & set(region))) != 0:
                        region = list(set(region2 + region))
                    else:
                        new_all_regions.append(region2)
                new_all_regions.append(region)
                all_regions = new_all_regions[:]
    return all_regions

def affected_area(all_regions):
    affected_areas = []
    num_cells = []
    for region in all_regions:
        adj = adj_cells_region(region)
        affected = []
        for cell in adj:
            if cells[cell[0]][cell[1]] == 'S':
                affected.append(cell)
        affected_areas.append(affected)
        num_cells.append(len(affected))
    return affected_areas, num_cells

def quarantine(region,cells):
    for cell in region:
        cells[cell[0]][cell[1]] = 'Q'
    walls_added = 0
    for cell in region:
        adj = adj_cells(cell[0],cell[1])
        for cell2 in adj:
            if cells[cell2[0]][cell2[1]] == 'S':
                walls_added += 1
    return walls_added
        
def spread_contagion(affected_areas,cells):
    for affected in affected_areas:
        for cell in affected:
            cells[cell[0]][cell[1]] = 'C'
    return
        

walls = 0
all_regions = find_regions(cells)
affected_areas, num_cells = affected_area(all_regions)
while len(affected_areas) > 0:
    max_ind = num_cells.index(max(num_cells))
    walls_added = quarantine(all_regions[max_ind],cells)
    walls = walls + walls_added
    del affected_areas[max_ind]
    spread_contagion(affected_areas,cells)
    
    all_regions = find_regions(cells)
    affected_areas, num_cells = affected_area(all_regions)

print(walls)




                