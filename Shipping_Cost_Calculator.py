# Shipping Cost Calculator

## Input package weight and shipping rate
weight = float(input("Enter the package weight in kilograms: "))
rate = float(input("Enter the shhipping rate per kilogram: "))

## Calulate shipping cost
shipping_cost = weight * rate

## Display the result
print(f"Sipping Cost: {shipping_cost} USD")
