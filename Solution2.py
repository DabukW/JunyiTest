
# -*- coding: utf-8 -*-



def main():
    user_input = input('請輸入數字 : ')

    try:
        user_input = int(user_input)
        if not user_input > 0:
            raise 'error'
    except:
        print('無效的輸入')
        return
    print('Input:', user_input)
    output = []
    for i in range(1, user_input+1):
        condition = (i % 3 != 0 and i % 5 != 0)
        if condition or i % 15 == 0:
            output.append(i)
    print('Output:', len(output))
    return


if __name__ == "__main__":
    main()