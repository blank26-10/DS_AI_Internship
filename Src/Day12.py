import matplotlib.pyplot as plt
plt.subplot(1,2,1)
categories = ['Electronics','Clothing','Home']
values = [300,450,200]
plt.bar(categories,values)
plt.title("Bar Chart")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.subplot(1,2,2)
sales = [100,243,354,453,544]
months = [1,2,3,4,5]
plt.plot(sales,months)
plt.title("Line Chart")
plt.xlabel("Sales")
plt.ylabel("Months")
plt.tight_layout()
plt.show()
