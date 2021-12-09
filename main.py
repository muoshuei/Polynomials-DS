from Polynomial import *
   
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
