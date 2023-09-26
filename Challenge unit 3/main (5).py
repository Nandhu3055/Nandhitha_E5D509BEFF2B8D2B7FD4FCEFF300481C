def LinearSearchProduct(productList,target):
  ind = []
  for index,product in enumerate(productList):
    if product == target:
      ind.append(index)
  return ind

product = ["apple","banana","pineapple","apple","kiwi","apple"]
target = "apple"
print(LinearSearchProduct(product,target))