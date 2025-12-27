# Function to perform a z-test
z_test <- function(x, mu, sigma, alternative = "two.sided") {
  # x: sample data
  # mu: hypothesized population mean
  # sigma: population standard deviation (known)
  # alternative: "two.sided", "less", or "greater"
  
  n <- length(x)
  x_bar <- mean(x)
  
  # Z statistic
  z_stat <- (x_bar - mu) / (sigma / sqrt(n))
  
  # P-value calculation
  if (alternative == "two.sided") {
    p_value <- 2 * (1 - pnorm(abs(z_stat)))
  } else if (alternative == "less") {
    p_value <- pnorm(z_stat)
  } else if (alternative == "greater") {
    p_value <- 1 - pnorm(z_stat)
  } else {
    stop("Invalid alternative hypothesis. Use 'two.sided', 'less', or 'greater'.")
  }
  
  # Conclusion
  conclusion <- ifelse(
    p_value < 0.05,
    "Reject the null hypothesis",
    "Fail to reject the null hypothesis"
  )
  
  # Return results
  list(
    z_statistic = z_stat,
    p_value = p_value,
    conclusion = conclusion
  )
}

# Example usage
sample_data <- c(72, 68, 74, 70, 71, 69, 63, 67, 75, 70)
result <- z_test(sample_data, mu = 70, sigma = 10, alternative = "two.sided")
print(result)

