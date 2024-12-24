def cal_area(height,base,shape):
    if shape=="triangle":
        area=(1/2)*base*height
    if shape=="rectangle":
        area=height*base
    return area

print("area of triangle",cal_area(5,6,"triangle"))
print("area of rectangle",cal_area(4,5,"rectangle"))
