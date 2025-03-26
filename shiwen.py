a_0 = 3
a_1 = 2

result_list = []
result_list.append(a_0)
result_list.append(a_1)

def sequence_checker(in_list):
    l = len(in_list)
    if(in_list[l-1] == (3*in_list[l-2] - 1*in_list[l-3])/2):
        return True

def normal_sequence(in_list):
    l = len(in_list)
    r = (3*in_list[l-1] - in_list[l-2]) / 2
    return r

def c_n(r,d,n):
    x = 2**(n-d) * (r) + 2**(n-d) - 1
    return x

def claimed_function(a_1, a_0,n):
    return (c_n(3,2,n)*a_1 - c_n(3,3,n)*a_0) / (2**(n-1))

n = 2
valid_results = True
while ( n < 1000 and valid_results):
    result_list.append(normal_sequence(result_list))
    r = claimed_function(a_1,a_0,n)
    if(sequence_checker(result_list) == False or r != result_list[len(result_list)-1]):
        valid_results = False
        print(n)
    n = n + 1
    
#fails at n = 54, when computational precision fails

