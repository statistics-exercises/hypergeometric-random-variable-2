# Multiple choices with replacement

The choice function that you wrote in the previous exercise simply generated a Bernoulli random variable with parameter `R/N`. The problem was thus rather straightforward. 

When these choice problems are set we are supposed to assume that the probabilities of picking each ball are identical and that the classical interpretation holds.  The probability of picking a particular ball or one of a set of balls of a particular colour is thus simply a Bernoulli random variable. 

In the remainder of this exercise, we will consider what happens when we pick multiple balls from the urn.  Our random variable will thus measure the number of green balls that we pull out from the urn when we make our multiple selections,  Importantly there are two ways we can proceed in these types of experiments:

1. __with replacement__ - in this version of the experiment the balls are replaced in the urn after each selection.  When we come to make our selection there are thus always `N` balls in total and `R` green balls.
1. __without replacement__ - in this version of the experiment the balls are not returned to the urn after each selection.  The total number of balls in the urn (`N`) thus decreases by one after each selection.  The number of green balls may also decrease as the experiment proceeds.

Your task in this exercise is to complete the function called `choice_with_replacement` in the panel on the left.  This function takes three parameters `M` (the number of balls that are drawn from the urn, `N` (the total number of balls in the urn) and `R` (the number of green balls in the urn).  Notice that the number of red balls is `N-R` so the balls in the urn are either red or green.  Your function should return a random variable that measures the number of green balls that are drawn if the sampling is done with replacement.

When the function is completed and the code is run a graph showing the values of the random variable in 100 separate experients are performed.
