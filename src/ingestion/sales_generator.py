import random
import time

def generate_sales():

    data = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "product_id": random.randint(1, 100),
        "amount": round(random.uniform(10, 500), 2)
    }

    print("Generated sale:", data)

    return data