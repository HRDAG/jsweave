# jsweave

Code to weave data literals into LaTeX, with defaults, so that the LaTeX code can be edited interactively without `knitr` or `Sweave`.

# Usage Overview 

This tool was built to help mitigate going back and forth to udpate your values. Instead you can use jsweave's 
tag to encase each value and this will allow you to keep your values calculated and up to date. This is especially helpful
because it informs you where the value came from, and if the data changes you can update it using jsweave instead of searching 
through your latex file to adjust each value change. 


```
jsweave --help 
```

# Installation  

To install this package we recommend [cloning the repository](https://help.github.com/articles/cloning-a-repository/). 

# Troubleshooting & Debugging

# Name collisions

[`js-weave`](https://www.npmjs.com/package/js-weave) is a javascript client for the Weave RPC

[`JSweave`](http://www.seinan-gu.ac.jp/~shito/jsweave/archives/manual.pdf) is a java program to weave R output into LaTeX.

# License

Please have a look at the [LICENSE.md] (https://github.com/HRDAG/jsweave/blob/master/LICENSE for more details.)


<!-- done. -->
