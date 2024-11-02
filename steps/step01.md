# Step 1 - Challenge: The Simplest Possible Shell



In this step your goal is to create the simplest possible command line shell. That’s a program that, starts up and waits for the user to type in a command. To make it easier to see which shell is running I’ve given my shell a unique prompt: ccsh>.

When the user enters a command we’ll need to trim any trailing whitespace or newline characters and then spawn a new process to run the entered command.

For example, here’s what happens when I run my ccsh:

```shell
% ccsh
ccsh> ls
LICENSE         README.md       dist            pyproject.toml  src
%
```

My shell outputs the prompt ccsh>. I have then run the command ls and it has output the results below the prompt. In this case you see the files from my Python implementation of ccsh.

Note that ccsh immediately terminates after running the command, returning me to the normal shell.