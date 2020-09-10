## Project

The project is a script tool to compress files into ```.gz``` gzip format.

### Usage
```
python3 main.py <path-to-directory>
```
For example, if you wanted to compress the files in the ```/var/log``` directory, the command would be:
```
python3 main.py /var/log
```
Alternatively, you may set up the script as a cron job. The included ```run.sh``` script does this, with default values being repeating monthly and the directory being ```/var/log```, you can change those values by editing the ```run.sh``` file yourself.
Then, run the following
```
chmod +x
./run.sh
```
to set the shell file as executable and run the script.



### Tests
The project includes simple tests of its functionality, which you can run using:
```
python3 test.py
```
The results of the test depend on the existing directory structure, changing it may result in tests failing.
