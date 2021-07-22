import pandas as pd
import matplotlib.pyplot as plt

url='https://drive.google.com/file/d/0B6GhBwm5vaB2ekdlZW5WZnppb28/view?usp=sharing'
url2='https://drive.google.com/uc?id=' + url.split('/')[-2]
df = pd.read_csv(url2)

print(df.count)
print(df['age'])

print(df.head()) 

  
# x axis values
x = [1,2,3]
# corresponding y axis values
y = [2,4,1]

plt.plot(df["age"], df["cheq_balance"])
  
# plotting the points 
plt.plot(x, y)
  
# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
  
# giving a title to my graph
plt.title('My first graph!')
  
# function to show the plot
plt.show()