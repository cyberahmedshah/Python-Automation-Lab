def greet(fx):
  def wrapper():
   print("Hello Sir")
   print(f"The temperature in degree is {fx():.2f}") 
   print("Thanks for using our tool")
  return wrapper


@greet
def celsuis():
  a=float(input("Enter the temperature in fahrenheit: "))
  b=a-32
  return b/1.8

celsuis()




