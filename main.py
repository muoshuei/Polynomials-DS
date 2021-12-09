from LinkedList import *

class Term(object):
    def __init__(self, coefficient: float, power: int):
        self.coefficient = coefficient
        self.power = power
class Polynomial(object):
    def __init__(self, function_head: str = 'f', indeterminate: str = 'x', poly: str = '0'):
        self.list = SingleLinkedList()
        self.str_form = f'{function_head}({indeterminate}) = {poly}'

def print_polynomial(list: SingleLinkedList, name:str):
    print(f'{name}(x) = ', end = '')
    if list.head == None:
        print('0')
        return
    curr = list.head
    while not curr == None:
        sign = '+'
        if curr == list.head:
            sign = ''
        if curr.elem.coefficient < 0:
            sign = '-'
        abs_coefficient = abs(curr.elem.coefficient)
        if(abs_coefficient == 1 and not curr.elem.power == 0):
            abs_coefficient = ''
        if curr.elem.power == 1:
            print(f'{sign} {abs_coefficient}x ', end='')
        elif curr.elem.power == 0:
            print(f'{sign} {abs_coefficient} ', end='')
        else:
            print(f'{sign} {abs_coefficient}x^{curr.elem.power} ', end='')
        curr = curr.next
    print()
    return
def negative(list:SingleLinkedList):
    curr = list.head
    new_list = SingleLinkedList()
    while True:
        if curr == None:
            break
        new_list.add_item(ListNode(Term(-1 * curr.elem.coefficient, curr.elem.power)))
        curr = curr.next
    return new_list

def sum(list_f:SingleLinkedList, list_g:SingleLinkedList):
    list_h = SingleLinkedList()
    curr_f = list_f.head # f(x) pointer
    curr_g = list_g.head # g(x) pointer
    while True:
        # Both reach end
        if curr_f == None and curr_g == None: 
            break
        # check which have gone to the end faster
        if curr_f == None:  
            list_h.add_item(ListNode(Term(curr_g.elem.coefficient,curr_g.elem.power)))
            curr_g = curr_g.next
            continue
        elif curr_g == None:
            list_h.add_item(ListNode(Term(curr_f.elem.coefficient,curr_f.elem.power)))
            curr_f = curr_f.next
            continue
        
        power_f = curr_f.elem.power
        power_g = curr_g.elem.power
        # same power add each other
        if power_f == power_g:
            coefficient = curr_f.elem.coefficient + curr_g.elem.coefficient
            # remove 0 coefficient terms
            if not coefficient == 0:
                list_h.add_item(ListNode(Term(coefficient, power_f))) 
            curr_f = curr_f.next
            curr_g = curr_g.next
        # get term with greater power
        elif power_f > power_g:
            list_h.add_item(ListNode(Term(curr_f.elem.coefficient,curr_f.elem.power)))
            curr_f = curr_f.next
        elif power_g > power_f:
            list_h.add_item(ListNode(Term(curr_g.elem.coefficient,curr_g.elem.power)))
            curr_g = curr_g.next
    return list_h
            
def diff(list_f:SingleLinkedList, list_g:SingleLinkedList):
    list_g_negative = negative(list_g)
    return sum(list_f, list_g_negative)

def product(list_f:SingleLinkedList, list_g:SingleLinkedList):
    new_list = SingleLinkedList()
    tmp_list = SingleLinkedList()
    curr_f = list_f.head
    curr_g = list_g.head
    while True:
        if curr_f == None:
            break
        curr_g = list_g.head
        tmp_list = SingleLinkedList()
        while True:
            if curr_g == None:
                break
            f_coeff = curr_f.elem.coefficient
            g_coeff = curr_g.elem.coefficient
            f_pow = curr_f.elem.power
            g_pow = curr_g.elem.power
            tmp_list.add_item(ListNode(Term(f_coeff * g_coeff, f_pow + g_pow)))
            curr_g = curr_g.next
        new_list = sum(new_list, tmp_list)
        curr_f = curr_f.next
    return new_list

def quotient_and_remainder(list_f:SingleLinkedList, list_g:SingleLinkedList):
    quo_list = SingleLinkedList()
    rem_list = SingleLinkedList()
    if list_f.head == None:
        return (quo_list, rem_list)
    tmp_list = list_f
    while True:
        curr_tmp = tmp_list.head
        curr_g = list_g.head
        if tmp_list.head.elem.power < list_g.head.elem.power:
            break
        coeff = curr_tmp.elem.coefficient / curr_g.elem.coefficient
        pow = curr_tmp.elem.power - curr_g.elem.power
        term = Term(coeff,pow)
        quo_list.add_item(ListNode(term))
        diff_list = SingleLinkedList()
        while True:
            if curr_g == None:
                break
            coeff_d = curr_g.elem.coefficient * term.coefficient
            pow_d = curr_g.elem.power + term.power
            diff_list.add_item(ListNode(Term(coeff_d, pow_d)))
            curr_g = curr_g.next
        tmp_list = diff(tmp_list, diff_list)
    rem_list = tmp_list
    return (quo_list, rem_list)
def quotient(list_f:SingleLinkedList, list_g:SingleLinkedList):
    return quotient_and_remainder(list_f,list_g)[0]
def remainder(list_f:SingleLinkedList, list_g:SingleLinkedList):
    return quotient_and_remainder(list_f,list_g)[1]

        
if __name__ == '__main__':  

    #f(x) = 3 x^10 + 5 x^6 + 4 x^3 + 2 x + 9
    list_f = SingleLinkedList()
    list_f.add_item(ListNode(Term(3,10)))
    list_f.add_item(ListNode(Term(5,6)))
    list_f.add_item(ListNode(Term(4,3)))
    list_f.add_item(ListNode(Term(2,1)))
    list_f.add_item(ListNode(Term(9,0)))

    #g(x) = 10 x^6 + 4 x^5 + x^3 + 5 x + 10
    list_g = SingleLinkedList()
    list_g.add_item(ListNode(Term(10,6)))
    list_g.add_item(ListNode(Term(4,5)))
    list_g.add_item(ListNode(Term(1,3)))
    list_g.add_item(ListNode(Term(5,1)))
    list_g.add_item(ListNode(Term(10,0)))


    print_polynomial(list_f, 'f')
    print_polynomial(list_g, 'g')

    list_s = sum(list_f, list_g)
    print("Sum of two polynomial is: ")
    print_polynomial(list_s, 's')

    list_d = diff(list_f,list_g)
    print("Difference of two polynomial is: ")
    print_polynomial(list_d, 'd')

    list_p = product(list_f,list_g)
    print("Product of two polynomial is: ")
    print_polynomial(list_p, 'p')

    list_q = quotient(list_f, list_g)
    print("Quotient of two polynomial is: ")
    print_polynomial(list_q, 'q')

    list_r = remainder(list_f, list_g)
    print("Remainder of two polynomial is: ")
    print_polynomial(list_r, 'r')
