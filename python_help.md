python --help
usage: C:\Users\Administrator\AppData\Local\Programs\Python\Python311\python.exe[option] ... [-c cmd / -m mod / file / -] [arg] ...

Option (and corresponding enviroment variables):
-b  : issue warning about str(bytes_instance), str(bytearray_instance) and comparing bytes/bytesarray with str. (-bb: issue error)

-B  : don`t write .pyc files on import; also PYTHONDONTWRITEBYCODE=x 

-c cmd  : program passed in as string (terminate option list)

-d  : turn on parser debugging output (for experts onlym only works on debug builds); also PYTHONDEBUG=x

-E  : ignore PYTHON* enviroment variables (such as PYTHONPATH)

-h  : print this help message and exit (also -? or --help)
-i  : inspect interactively after running script; force a prompt even if stin does not appear to be terminal; also PYTHONINSPECT=x

-I  : isolate Python from the user`s enviroment(implies -E and -s)-m mod  : run library module as a script  (terminates option list)
-0  : remove assert and __debug__-dependent statements; add .opt-2 before .pyc extension; also PYTHONOPTIMIZE=x

-00 : do -0 changes and also discard docstringsl add .opt-2 before .pyc extension

-P  : don`t prepared a potentially unsafe path to sys.path 

-q  : don`t print version and copyright messages interactive startup 
-s  : don`t add user site directory to sys.path; also PYTHONNOUSERSITE
-S  : don`t imply `import site` on initialization
-u  : force the stdout and stderr stream to be unbuffered;
-v  : verbose (trace import statement); also PYTHONVERBOSE=x
-V  : print the Python version number and exit (also --version) when given twice, print more information about the build

-W arg  : warning control; arg is action is action:message:category:module:lineno also PYTHONWARNINGS=arg

-x  : skip first line of source, allowing use of non-Unix form of #!cmd
-X opt  : set implementation-specific option 
--check-hash-based-pycs always|default|never:
control how Python invalidates hash-based .pyc files

--help-env  :   print help about Python enviroment variables and exit 
--help0xoption  : print help about implementation-specific -X options and exit

--help-all  : print complete help information and exit
Arguments: 
file  : program read from script file 
- : program read from stdin(defaultl interactive mode if a tty)

arg...  : arguments passed to program in sys.argv[1:]