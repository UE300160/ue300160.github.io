#!/usr/bin/env python

# fields and fences

from util import read_input

def find_crops(farm):
    catalogue = set()
    for lane in farm:
        for field in lane:
            catalogue.add(field)
    return list(catalogue)

def find_plot(farm, i, j, crop, plot):
    # check if we're out of bounds
    if i < 0 or i >= len(farm) or j < 0 or j >= len(farm[0]):
        return
    # check if we've already been here
    if [i, j] in plot:
        return
    # check if this is the right crop
    if farm[i][j] != crop:
        return
    plot.append([i, j])
    find_plot(farm, i+1, j, crop, plot)
    find_plot(farm, i-1, j, crop, plot)
    find_plot(farm, i, j+1, crop, plot)
    find_plot(farm, i, j-1, crop, plot)

def find_all_plots(farm, crop):
    plots = []
    crop_locations = []
    for i, lane in enumerate(farm):
        for j, field in enumerate(lane):
            if field == crop:
                if [i, j] in crop_locations:
                    continue
                plot = []
                find_plot(farm, i, j, crop, plot)
                plots.append(plot)
                crop_locations += plot
    return plots

def perimeter_contribution(point, farm):
    i, j = point
    crop = farm[i][j]
    perimeter = 0
    if i == 0 or farm[i-1][j] != crop:
        perimeter += 1
    if i == len(farm) - 1 or farm[i+1][j] != crop:
        perimeter += 1
    if j == 0 or farm[i][j-1] != crop:
        perimeter += 1
    if j == len(farm[0]) - 1 or farm[i][j+1] != crop:
        perimeter += 1
    return perimeter

def perimeter(plot, farm):
    total = 0
    for point in plot:
        total += perimeter_contribution(point, farm)
    return total

def area(plot):
    return len(plot)

# given a set of coordinates, find how many sides the resulting object has


def main():
    farm = read_input('../aoc_data/day12_test1.txt')
    crops = find_crops(farm)
    fencing_costs = 0
    for crop in crops:
        plots = find_all_plots(farm, crop)
        crop_perimeter = 0
        for plot in plots:
            sides(plot)
            # crop_perimeter = perimeter(plot, farm)
            # crop_perimeter = sides(plot, farm)
            # crop_area = area(plot)
            # fencing_costs += crop_perimeter * crop_area

    # print(fencing_costs)

if __name__ == "__main__":
    main()