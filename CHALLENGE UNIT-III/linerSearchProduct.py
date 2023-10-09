def linerSearchProduct(ProductList,targetproduct):
    indices=[]
    for index,product in enumerate(ProductList):
        if product == targetproduct:
            indices.append(index)
    return indices
products=["shoes","boot","loofer","shoes","sandal","shoes"] 
target="shoes"  
target2="apple"  
result=linerSearchProduct(products,target) 
print(result)
