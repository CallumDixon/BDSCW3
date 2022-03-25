import os

my_dir = "./datasets/energy"# enter the dir name
for fname in os.listdir(my_dir):
    if len(fname) == 16:
        os.remove(os.path.join(my_dir, fname))
