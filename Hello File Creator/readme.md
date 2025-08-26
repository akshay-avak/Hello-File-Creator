# Hello File Creator

# Roadmap

- [X] Create multiple files (bulk files)  
- [X] Create multiple files where user provides file 

## What i learned when researching this

### open()
It is a built-in python function that opens a file and returns a file object.

syntax-> ```open('file','mode') ```
There more than 2 parameters these two are commonly used.

About Parameters  
**file :** a path to the file or name of file can be given to open. Eg: ```file.txt```

**mode :** This parameter defines how the file is opened.
  

  * 'r' --> **Read** (Is the default mode).Throws an error if file does not exist.

  * 'w' --> **Write** .Creates a new file or overwrites if it exists.

  * 'a' --> **Append**. Creates a new file if not present, Writes content to the file at the end.

  * 'x' --> **Exclusive creation**.Throws error if file exists.



