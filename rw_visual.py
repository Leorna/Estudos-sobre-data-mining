from random_walk import RandomWalk


#continues creating new walks while the progrem is active
while True:
    #creates a random walk and plot the poits
    rw = RandomWalk()
    rw.fill_walk()
    rw.plot_points()
    rw.plot_line()
    
    keep_running = input('Make another walk? (y/n): ')
    if keep_running.lower() == 'n':
        break