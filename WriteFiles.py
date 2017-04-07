from sys import argv
import random

script, filename = argv

phrases = ['test', 'hi', 'bye', 'year', 'this', 'that', 'brick', 'brack', 'mr. jones', 'badgers']

print ("We're going to erase %r." % filename)
print ("If you don't want, hit CTRL-C (^C).")
print ("If you do want that, hit RETURN.")

raw_input("?")

print ("Opening the file.....")
target = open(filename, 'w')
target.truncate()

#target.write("testing, 36, hello")

for x in xrange(1,10000000):
    random.shuffle(phrases)
    target.write("%s,%d,%d,%s,%d" % (phrases[x%10],x%10,random.randint(50,100), random.choice('rqypowropisvnloipuwnihaadf'), random.randint(600, 5000)))
    target.write("\n")

target.close()


      
