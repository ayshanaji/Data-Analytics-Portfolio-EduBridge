sp<-readline("Enter the selling price:")
sp<-as.integer(sp)
cp<-readline("Enter the cost price:")
cp<-as.integer(cp)
if (sp>cp)
{
  print("profit")
}else
{
  print("loss")
}