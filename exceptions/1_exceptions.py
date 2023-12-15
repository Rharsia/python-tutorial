while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")


try:
    numerator = 10
    denominator = 0

    result = numerator/denominator

    print(result)
except:
    print("Error: Denominator cannot be 0.")


# multiple except blocks
try:
    
    even_numbers = [2,4,6,8]
    print(even_numbers[5])

except ZeroDivisionError:
    print("Denominator cannot be 0.")
    
except IndexError:
    print("Index Out of Bound.")


try:
    8/0
except ZeroDivisionError:
    print("cant divide by zero")


try:
    num = int(input("Enter a number: "))
    assert num % 2 == 0
except:
    print("Not an even number!")
else:
    reciprocal = 1/num
    print(reciprocal)


# Finally will always execute whether there was an exception or not
try:
    numerator = 10
    denominator = 2

    result = numerator/denominator

    print(result)
except:
    print("Error: Denominator cannot be 0.")
    
finally:
    print("This is finally block.")


try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

# else, will run when nothings goes wrong
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")