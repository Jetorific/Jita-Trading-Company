#Ship Warp Speed, Distance, and Jump Values are simply a placeholder, eventually we'll pull them from ship info and route

distance = 68 #Au
warp_speed = 1.5 #Au / sec
num_of_jumps = 6
jump_time = 6 #seconds / jump -- tested through an average across 4 jumps; it was also taken in the slow hauler, so I'll test with something faster later


trip_time = (distance / warp_speed) + (num_of_jumps * jump_time) #sec
