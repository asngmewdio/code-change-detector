# Code change detector

## Running script locally
e.g. command to compare two files
```
python compare.py base.cpp bad.cpp
python compare.py base.cpp single.cpp
```


## Running script in docker
To build the Docker image, you can run the following command in the same directory as the Dockerfile:
```
docker build -t comparer .
```
To run a container from the Docker image, you can run the following command:

- If file was copied while creating image
```
docker run --rm comparer python compare.py base.cpp single.cpp
```
- If you want to use custom files from host system
```
docker run --rm -it -v path/to/file:/app/ comparer python compare.py base.cpp single.cpp
```
Example `path/to/file` is  `C:/Users/XXXX/repos/code-change-detector`

A comment consists of: \
●	Comment declaration \
// \
●	Type of comment character \
o	‘ ’ (nothing) - one-line comment, indicates that the comment is relevant only for the single line below it \
o	‘<’ - start comment, indicates the start of a modification spanning multiple lines \
o	‘>’ - end comment, indicates the end of a modification spanning multiple lines \
o	‘-’ - removal comment, indicates that a portion of the file was removed without any new line to replace it \
●	Comment identificatory #WJ \
●	Date in YYYY-MM-DD format \
●	Optional comment
