observed<-c(50,30,20)
expected<-c(40,40,20)
chi_square<-sum((observed-expected)^2/expected)
df<-length(observed)-1
p_value<-pchisq(chi_square,df,lower.tail=FALSE)
cat("Chi_square statistic: ",chi_square,"\n")
cat("degrees of freedom: ",df,"\n")
cat("p_value: ",p_value,"\n")
alpha<-0.05
if(p_value<alpha){
	cat("conclusion: reject the null hypothesis (observed does not match expected)\n")
}
else{
	cat("conclusion: fail to reject the null hypothesis (observed mathes expected)\n")
}

