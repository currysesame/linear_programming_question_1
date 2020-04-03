# linear_programming_question_1

The question is come from: 來源：奇點無限股份有限公司-演算法工程師筆試題目
The original site is: https://docs.google.com/document/d/1mhKLc4LEIVvP0jUudIO2_WpOFF7knHA6Agmgbi6if3E/edit

One man sells some food on the street. The length of the street in the town is 4 Km. He walk 100 m can gain 20 dollars on average. 

At the first 1 km. It costs 5 physical strengths for this man each 100 m.
At the second km. It costs 10 physical strengths for this man each 100m.
The third 1 km. It costs 15 physical strengths for this man each 100m.
The last 1 km. It costs 20 physical strengths for this man each 100m.

After walking 4 km can reach the other side of this town, this man would go back to home immediately. Of course, he can go home any time as he want.
There would not cost any physical strength and no gain for money after he decided to go home.
On the tour, there are some places crowded of people. The positions are at the 500m, 1000m, 2000m, 3000m and 4000m. If do some effort, he can gain some extra money. If not, he still can gain a little money.

At 500m, he can cost 20 physical strengths to sell his food for 60 dollars. Otherwise, he can gain only 20 dollars.
At 1000m, he can cost 40 physical strengths to sell his food for 120 dollars. Otherwise, he can gain only 40 dollars.
At 2000m, he can cost 100 physical strengths to sell his food for 300 dollars. Otherwise, he can gain only 60 dollars.
At 3000m, he can cost 100 physical strengths to sell his food for 300 dollars. Otherwise, he can gain only 60 dollars.
At 4000m, he can cost 120 physical strengths to sell his food for 360 dollars. Otherwise, he can gain only 60 dollars. 

He want to minimize the costs of his physical strength, such that after one week, he can gain over 10,000 dollars. Please use the integer programming to help him solve this problem. Each movement is 100m for one unit. Need to write down the function, constraints and the variables.


The following is my solution:

I would like to let the total steps from 41 steps to 5 steps. Since there are too many things have to analyze. But fortunately, if only check the 500m, 1000m, 2000m, 3000m and 4000m. For these five points, the choices of do the effort or not are only 32 types of situations. So there are only 32 * 5 pairs of data. And the other hand, there are some duplications. And there are some cases not match the gain if do the efforts. So delete these duplications and the no worth to do cases. Finally, only remain 34 cases. And the best thing is that in this question, if sorted the cases. There are the monotonic sequences for the efforts and the gains. So we can use the continuality method to solve this question. Use gradient descent method is one of the best choices in this situation. 
The answer is as follow:

|  | Gain | Cost | Steps | 500m | 1000m | 2000m | 3000m | 4000m |
| ----- | ------ | ------ | ------ | ----- | ----- | ----- | ----- | ----- |
| Day 1 | 1940 | 880 | 40 | 1 | 1 | 1 | 1 | 1 |
| Day 2 | 1340 | 540 | 30 | 0 | 1 | 1 | 1 | 0 |
| Day 3 | 1340 | 540 | 30 | 0 | 1 | 1 | 1 | 0 |
| Day 4 | 1300 | 520 | 30 | 1 | 0 | 1 | 1 | 0 |
| Day 5 | 1380 | 560 | 30 | 1 | 1 | 1 | 1 | 0 |
| Day 6 | 1380 | 560 | 30 | 1 | 1 | 1 | 1 | 0 |
| Day 7 | 1340 | 540 | 30 | 0 | 1 | 1 | 1 | 0 |
| Total | 10020 | 4140 | 220 | 4 | 6 | 7 | 7 | 1 |

1 = stay there and do some effort to gain some money.
0 = not stay there and gain a little money.
