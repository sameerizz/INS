from random import randint

if __name__ == '__main__':
    # Publicly shared prime number q
    q = 23
    # Publicly shared base (primitive root) alpha
    alpha = 9
    
    # Displaying the values of q and alpha
    print('The Value of q is: %d' % q)
    print('The Value of alpha is: %d' % alpha)
    
    # Alice's private key (chosen secretly)
    # Generate Alice's private key as a random integer between 1 and q-1
    XA = randint(1, q-1)
    print('Secret Number for Alice is: %d' % XA)
    
    # Calculate Alice's public key using alpha^XA % q
    YA = pow(alpha, XA, q)  # YA = alpha^XA mod q
    
    # Bob's private key (chosen secretly)
    # Generate Bob's private key as a random integer between 1 and q-1
    XB = randint(1, q-1)
    print('Secret Number for Bob is: %d' % XB)
    
    # Calculate Bob's public key using alpha^XB % q
    YB = pow(alpha, XB, q)  # YB = alpha^XB mod q
    
    # Alice calculates the shared secret key using Bob's public key and her private key
    k1 = pow(YB, XA, q)  # k1 = YB^XA mod q
    
    # Bob calculates the shared secret key using Alice's public key and his private key
    k2 = pow(YA, XB, q)  # k2 = YA^XB mod q
    
    # Display the calculated secret keys
    print('Secret Key for Alice is: %d' % k1)
    print('Secret Key for Bob is: %d' % k2)
