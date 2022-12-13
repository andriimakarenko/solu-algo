# solu-algo
Guys, please hear me out.
It was my first tech interview in over a year and first live coding since like 2018.
I know I absolutely bombed it but it's because I've went full panic mode.
When I calmed down, I came up with this. Please, PLEASE check it out.
It's in the file named `SOLUtion.py`. Is that why you're called Solu btw?

Also, once I was done with the first version, I decided it's not enough and went for a second one, I decided to exploit the fact that cutting away the corner element of the array (and string being an array of letters) should be resourse-efficient in most languages.
Unfortunately, I forgot that strings are immutable in Python and they get re-created in each iteration.
Still, it brought an improvement in speed, only not as big one as I hoped it would bring.

P.S.: Also it took me some time to figure out the seemingly simple task of match-casing to a variable, cause somehow I have only match-cased in Python to constants, such hard-coded strings or numbers. I googled it and played with a simplified version in the file `check.py` that I deleted with the last commit. Feel free to go to the commit history and laugh at how silly I am in it :)