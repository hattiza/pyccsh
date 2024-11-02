import subprocess

def ccsh():
  command = input("ccsh> ").strip()


  result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  stdout, stderr = result.stdout, result.stderr
  out = stdout.decode('utf-8')
  err = stderr.decode('utf-8')


  if stderr:
    lines = err.split("\n")
    for line in lines:
      print(line)
  else:
    lines = out.split("\n")
    for line in lines:
      print(line)


  print(stdout, stderr)




if __name__ == "__main__":
  ccsh()