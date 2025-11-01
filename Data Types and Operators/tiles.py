tile_dimensions_1 = 9 * 7
tile_dimensions_2 = 5 * 7
rate = 6 # tiles comes in packages of 6

tot_tile_dimensions = tile_dimensions_1 + tile_dimensions_2 

print("the total tiles needed are : ", tot_tile_dimensions) # the total tiles needed.

tiles_bought = 17 * rate
tiles_leftover = tiles_bought - tot_tile_dimensions
print("tiles left: ", tiles_leftover)

