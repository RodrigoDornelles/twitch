import subprocess
import os
import time

cmd_arr = (
 'espeak', '-vbrazil-mbrola-4', 'amigo voce é um amigo, obrigado amigo.',
 '-p', '300', '-s', '100'
)

subprocess.Popen(cmd_arr)

print('foo')
time.sleep(2)
print('bar')
