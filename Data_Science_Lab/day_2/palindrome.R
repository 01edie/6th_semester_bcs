# Program to check if the input number is palindrome or not
# take input from the user
#num = as.integer(readline(prompt="Enter a number: "));
num=121;
num1=num;

sum=0;
while(num!=0){
sum=sum*10+(num%%10);
num=num%/%10;

}

if(sum==num1){
print(paste(sum,"is a palindrome number"))
}else{
print(paste(sum,"is not a palindrome number"))
}

