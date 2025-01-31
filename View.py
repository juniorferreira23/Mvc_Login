from Controller import UserController

def run_system() -> None:
    controller = UserController()
    while True:
        print(
            '\n[1] Login\n'
            '[2] Register\n'        )
        option = input('Select option: ')
        if not option:
            continue
        elif option.isdigit():
            option = int(option)
        match option:
            case 1:
                username = input('Enter Username (E-mail): ')
                password = input('Enter Password: ')
                response = controller.login(username, password)
                print(response)
            case 2:                
                username = input('Enter Username (E-mail): ')
                password = input('Enter Password: ')
                re_password = input('Repeat Password: ')
                response = controller.register_user(username, password, re_password)
                print(response)
            case _:
                continue
            
if __name__ == '__main__':
    run_system()