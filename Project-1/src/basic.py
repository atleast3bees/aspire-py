"""
Author : Rori Wu

Date : 7/3/23

Description : Project-1 practice functions
"""


def add_two (x):
    """
    Start easy :)
    This function should take a number and add 2 to it

    Implement this function then try running the code to check your work
    """
    return x + 2 
    pass 

def is_even(x):
    """
    This function should return true if the number is even, else False
    """
    return x % 2  == 0
    pass

def is_odd(x):
    """
    This function should return true if the number is odd, else False
    """
    return not(is_even(x))
    pass

def for_fun(x):
    """
    This function should take any arbitrary number x,
    and return a list of all even numbers from -x to x
    """
    lst = []
    if x >= 0: 
        for i in range(-x,x+1):
            if is_even(i):
                lst.append(i)
    else:
        for i in range(x,-x+1):
            if is_even(i):
                lst.append(i)
    return lst
    pass

def is_prime(x):
    """
    This function should return True if the number is prime, else False

    DO NOT GOOGLE! Remember prime numbers are only divisible by themselves and 1
    """
    if x < 0:
        x = -x
    divisible_count = 0
    for i in range(1,x+1):
        if x % i == 0:
            divisible_count += 1
            if divisible_count > 2:
                return False
    return True
    pass

def is_prime_robust(x):
    """
    This function is the same as the above, except make it robust to user input

    return False for bad input
    """
    if isinstance(x, int) and not(isinstance(x, bool)):
        return True
    return False
    pass

def n_fibonacci(n):
    """
    This function should return a list of the first n fibonacci numbers

    The fibonacci sequence is defined by the following:
    F_n = F_{n-1} + F_{n-2}
    such that F_0 = 0 and F_1 = 1

    DO NOT GOOGLE

    Make sure inputs are robust, return False for bad inputs
    """
    if isinstance(n, int) and not(isinstance(n, bool)):
        if n==1:
            return [0]
        elif n>1:
            lst = [0,1]
            for i in range(1,n-1):
                lst.append(lst[i-1]+lst[i]) 
            return lst
    return False
    pass

def make_tree():
    """
    This function should print the following tree using only for loops and prints


    +
   +++
  +++++
 +++++++
+++++++++

    You CANNOT just use a bunch of individual prints
    """
    width = 1
    for i in range(1,6):
        print(" "*(5-i) + "+"*width)
        width += 2
    pass

def make_tree_inverted():
    """
    This function should print the following tree using only for loops and prints

+++++++++
 +++++++
  +++++
   +++
    +

    You CANNOT just use a bunch of individual prints
    """
    width = 9
    for i in range(1,6):
        print(" "*(i-1) + "+"*width)
        width -= 2
    pass

def dictionary_basics(d, key, value):
    """
    This function takes a dictionary, key, and value.
    Return a 3-tuple containing the following:
    - A sorted list of all the values whose keys contain the word "red"
    - The value of the key passed in
    - The key of the value passed in
    """
    red_list = []
    for i in d.keys():
        if i.find("red")!=-1:
            red_list.append(d[i])
    red_list.sort()
    d_value = d[key]
    d_key = 0
    for i in d.keys():
        if str(d[i])==value:
            d_key = i
    tup = (red_list,d_value,d_key)
    return tup
    pass



# =================================================================================================
# DO NOT EDIT ANY CODE BELOW THIS LINE: Would be cheating...
# =================================================================================================
    """
    ===============================================
    STOP HERE! DO NOT EDIT ANY CODE BELOW THE T-REX
    ===============================================
                              _.-.
                             /  99\
                            (      `\
                            |\\ ,  ,|
                    __      | \\____/
              ,.--"`-.".   /   `---'
          _.-'          '-/      |
      _.-"   |   '-.             |_/_
,__.-'  _,.--\      \      ((    /-\
',_..--'      `\     \      \\_ /
                `-,   )      |\' 
                  |   |-.,,-" (  
                  |   |   `\   `',_
                  )    \    \,(\(\-'
              jgs \     `-,_
                   \_(\-(\`-`
                      "  "

    """
def check_input():
    while True:
        x = input("Be honest...[Yes/No]")
        if x.lower() == "yes": return True
        elif x.lower() == "no": return False
        else: print("Enter Yes or No")

import rsa
import time
if __name__=="__main__":
    fun = 33
    fun1 = [-32, -30, -28, -26, -24, -22, -20, -18, -16, -14, -12, -10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32]
    even = 1029428
    odd = 1029427
    negative = -12949124
    prime = 13
    prime2 = 7283
    fib = 20
    fib1 = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]
    d = {"hi": 114, "red_panda": 23, "bred": 22, "chicken": 1, "tread": 2, "red_sauce": 100}
    key = "hi"
    value = "1"
    d1 = ([22, 23, 100], 114, "chicken")

    print("Running tests...")
    assert add_two(even)==even+2, "❌❌❌ Test 1 Failed..."
    assert add_two(odd)==odd+2, "❌❌❌ Test 1 Failed..."
    time.sleep(0.25)
    print("🔥🔥🔥 Test 1 Passed!")
    assert is_even(even)==True, "❌❌❌ Test 2 Failed..."
    assert is_even(odd)==False, "❌❌❌ Test 2 Failed..."
    time.sleep(0.25)
    print("🔥🔥🔥 Test 2 Passed!")
    assert is_odd(even)==False, "❌❌❌ Test 3 Failed..."
    assert is_odd(odd)==True, "❌❌❌ Test 3 Failed..."
    time.sleep(0.25)
    print("🔥🔥🔥 Test 3 Passed!")
    assert for_fun(fun)==fun1, "❌❌❌ Test 4 Failed..."
    time.sleep(0.25)
    print("🔥🔥🔥 Test 4 Passed!")
    assert is_prime(prime)==True, "❌❌❌ Test 5 Failed..."
    assert is_prime(negative)==False, "❌❌❌ Test 5 Failed..."
    assert is_prime(prime2)==True, "❌❌❌ Test 5 Failed..."
    time.sleep(0.25)
    print("🔥🔥🔥 Test 5 Passed!")
    assert is_prime_robust(prime)==True, "❌❌❌ Test 6 Failed..."
    assert is_prime_robust(prime2)==True, "❌❌❌ Test 6 Failed..."
    assert is_prime_robust("hello")==False, "❌❌❌ Test 6 Failed..."
    assert is_prime_robust(True)==False, "❌❌❌ Test 6 Failed..."
    time.sleep(0.25)
    print("🔥🔥🔥 Test 6 Passed!")
    assert n_fibonacci(fib)==fib1, "❌❌❌ Test 7 Failed..."
    assert n_fibonacci("hello")==False, "❌❌❌ Test 7 Failed..."
    time.sleep(0.25)
    print("🔥🔥🔥 Test 7 Passed!")
    print("Does this:")
    make_tree()
    print("Look like this?:")
    print("""
    +
   +++
  +++++
 +++++++
+++++++++

    """)
    assert check_input(), "❌❌❌ Test 8 Failed..."
    time.sleep(0.25)
    print("🔥🔥🔥 Test 8 Passed!")
    print("Does this:")
    make_tree_inverted()
    print("Look like this?:")
    print("""
+++++++++
 +++++++
  +++++
   +++
    +
    """)
    assert check_input(), "❌❌❌ Test 9 Failed..."
    time.sleep(0.25)
    print("🔥🔥🔥 Test 9 Passed!")
    assert dictionary_basics(d, key, value)==d1, "❌❌❌ Test 10 Failed..."
    time.sleep(0.25)
    print("🔥🔥🔥 Test 10 Passed!")

    print("Congrats!!! You have unlocked the secret code")
    print("Loading Secret...")
    time.sleep(2)
    with open('secret_sauce/private.pem', mode='rb') as privatefile:
        privkeydata = privatefile.read()
    with open('secret_sauce/public.pem', mode='rb') as publicfile:
        pubkeydata = publicfile.read()
    privateKey = rsa.PrivateKey.load_pkcs1(privkeydata)
    publicKey = rsa.PublicKey.load_pkcs1_openssl_pem(pubkeydata)
    with open("secret_sauce/secret_message1.txt", "rb") as msg:
        secret = msg.read()
    decMessage = rsa.decrypt(secret, privateKey).decode()
    print("SECRET MESSAGE: ", decMessage)
