import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Вежливый скрипт')
    parser.add_argument('name', help='Имя') 
    parser.add_argument('-s', '--surname', help='Фамилия')    
    args = parser.parse_args()
    parts = [] 
    # Добавляем приветствие по имени.
    parts.append(f'Hello, {args.name}')
    # Если указана фамилия, то она тоже добавляется к выводу.
    if args.surname is not None:
        parts.append(args.surname)
    # Печатаем через пробел все элементы списка parts.
    print(*parts)