year<-readline("Enter the year:")
year<-as.integer(year)
if (year%%4==0)
{
  print("Leap year")
}else
{
  print("Not a leap year")
}