# Martingale strategy analysis
Analysis of an old betting strategy using a roulette system.

First of all, as many do, I start by saying that I do not recommend roulette nor any activities like gambling. The study was made to confirm if the Martingale system works. In theory it was a good way to get profit, but in practice is more complicated than it sounds.

# How the strategy works?
Simple.

If you **win** you bet the same amount of money like last time.\
If you **lose** you double the money and bet on the same color like last time.

The point is to bet on the same color everytime. Changing it will result in this strategy **not working**.

# What I wanted to do
I have implemented a program in python using Pillow and pyautogui, that can visually capture every needed element on the screen and then press click where it is requested, pointed by the user, automating the betting process.

Here is a link for a more detailed explanation by Daniel Oehm, _Martingale strategies don’t work, but we knew that – Simulation analysis in R_: http://gradientdescending.com/martingale-strategies-dont-work-but-we-knew-that-simulation-analysis-in-r/


# Conclusion
The strategy is not working. At some point there will be a great losing streak where all the money will be gone. Maybe there are some optimizations that can make it work in a long run, but at some point the result is still the same. Maybe there are already machine learning applications for that? 
