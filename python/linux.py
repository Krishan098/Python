# $ pwd: returns working directory
# $ ls : list directory contents#
#        :. -l :a total sum for all the file sizes is output on a line before the long listing.
#        :. -h :used with the option -l, this changes the file sizes into something more readable
#        :. -a: short for 'all', include 'hidden' directory entries whose names begin with a dot.
# $ cp : copy a file
# $ mv : move a file
# $ mkdir : 
#         :. -p : any intermediate directories that don't exist yet will also be created
# $ rm: removes directory. follow -p argument
#         :. -r: recursive, won't remove special files
#         :. -f: forces to remove everything
#         :. -i: forces you to confirm the delete option
# $ rmdir
# $ cat: prints everything on screen
# $ less: allows to scroll through the file
# $ tail: prints the last 10 lines of the file
# $ head: shows the first 10 lines of the file
# both head and tail take -n for the number of lines to be displayed
# ctrl+r : allows us to remember the command


''' BASH SCRIPTS:
            with these we can run sequence of commands.
            command line scripts start with the shebang - a sequence of the 2 characters #!.
            #!interpreter[optional arguments]
            #!/bin/bash
            #!/usr/bin/env bash
    
    bash has variables.
    myvar="hello world"
    echo $myvar
    $0 : name of the current script
    $1...$9: First 9 arguments of the script
    $#: Num of arguments passed to the script
    $@: all the arguments supplied to the script
    $USER: username of the user running the script
    $HOSTNAME: hostname of the machine
    $SECONDS: num of seconds since the script has started
    $RANDOM: returns a diff number everytime
    $LINENO : returns the current line number
    
BASH SCRIPT ARGUMENTS:
            call it arguments.sh
            #!/bin/bash
            echo "Hello $1, from $0"
Prevent using unset variables by starting our scripts:
    set -u


BASH FOR LOOP:
        for variable in a list
        do
            command1
            commandN
        done
STARTING A BASH SCRIPT:
        bash loop.sh
        $ chmod +x loop.sh
With test -z we can check if a variable's length is zero.

$man help

$find: lists all directories and files
$find .-type f 
find .-type d

'''
'''
UNIX PIPES:
        A pipe bridges 2 processes together. written with | character, connects the output of one command to the input of the second. It's one of the fundamental building blocks of a Unix shell.
        wc counts all the lines, words and bytes it is fed.
        wc -l counts the num of lines
'''

'''
jq command-line tool:
        echo'{"Price":10.0,"Name":"Cable"}'|jq
'''

'''
history n
!! repeat the last command
!n repeat command number n from history
!cd: re run the last command you typed starting with
!* substitute the arguments from the previous commands
'''

'''
BASH MULTIPROCESSING:
            Xargs:
                    xargs[options][command[initial-arguments]]
                    it can run processes in parallel with the -p option.
                    
'''