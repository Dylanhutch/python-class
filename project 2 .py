#first you have to give the user a input to give you a number for your Probability formula
red_dots = float(input("Enter amount red dots: "))
blue_dots = float(input("Enter amount of blue dots: "))
purple_dots = float(input("Enter amount of purple dots: "))
#now you have to find the total amount of dots
total = red_dots + blue_dots + purple_dots
#now you get the total of all the colors 
total_of_red_dots = total - (blue_dots + purple_dots)
total_of_blue_dots = total - (red_dots + purple_dots)
total_of_purple_dots = total - (red_dots + blue_dots)
#now you do the Probability formula on all of the dots
chances_of_geting_purple = total_of_purple_dots/total
chances_of_geting_blue = total_of_blue_dots/total
chances_of_geting_red = total_of_red_dots/total
#and you print you chances of geting the diffrent colors
print("The total amout of dots is " + str(total))
print("The total amount of red dots is: " + str(chances_of_geting_red))
print("The total amount of blue dots is: " + str(chances_of_geting_blue))
print("The total amount of purple dots is: " + str(chances_of_geting_purple))