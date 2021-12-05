import os
import click


@click.command()
# @click.option('--all', help='Run all .feature files.')
def all():
    os.system("behave features\contact_us.feature")
    os.system("behave features\invalid_sign_up.feature")
    os.system("behave features\\valid_sign_up.feature")
    os.system("behave features\search.feature")    
    os.system("behave features\prdouct_with_options.feature") 
    os.system("behave features\purchasing_item.feature") 
    

@click.command()
# @click.option('--contact_us', help='Run contact_us.feature file.')
def contact_us():
    os.system("behave features\contact_us.feature")


@click.command()
# @click.option('--invalid_sign_up', help='Run invalid_sign_up.feature file.')
def invalid_sign_up():
    os.system("behave features\invalid_sign_up.feature")


@click.command()
# @click.option('--valid_sign_up', help='Run valid_sign_up.feature file.')
def valid_sign_up():
    os.system("behave features\\valid_sign_up.feature")


@click.command()
# @click.option('--search', help='Run search.feature file.')
def search():
    os.system("behave features\search.feature")    

@click.command()
# @click.option('--prdouct_with_options', help='Run prdouct_with_options.feature file.')
def prdouct_with_options():
    os.system("behave features\prdouct_with_options.feature")    


@click.command()
# @click.option('--purchasing_item', help='Run purchasing_item.feature file.')
def purchasing_item():
    os.system("behave features\purchasing_item.feature")    



@click.group()
def main():
    pass


main.add_command(all)
main.add_command(contact_us)
main.add_command(invalid_sign_up)
main.add_command(valid_sign_up)
main.add_command(search)
main.add_command(prdouct_with_options)
main.add_command(purchasing_item)

if __name__ == "__main__":
    main()
