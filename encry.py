characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]

encry=input("Enter Text to Encrypt :")
e_n = [ord(letter) - 97 for letter in encry]
key=[[17,17,5],[21,18,21],[2,2,19]]

c=[]
for i in range(0,len(encry),3):
    d=[]
    d.append(e_n[i])
    d.append(e_n[i+1])
    d.append(e_n[i+2])
    c.append(d)

ci=[]
for i in range(0,len(c)):
    A3=[[0],[0],[0]]
    A3[0][0]=((c[i][0]*key[0][0])+(c[i][1]*key[1][0])+(c[i][2]*key[2][0]))
    A3[1][0]=((c[i][0]*key[0][1])+(c[i][1]*key[1][1])+(c[i][2]*key[2][1]))
    A3[2][0]=((c[i][0]*key[0][2])+(c[i][1]*key[1][2])+(c[i][2]*key[2][2]))
    ci.append(A3[0][0]%26)
    ci.append(A3[1][0]%26)
    ci.append(A3[2][0]%26)
cipher=""
for i in range(len(ci)):
    temp=ci[i]
    cipher+=characters[temp]
print("Encrypted Text :",cipher)
    


            
            
            


    
    
        



    
