import subprocess

proc = subprocess.Popen(["cat", "/etc/services"], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
print "program output:", out