tweet = {
	"user" : "bryanclark90",
	"text" : "Go Cougs!",
	"rt_cnt" : 100,
	"hashtags" : ["#data", "#GoCougs"]
}

tweet_keys = tweet.keys() #list of keys
tweet_values = tweet.values() 
tweet_items = tweet.items()

print("Keys: ")
print(tweet_keys)
print("Values: ") 
print(tweet_values)
print("Items: ")
print(tweet_items)

even_number = [x for x in range(5) if x%2 == 0]
squares = [x*x for x in range(5)]

print(even_number)
print(squares)

zeroes = [0 for _ in even_number]

print(zeroes)

increasing_pairs = [(x,y)
		    for x in range(10)
		    for y in range(x+1, 10)]

print(increasing_pairs)

from matplotlib import pyplot as plt

years = [1950,1960,1970,1980,1990,2000,2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]
#create a line chart , years on x axis and gdp on y axis
plt.plot(years, gdp, color='blue', marker='o', linestyle='solid')

#add a title
plt.title("Nominal GDP")

#add a label to the y-axis
plt.ylabel("Billions of $")
#x-axis ?
plt.xlabel("Year")
#plot that shit
plt.show()

