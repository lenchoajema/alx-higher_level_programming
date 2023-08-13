import sys

if __name__ == "__main__":
    argv = sys.argv[1:]  # Exclude the script name itself
    
    num_args = len(argv)
    
    if num_args == 0:
        print("Number of argument(s): 0.")
    elif num_args == 1:
        print(f"Number of argument(s): 1: {argv[0]}.")
    else:
        print(f"Number of argument(s): {num_args}: {', '.join(argv)}.")
    
    if num_args > 0:
        for i, arg in enumerate(argv, start=1):
            print(f"{i}: {arg}")
