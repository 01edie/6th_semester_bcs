num = as.integer(readline(prompt="Enter a number:"))
a = 0
b = 1
if(num<0){
print("Invalid Range")
}else{
cat(a,b," ")
for(i in 1:(num-2)){
sum=a+b
cat(sum," ")
a<-b
b<-sum
}
}