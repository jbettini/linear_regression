import pandas as pd
import numpy as np

def main():
    try:

        try:
            thetas = pd.read_csv('thetas.csv')
            theta0 = thetas['theta0'][0]
            theta1 = thetas['theta1'][0]
        except FileNotFoundError:
            print("No model thetas init as 0")
            theta0, theta1 = 0.0, 0.0

        while True:
            user_input = input("Entrez le kilometrage : ")
            try:
                input_as_int = float(user_input)
            except BaseException:
                continue
            break

    except TypeError as e:
        print(f"TypeError: {str(e)}")
    except BaseException as e:
        print(f"An exception has been caught: {type(e).__name__} - {str(e)}")


if __name__ == "__main__":
    main()