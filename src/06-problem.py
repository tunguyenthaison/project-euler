from timeit import default_timer as timer


if __name__ == "__main__":
    start = timer() 
    n = 100
    ans = (n * (n+1) / 2) ** 2 - (n * (n + 1) * (2 * n + 1) / 6)
    print(int(ans))
    end = timer()
    print(end - start)    
    