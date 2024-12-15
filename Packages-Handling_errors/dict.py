# Task 1 :
my_dict={
    'name':'sura',
    'age':'23',
    'city':'tulkarm'
}
key=input('Enter a key (name,age,city):')

try:
    print(my_dict[key])
except KeyError:
    print("key not found in the my_dict")