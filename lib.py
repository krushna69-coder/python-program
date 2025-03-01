# import matplotlib.pyplot as plt

# x = [1, 2, 3, 4, 5]  
# y = [2, 4, 6, 8, 10]  

# plt.plot(x, y, marker='o', color='b', linestyle='--', label='Line 1')

# plt.title('Basic Plot Example')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')

# plt.legend()
# plt.show()


# import matplotlib.pyplot as plt

# x = [1, 2, 3, 4, 5]
# y = [5, 7, 6, 8, 7]
# sizes = [20, 50, 80, 200, 100]  
# colors = ['red', 'blue', 'green', 'purple', 'orange']  


# plt.scatter(x, y, s=sizes, c=colors, alpha=0.8, edgecolor='black')

# plt.title('Scatter Plot Example')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')

# plt.show()


# import matplotlib.pyplot as plt

# categories = ['A', 'B', 'C', 'D']
# values = [4, 7, 1, 8]

# plt.bar(categories, values)

# plt.xlabel('Categories')
# plt.ylabel('Values')
# plt.title('Simple Bar Plot')
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
# x=np.random.normal(170,10,250)
# plt.hist(x)
# plt.show()

import numpy as np
import matplotlib.pyplot as plt
y=np.array([35,25,25,15])
plt.pie(y)
plt.show()