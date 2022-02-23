salary<-readline("Enter the salary:")
salary<-as.integer(salary)
bonus<-readline("Enter the bonus:")
bonus<-as.integer(bonus)
if (salary>20000)
{
  print(paste(
    "salary=",salary+bonus))
}