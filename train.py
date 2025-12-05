import pandas as pd
import numpy as np

def normalize(array):
    return (array - array.min()) / (array.max() - array.min())

def main():
    try:
        data = pd.read_csv('data.csv')

        km = np.array(data["km"])
        price = np.array(data["price"])

        m = len(km) # total data

        assert(m == len(b))

        w0 = 0.0 # theta0 km
        w1 = 0.0 # theta1 price
        learning_rate = 0.01 # Alpha
        epochs = 1000 # Nombre d'itérations
        
        km_normalized = normalize(km)
        price_normalized = normalize(price)

        for epoch in range(epochs):
            

    except TypeError as e:
        print(f"TypeError: {str(e)}")
    except BaseException as e:
        print(f"An exception has been caught: {type(e).__name__} - {str(e)}")


if __name__ == "__main__":
    main()