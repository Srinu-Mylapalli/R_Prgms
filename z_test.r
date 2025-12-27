#function to perform a z-test
z_test<-function(x,mu,sigma,alternative="two.sided"){
	#x:sample data
	#mu:hypothesized population mean
	#sigma:population standard deviation(known)
	#alternative : type if test ("two.sided","less","greater")
	#sample size
	n<-length(x)
	z_stat<-(x_bar-mu/sigma/sqrt(n))
	#p_value calculation
	if(alternative=="two.sided"){
		p_value<-2*(1-pnorm(abs(z_stat)))
	}
	else if(alternative == "less"){
		p_value<-pnorm(z_stat)
	}
	else{
		stop("Invalid alternative hypothesis. use 'two.sided','less',or 'greater'")
	}
	#Result
	list(
	     z_statistic=z_stat,
	     p_value=p_value,
	     conclusion=if else (p_value<0.05,"Reject the null hypotjesis","fail to reject the null hypothesis")
}

#Example usage of the z_test function
#hypothesis:Test  of the mean weight is 70 (mu=70)
#known population standard deviation is 10 (sigma=10)
#sample data
sample_data<-c(72,68,74,70,71,69,63,67,75,70)
#perform z-test
result<-z_test(sample_data,mu=70,sigma=10,alternative="two.sided")
#print results
print(result)
