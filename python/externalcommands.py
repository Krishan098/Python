#A program that is executed on a computer is also called a process
'''
    A process is the instance of a computer program that is being executed by one or more threads.
    :. A process can have multiple threads-multithreading.
    :. Multiple processes can run at once.
    :. processes can be different programs, but they can also be multiple instances of the same program.
    :.Sub-processes/child process: if we want to run an external command, it means you need to create a new process from your Python process.
    :.fork:
            multiprocessing:the process forks itself, meaning a new copy of the process is created and started. useful to parallelize our code and use multiple CPUs on the machine.
            :.can also be used to start another process. The process forks itself first and then replaces itself with another process.
    :.subprocess module
    :. The wrapper function run() from the subprocess package helps to run external commands.
    
'''

import subprocess
#subprocess.run(['ls','-al'])
result=subprocess.run(['python3','--version'])
result
#returncode=0 means successfully completed, other than that means that there is some error.
result_1=subprocess.run(['python3','--version'],capture_output=True,encoding='UTF-8')
result_1
code="""
...for i in range(1,3):
...     print(f"Hello world {i}")
..."""
result_2=subprocess.run(['python3'],input=code,capture_output=True,encoding='UTF-8')
print(result_2.stdout)
result_3=subprocess.run(['ls-al | head -n 1'],shell=True)#prone to command injection attacks
result_3
'''COMMAND INJECTION:
        injects extra commands to gain control over a computer system.
'''
thedir=input()
result_4=subprocess.run([f'ls-al {thedir}'],shell=True)
