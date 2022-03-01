# Program to check if the input number is even or odd
# take input from the user
num = as.integer(readline(prompt="Enter a number: "))
if(num%%2==0){
print(paste(num,"is even number"))
}else{
print(paste(num,"is odd number"))
}
