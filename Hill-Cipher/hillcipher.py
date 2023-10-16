import numpy

def create_matrix_from(key):
    m=[[0] * 3 for i in range(3)]
    for i in range(3):
        for j in range(3):
            m[i][j] = ord(key[3*i+j]) % 65
    return m

# C = P*K mod 26
def encrypt(P, K):
    C=[0,0,0]
    C[0] = (K[0][0]*P[0] + K[1][0]*P[1] + K[2][0]*P[2]) % 26
    C[1] = (K[0][1]*P[0] + K[1][1]*P[1] + K[2][1]*P[2]) % 26
    C[2] = (K[0][2]*P[0] + K[1][2]*P[1] + K[2][2]*P[2]) % 26
    return C

def Hill(message, K):
    cipher_text = []
    #Transform the message 3 characters at a time
    for i in range(0,len(message), 3):
        P=[0, 0, 0]
        #Assign the corresponfing integer value to each letter
        for j in range(3):
            P[j] = ord(message[i+j]) % 65
        #Encript three letters
        C = encrypt(P,K)
        #Add the encripted 3 letters to the final cipher text
        for j in range(3):
            cipher_text.append(chr(C[j] + 65))
        #Repeat until all sets of three letters are processed.
        
    #return a string
    return "".join(cipher_text)

def MatrixInverse(K):
    det = int(numpy.linalg.det(K))
    det_multiplicative_inverse = pow(det, -1, 26)
    K_inv = [[0] * 3 for i in range(3)]
    for i in range(3):
        for j in range(3):
            Dji = K
            Dji = numpy.delete(Dji, (j), axis=0)
            Dji = numpy.delete(Dji, (i), axis=1)
            det = Dji[0][0]*Dji[1][1] - Dji[0][1]*Dji[1][0]
            K_inv[i][j] = (det_multiplicative_inverse * pow(-1,i+j) * det) % 26
    return K_inv

if __name__ == "__main__":
    
    message = input ("Enter the Plaintext : ")
    key = input ("Enter the key : ")
    #Create the matrix K that will be used as the key
    K = create_matrix_from(key)
    print(K)
    # C = P * K mod 26
    cipher_text = Hill(message, K)
    print ('Cipher text: ', cipher_text)
    
    
    # Decrypt
    # P = C * K^-1 mod 26
    K_inv = MatrixInverse(K)            
    plain_text = Hill(cipher_text, K_inv)
    print ('Plain text: ', plain_text)

        # K x K^-1 equals the identity matrix
    M = (numpy.dot(K,K_inv))
    for i in range(3):
        for j in range(3):
            M[i][j] = M[i][j] % 26
    print(M)
