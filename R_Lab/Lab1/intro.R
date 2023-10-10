## Data Types 
## Vectos Lists Matrices Arrays Factors DataFrames

##Vectors
V = 10  # Atomic variable
V

V1 = c(10,20,30)
V1

apple <- c('red', 'green','yellow')
print(apple)
print(class(apple))

## [1] "red"    "green"  "yellow"
## [1] "character"

data1 = c(3,6,9,12,78,5,7,7)
datatext = c('Mon','Tue','Wed')
datatext  = c(datatext,'Thu','Fri')
print(datatext)
Data2 = c(data1, datatext)
print(Data2)

##  [1] "Mon" "Tue" "Wed" "Thu" "Fri"
##  [1] "3"   "6"   "9"   "12"  "78"  "5"   "7"   "7"   "Mon" "Tue" "Wed" "Thu" "Fri"

print(class(Data2))
## [1] "character"

print(class(data1))
## [1] "numeric"

#Using the vector() Function 
x <- vector('numeric',length = 10)
x


numbers = 1:10
print(numbers)


numbers <- seq(from = 0, to = 100, by = 20)
print(numbers)


v = seq(2,4,by = 0.4)
v

V = seq(1,4, length.out = 5)
V


#Accessing vector elements using the position 
t <- c("Sun","Mon", "Tue" ,"Wed" ,"Thu" ,"Fri","Sat")
u <- t[c(2,3,6)]
print(u)

#Accessing the vector elements using the logical indexing 
v <- t[c(TRUE,FALSE,FALSE,FALSE,FALSE,TRUE,FALSE)]
print(v)

## [1] "Sun" "Fri"

#Accessing the vector elements using negative indexing
x  = t[c(-2,-5)]
print(x)

## [1] "Sun" "Tue" "Wed" "Fri" "Sat"

#Accessing the vector elements using 0/1 indexing
y = t[c(0,1,0,0,1,1,0)]
print(y)

## [1] "Sun" "Sun" "Sun"

#Vector Manipulation
#Create two vectors
v1 <- c(3,7,5,0,11,8)
v2 <- c(3,5,7,33,2,1)

#Vector addition
add.result <- v1+v2
print(add.result)

## [1]  6 12 12 33 13  9

#vector subtraction
sub.result <- v1-v2
print(sub.result)
## [1]   0   2  -2 -33   9   7


#Vector Multiplication
multi.result <- v1*v2
print(multi.result)
## [1]  9 35 35  0 22  8


#Vector division
divi.result <- v1/v2
print(divi.result)
## [1] 1.0000000 1.4000000 0.7142857 0.0000000 5.5000000 8.0000000

mod.result = v1%%v2
print(mod.result)

## [1] 0 2 5 0 1 0

#Sort the element of the vector 
v <- c(3,8,4,5,0,11,-9,304)

sort.result <- sort(v)
print(sort.result)


#Sort the elements in the reverse order
revsort.result <- sort(v, decreasing = TRUE)
print(revsort.result)

m <- rep(v,each = 2)  #Repeat the each element twice
print(m)
##  [1]   3   3   8   8   4   4   5   5   0   0  11  11  -9  -9 304 304

print(min(v))
## [1] -9

print(max(v))
## [1] 304

print(sum(v))
## [1] 326

print(mean(v))
## [1] 40.75

print(sd(v))
## [1] 106.5347

print(which.min(v))
## [1] 7


