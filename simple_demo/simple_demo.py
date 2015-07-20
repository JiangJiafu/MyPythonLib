#!/usr/bin/python
import parastor.node

def empty_func():
    """Do nothing"""
    pass

def swap_demo():
    
    print '\nswap_demo'
    # Swap two numbers.
    a = 1
    b = 2
    a, b = b, a
    print a, ',', b

def string_demo():
    """Show how to print a simple string."""

    print 'Hello World1'
    print "Hello World2"
    print """Hello
World3"""
    print "Hello world4",
    print " Hello world5"

def string_demo2():
    """String demo2"""

    str1 = 'sugon'
    print str1 * 2
    print 'the length of str1 is %d' % len(str1)
    if str1.startswith('su'):
        print '%s start with su' % str1
    if str1.find('go'):
        print '%s contains go' % str1

def list_demo():
    """How to use list."""

    list_a = ['s', 'u', 'g', 'o', 'n']
    print list_a
    print list_a[0: 2]
    print list_a[0:]
    print list_a[-2:]
    if 'g' in list_a:
        print 'g is in list_a'
    list_b = range(0, 10)
    print list_b
    list_c = [x for x in list_b if x % 2 == 0]
    print list_c
    list_d = list_c * 2
    print list_d
    
def list_demo2():
    """How to add and delete an element."""

    print '\nlist_demo2:'
    list_a = ['s', 'u', 'g']
    list_a.append('o')
    list_a.append('n')
    list_a.pop()
    print list_a
    list_a.sort()
    print list_a

def dict_demo1():
    """How to define a dict."""
    
    print '\ndict demo1'
    a = dict(one=1, two=2, three=3)
    b = {'one': 1, 'two': 2, 'three': 3}
    c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
    d = dict([('two', 2), ('one', 1), ('three', 3)])
    e = dict({'three': 3, 'one': 1, 'two': 2})
    print a == b == c == d == e
    print b['one']
    b['one'] = 'one'
    print b['one']
    for (k, v) in a.items():
        print '%s:%s' % (k, v)

def dict_demo2():
    """Define a complicated dict."""

    print '\n dict demo2'
    
    dict_c = {
        'list_a': ['su', 'gon'],
        'str': 'sugon',
        'dict': {
            'name': 'jiangjiafu',
            'title': 'manong'
        }
    }

    print dict_c['str']
    print dict_c['dict']['name']

def fun2(a, b, c='Hello', d=None, *args, **kwargs):
    """How to define a function with many parameters."""

    print '\nfun2'
    print 'a is ', a
    print 'b is ', b
    print 'c is ', c
    print 'd is ', d
    print 'args is ', args
    print 'kwargs is', kwargs

def class_demo():
    """How to define a class"""

    print '\nclass demo'
    mgrnode = parastor.node.MGRNode('MGR', 1)
    print mgrnode.get_desc()

   

def main():
    empty_func()
    swap_demo()
    string_demo()
    print string_demo.__doc__
    string_demo2()
    list_demo()
    list_demo2()
    dict_demo1()
    dict_demo2()
    fun2(1, 2, 'World', True, 3, 4, 5, 6, name='jiangjiafu', company='sugon')
    class_demo()

if __name__ == '__main__':
    main()
