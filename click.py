import click

@click.command()
@click.option('--user_name', default=find_cookie(), prompt='Profile', help='User name')
def main(user_name):
	table_users = User()
	cur_user = table_users.query.filter(User.user==user_name).first()