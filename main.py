
'''
    Scrieți un program care determină cea mai lungă subsecvență cu o anumită proprietate a unei liste de numere.
        7.	Toate numerele sunt neprime.
        17.	Media numerelor nu depășește o valoare citită.
        4.	Numerele sunt ordonate crescător.
'''


def verificare_neprim(nr):
    '''
    Verificam daca nr este numar neprim
    :param nr: int, un numar din lista
    :return: True daca nr este neprim si False in caz contrar
    '''
    if nr<2:
       return True
    elif nr==2:
        return False
    elif nr%2==0:
        return True
    else:
        for i in range(3,nr//2+1,2):
            if nr%i==0:
                return True
        return False
def test_verificare_neprim():
    assert verificare_neprim(45) == True
    assert verificare_neprim(13) == False
test_verificare_neprim()


def neprime(lst):
    '''
    Verificam daca toate numerele din lista sunt neprime
    :param lst: int, lista
    :return: True daca lst are toate elementele neprime si False in caz contrar
    '''
    for element in lst:
        if verificare_neprim(element)== False:
            return False
    return True
def test_neprime():
    assert neprime([12,63,42,55, 81,1]) == True
    assert neprime([12,63,42,55, 81,2]) == False
test_neprime()


def get_longest_all_not_prime(numere):
    '''
    Determina cea mai lunga secventa de numere neprime
    Daca sunt mai multe secvente de aceeasi lungime se va afisa prima gasita
    :param numere: int, lista cu numerele introduse
    :return: secventa maxima care indeplineste conditia
    '''
    secventa=[]
    for i in range(len(numere)):
        for j in range(i, len(numere)):
            considered = numere[i:j + 1]
            if neprime(considered):
                if len(secventa) < len(considered):
                    secventa = considered
    return secventa
def test_get_longest_all_not_prime():
    assert get_longest_all_not_prime([2,13,17,22, 81,5,3,6]) == [22, 81]
    assert get_longest_all_not_prime([2,13,17,22, 81,5,3,6,66,21,24,58,11]) == [6,66,21,24,58]
test_get_longest_all_not_prime()


def medie(lst):
    '''
    Se calculeaza media elementelor din lista
    :param lst: int, lista
    :return:  media numerelor din lst
    '''
    sum=0
    for element in lst:
        sum+=element
    med=sum/len(lst)
    return med
def test_medie():
    assert medie([12,2,4,6]) == 6
    assert medie([12,78, 32,1,4]) == 25.4
test_medie()


def get_longest_average_below(numere, val):
    '''
    Determina cea mai lunga secventa de numere din lista data a caror medie este mai mica sau egala cu o valoare data
    Daca sunt mai multe secvente de aceeasi lungime se va afisa prima gasita
    :param numere: int, lista de numere
    :param val: int, valoare cu care comparam mediile
    :return: secventa maxima care indeplineste conditia
    '''

    secventa = []
    for i in range(len(numere)):
        for j in range(i, len(numere)):
            considered = numere[i:j + 1]
            if medie(considered)<=val:
                if len(secventa)<len(considered):
                    secventa = considered
    return secventa
def test_get_longest_average_below():
    assert get_longest_average_below([12,12,5,3,4],13) == [12,12,5,3,4]
    assert get_longest_average_below([12,103,12,3,4],13) == [12,3,4]
test_get_longest_average_below()


def crescator(lst):
    '''
    Se verifica daca toate numerele din lista data sunt in ordine crescatoare
    :param lst: int, lista de numere
    :return: True daca toate numerele din lista sunt crescatoare si False in caz contrar
    '''
    a=lst[0]
    for element in lst[1:]:
        if a>element:
           return False
        a=element
    return True
def test_crescator():
    assert crescator([1,2,3,4,4,5]) == True
    assert crescator ([1,3,9,4,5]) == False
test_crescator()

def get_longest_equal_int_real(numere):
    '''
    Determina cea mai lunga secventa de numere in ordine crescatoare din lista
    Daca sunt mai multe secvente de aceeasi lungime se va afisa prima gasita
    :param numere: int, lista de numere
    :return: secventa maxima care indeplineste conditia
    '''
    secventa = []
    for i in range(len(numere)):
        for j in range(i, len(numere)):
            considered = numere[i:j + 1]
            if crescator(considered):
                if len(secventa) < len(considered):
                    secventa = considered
    return secventa
def test_get_longest_equal_int_real():
    assert get_longest_equal_int_real([1,3,9,4,5]) == [1,3,9]
    assert get_longest_equal_int_real([1,2,3,4,4,5]) == [1,2,3,4,4,5]
    assert get_longest_equal_int_real([5,4,3,2,1]) == [5]
test_get_longest_equal_int_real()


def read_list():
    # citim numerele asa: 3,56,7,1,3, 43, 5 , 54
    given = input('Dati numerele separate prin virgula: ')
    str_list = given.split(',')
    int_list = []
    for str_num in str_list:
        int_list.append(int(str_num))
    return int_list



def print_meniu():
    print("1. Citire lista")
    print("2. Determinare secventa maxima de numere neprime")
    print("3. Determinare secventa maxima de numere a caror medie nu depasesc o valoare data")
    print("4. Determinare secventa maxima de numere in ordine crescatoare")
    print("x. Iesire")

def main():
    numere=[]
    while True:
        print_meniu()
        option = input('Alegeti o optiune: ')
        if option == '1':
            numere = read_list()
        elif option == '2':
            result = get_longest_all_not_prime(numere)
            print('Cea mai lunga secventa cu toate numerele neprime este: ')
            print(result)
        elif option == '3':
            val=int(input("Introduceti valoarea: "))
            result = get_longest_average_below(numere,val)
            print('Cea mai lunga secventa de numerele a caror medie nu depaseste valoarea data  este: ')
            print(result)
        elif option == '4':
            result = get_longest_equal_int_real(numere)
            print('Cea mai lunga secventa de numerele in ordine crescatoare  este: ')
            print(result)
        elif option == 'x':
            break
        else:
            print('Optiune invalida, reincearca!')

if __name__ == '__main__':
  main()