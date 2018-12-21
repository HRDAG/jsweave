# jsweave

Code to weave data literals into LaTeX, with defaults, so that the LaTeX code can be edited interactively without `knitr` or `Sweave`.

# Usage Overview 

This tool was built to help mitigate updating your values. Instead you can use jsweave's 
command to encase each value in your document and this will allow you to keep your values calculated and up to date.
This is especially helpful because it informs you where the value came from, and if the data changes you can update it using jsweave instead of searching through your document to adjust each value change. 

The overall process is as follows:
```
original_file.tex --> processed_file.tex --> processed_file.pdf
```

To setup your latex file so that your values are calcuated, include the following line in the frontmatter:

```
\newcommand{\jsonsub}[2][XXXXX]{\textcolor{red}{#1}}
```

Then, in your document, encase literal values with the `jsonsub` command. That is, instead of:

```
The number of observations is 20
```

Use this: 

```
The number of observations is \jsonsub[20]{nobs}
```

Run jsweave 
```
jsweave sub -t processed_file.tex -j json_data.json
```


```
jsweave --help 
```
```
usage: jsweave [-h] -t TEX -j JSON [-l LOG] {sub,check,update}

positional arguments:
  {sub,check,update}

optional arguments:
  -h, --help            show this help message and exit
  -t TEX, --tex TEX     Input TeX file
  -j JSON, --json JSON  JSON file
  -l LOG, --log LOG     Log file name
```
# Installation  

To install this package we recommend [cloning the repository](https://help.github.com/articles/cloning-a-repository/). 

# Name collisions

[`js-weave`](https://www.npmjs.com/package/js-weave) is a javascript client for the Weave RPC

[`JSweave`](http://www.seinan-gu.ac.jp/~shito/jsweave/archives/manual.pdf) is a java program to weave R output into LaTeX.

# License

Please have a look at the [LICENSE.md](https://github.com/HRDAG/jsweave/blob/master/LICENSE) for more details.


<!-- done. -->
