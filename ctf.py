import shlex
import subprocess
import pyautogui
import time

def NumberPress(x, check):
    s = str(x)

    for i in s:
        pyautogui.press(i)
        # time.sleep(0.001)
        # print(i, end='')
    if check != 0:
        time.sleep(0.005)
        pyautogui.press('enter')


    # print()
def run_command(command):
    check = 0
    x = -2
    x_old = -1
    timer = 0
    process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)
    while True:
        # print('111')
        if check == 0:
            timer = time.clock_gettime(time.CLOCK_REALTIME)
        output = process.stdout.readline()
        # print(output, '+++')
        # time.sleep(0.06)
        if output == '' and process.poll() is not None:
            break
        if output:
            # print(output.decode().split())
            lol = output.decode().split()
            if lol[2] == 'plus':
                x = int(lol[1]) + int(lol[3])
            elif lol[2] == 'minus':
                x = int(lol[1]) - int(lol[3])
            elif lol[2] == 'multiply':
                x = int(lol[1]) * int(lol[3])
            elif lol[2] == 'divide':
                x = 1
                int(lol[1]) / int(lol[3])

        if check == 0:
            time.sleep(2)
            NumberPress('57ef8df8f232a9ad4094f9136f48806d', check)
            pyautogui.press('enter')
        check += 1

        if (x == x_old):
            break;

        # print('x= ', x, "task#", check-1, 'time=', time.clock_gettime(time.CLOCK_REALTIME)-timer, 's')

        if check > 1:
            NumberPress(x, check)

        x_old = x



            # process.stdin.write('123\n'.encode())
            # print('111')
            # process.stdin.close()
            # process.stdin.write("123")



    rc = process.poll()
    print(output)
    # print()
    return rc

run_command('nc ege.q.2020.ugractf.ru 1337')