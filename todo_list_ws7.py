def add_task(tasks):
    t=input('Task: ')
    tasks.append(t)

def view_tasks(tasks):
    for i,t in enumerate(tasks):
        print(i,t)

def delete_task(tasks):
    try:
        i=int(input('Index: '))
        tasks.pop(i)
    except:
        print('invalid')

def main():
    tasks=[]
    while True:
        print('1 add 2 view 3 delete 4 exit')
        c=input().strip()
        if c=='1': add_task(tasks)
        elif c=='2': view_tasks(tasks)
        elif c=='3': delete_task(tasks)
        elif c=='4': break
        else: print('invalid')

if __name__=='__main__':
    main()
