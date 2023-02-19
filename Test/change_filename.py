import subprocess
for k in range(13,101 + 1):
    cmd = ["copy","C:\\Users\\kpp01\\Documents\\alc_on_keyboard\\words\\p1\\word_raw" + str(k) + ".txt","C:\\Users\\kpp01\\Documents\\alc_on_keyboard\\words\\word_raw" + str(k - 1) + ".txt"]
    print(cmd)
    subprocess.call(cmd,shell = True)