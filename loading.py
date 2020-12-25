# import time,sys
# while True:
# 	blah="\|/-\|/-"
# 	for l in blah:
# 		sys.stdout.write(l)
# 		sys.stdout.flush()
# 		sys.stdout.write('\b')
# 		time.sleep(0.2)


from halo import Halo

spinner = Halo(text='Loading', spinner='dots2')
spinner.start()

# Run time consuming work here
# You can also change properties for spinner as and when you want

