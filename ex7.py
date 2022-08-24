#task 1
city="London"
print(city)
#task 2
city="Berlin"
population=3645000
print(city+ ": " +str(population))
#Task 3
city="London"
population=9000000
my_city=city.isalpha()

print("city: "+city , "("+ str(my_city)+")"  )
print("population: "+str(population))
#Task 4
text="Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital."
my_text1=text.index("capital")
print("capital"+":",str(my_text1))
#Task 5
text="Berlin straddles the banks of the Spree, which flows into the Havel (a tributary of the Elbe) in the western borough of Spandau."
my_text2=text.split()
print(my_text2)
#Task 6
text="Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital."
my_text4=text.replace("capital","capital of Germany")
print(my_text4)
