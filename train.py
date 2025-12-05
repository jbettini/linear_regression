import pandas as pd
import numpy as np


def normalize_array(array):
    return (array - array.min()) / (array.max() - array.min())


def get_real_theta1(w1, km, price):
    range_x = km.max() - km.min()
    range_y = price.max() - price.min()
    return (range_y * w1) / range_x


def get_real_theta0(w0, real_theta1, km, price):
    range_y = price.max() - price.min()
    return price.min() + (range_y * w0) - (real_theta1 * km.min())


def main():
    try:
        data = pd.read_csv('data.csv')

        km = np.array(data["km"])
        price = np.array(data["price"])

        m = len(km)             # total data

        assert (m == len(price))

        w0 = 0.0                # theta0 mileage
        w1 = 0.0                # theta1 price
        learning_rate = 0.01    # Alpha
        epochs = 5000           # Nombre d'itérations

        km_normalized = normalize_array(km)
        price_normalized = normalize_array(price)

        for epoch in range(epochs):
            total_errors_theta0 = 0.0
            total_errors_theta1 = 0.0
            for current_data in range(m):
                pred = w0 + (w1 * km_normalized[current_data])
                goal_pred = price_normalized[current_data]

                error_pure = pred - goal_pred

                total_errors_theta0 += error_pure
                total_errors_theta1 += error_pure * km_normalized[current_data]

            w0 -= learning_rate * (total_errors_theta0 / m)
            w1 -= learning_rate * (total_errors_theta1 / m)

        real_theta1 = get_real_theta1(w1, km, price)
        real_theta0 = get_real_theta0(w0, real_theta1, km, price)

        df = pd.DataFrame({'theta0': [real_theta0], 'theta1': [real_theta1]})
        df.to_csv('thetas.csv', index=False)
        print("thetas saved !")

    except TypeError as e:
        print(f"TypeError: {str(e)}")
    except BaseException as e:
        print(f"An exception has been caught: {type(e).__name__} - {str(e)}")


if __name__ == "__main__":
    main()
