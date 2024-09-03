"""
Question 2

You won’t get caught if you hide behind someone.”
Sang-Woo advises Gi-Hun to hide behind someone to avoid getting shot.
Gi-Hun follows Sang-Woo's advice and hides behind Ali, who saved his life earlier. Gi-Hun and Ali 
both have the same height, K. Many players saw this trick and also started hiding behind Ali.
Now, there are N players standing between Gi-Hun and Ali in a straight line, with the ith player having height Hi. 
Gi-Hun wants to know the minimum number of players who need to get shot so that Ali is visible
in his line of sight.
"""

def min_shots_to_visible(N, K, heights):
    shots_needed = 0
    
    for height in heights:
        if height > K:
            # If the player's height is greater than K, they need to be shot
            shots_needed += 1
            
    return shots_needed

def main():
    T = int(input())
    
    results = []
    for _ in range(T):
        N, K = map(int, input().split())
        heights = list(map(int, input().split()))
        
        results.append(min_shots_to_visible(N, K, heights))
    
    print("Result:")
    for result in results:
        print(result)


if __name__ == "__main__":
    main()
