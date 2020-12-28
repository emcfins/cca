# cca

Let's make America [Colossal Cave Adventure] (https://en.wikipedia.org/wiki/Colossal_Cave_Adventure) again!

Based upon Fortran code found on [Jerz's Literacy Weblog] (http://jerz.setonhill.edu/intfic/colossal-cave-adventure-source-code/)

Quite a bit more info [here] (http://www.digitalhumanities.org/dhq/vol/001/2/000009/000009.html#section02), including an early translation to C


### Using the Dockerfile

When in the same directory as the README.md, run:
```
docker build -t cca .

docker run -it -v <location of project>:/data cca
```

### To Compile - as of Nov19, 2020

```
cd nelson-port
g77 -o adventure.out advent.for 2> compile.out
```
### To Run
```
./adventure.out
```

### Things I've learned so far by Erin

* vim is awesome becuase it does syntax highlighting for Fortran. SUPER helpful

* when talking about this project, I say 4chan instead of Fortran 9 times out of 10

* all commands have to start at column 7

* to convert the tabs to 6 spaces

```
:set tabstop=4 shiftwidth=4 expandtab
:%!expand -t6
```
