stack=[]
acc=0
def push(x):
  stack.append(x)
def asciipop():
  print(chr(stack.pop()))
def intpop():
  print(stack.pop())
def rev():
  stack.reverse()
def dup():
  stack.append(stack[-1])
print("Insert file name and full directory:")
dir=input()
#file grabber
codefile=open(dir)
#text extractor
code=codefile.read()
codefile.close()
code=code.split()
x=0

while(x<len(code)):
  if(code[x]==')'):
    break
  elif(code[x]=='?'):
    push(int(input()))
  elif(code[x]=='.'):
    intpop()
  elif(code[x]==','):
    asciipop()
  elif(code[x]=='+'):
    push(stack.pop()+stack.pop())
    
