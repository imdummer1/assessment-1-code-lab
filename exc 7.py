def Count(start, end, step):
    print(f"\nFrom {start} to {end} by {step}:\n")
    for index in range(start, end + step, step):
        print(index)
        
# from 0 to 50 by 1 step
Count(0, 50, 1) 
# from 50 to 0 by -1 step
Count(50, 0, -1)
# from 30 to 50 by 1 step
Count(30, 50, 1)
# from 50 to 10 by -2 step
Count(50, 10, -2)
# from 100 to 200 by 5 step
Count(100, 200, 5)