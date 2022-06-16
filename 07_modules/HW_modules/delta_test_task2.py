from task_02_delta_module import delta as d

def calculation(val1,val2,val3):
    return d(val1,val2,val3)

def main():
    val1 = int(input('Enter value for a'))
    val2 = int(input('Enter value for b'))
    val3 = int(input('Enter value for c'))
    calculation(val1,val2,val3)
main()

