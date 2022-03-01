# Program to print fibonacci series
# take input from the user
#num = as.integer(readline(prompt="Enter a number: "));

num1=0;
num2=1;
print(num1);
print(num2);

for(i in 1:5){
num3=num2+num1;
print(num3);
num1=num2;
num2=num3;	
}

