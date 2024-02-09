# Market Turning Point Analysis Program
This is a learning project and a Work In Progress (WIP).

In his [personal blog](https://mrzepczynski.blogspot.com/2020/06/turning-points-kill-trend-following.html), Mr. Mark Rzepczynski talks about the devastating impacts that market turning 
points can have for trend followers. A market with a high number of turning points will also represent a higher number in whipsaw losses, and consequently a lower number of long-term trends.

This tool was created with the purpose of helping traders analyze the number of turning points for any given market. Simply provide a directory with CSV price data and the program will analyse all the markets according to the **crossover criteria**.
> A turning point is defined as a period of transition between trends. This program uses moving average crossovers to determine that. This is the same methodology used in the research paper ["Breaking Bad Trends"](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3594888), by Christian L. Goulding, Campbell R. Harvey, and Michele G. Mazzoleni. 
> Whenever a short-term moving average and a long-term moving average cross eachother, the program considers it a turning point. Both of the moving average lengths can be configured inside the `config.py` file.
Both this project and README are still a WIP. Some future plans include
- Exporting results to spreadsheets
- Adding Yahoo Finance API support for stock analysis