# GP code to create data

This directory contains an example code that uses PiCat. This program can be downloaded from https://www.hakank.org/picat/


First, generate configuration files from contants.py which include dimensionless constants:

``` bash
mkdir config
picat generate_config_files.pi
```
These files will be created inside the directory "config" 

Then run GP on 2 servers with at least 36 cores as:

``` bash
mkdir inputs
mkdir out
./ARUN_GLOBAL1 # run on server 1 
./ARUN_GLOBAL2 # run on server 2 
````

To run on more servers, change the number of servers in ARUN and generate more scripts "GLOBAL".


The results of GP will be in the directory "out"


S. V. Chekanov and H.Kjellerstrand (June 26, 2025)

