def estimate_house_sales_price(num_of_bedrooms, sqft, neighborhood):
  price = 0
# a little pinch of this
  price += num_of_bedrooms * 0.123
# and a big pinch of that
  price += sqft * 0.41
# maybe a handful of this
  price += neighborhood * 0.57
  return price
print(estimate_house_sales_price(3,2000,437500))
