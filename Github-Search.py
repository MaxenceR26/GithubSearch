from os import system
import requests
from treelib import Tree
from pystyle import Colors, Colorate
from pycenter import center

# By Kijusu / Maxence R <3


class gitsearch:
    def __init__(self):
        system("cls")
        self.title = """

  ▄▀  ▄█    ▄▄▄▄▀  ▄  █   ▄   ███          ▄▄▄▄▄   ▄███▄   ██   █▄▄▄▄ ▄█▄     ▄  █ 
▄▀    ██ ▀▀▀ █    █   █    █  █  █        █     ▀▄ █▀   ▀  █ █  █  ▄▀ █▀ ▀▄  █   █ 
█ ▀▄  ██     █    ██▀▀█ █   █ █ ▀ ▄     ▄  ▀▀▀▀▄   ██▄▄    █▄▄█ █▀▀▌  █   ▀  ██▀▀█ 
█   █ ▐█    █     █   █ █   █ █  ▄▀      ▀▄▄▄▄▀    █▄   ▄▀ █  █ █  █  █▄  ▄▀ █   █ 
 ███   ▐   ▀         █  █▄ ▄█ ███                  ▀███▀      █   █   ▀███▀     █  
                    ▀    ▀▀▀                                 █   ▀             ▀   
                                                            ▀                      
                                By Kijusu / Maxence

        """

        print(Colorate.Horizontal(Colors.yellow_to_green, center(self.title)))

        self.name = input(Colorate.Horizontal(Colors.yellow_to_green, "Username -> "))
        self.request = requests.get(f"https://api.github.com/users/{self.name}")
        self.Data = self.request.json()

        self.tree = Tree()
        self.treeEmails = Tree()
        self.treeUrl = Tree()
        self.treeBlogAndNetworks = Tree()
        self.treeGithubInfo = Tree()
        self.treeOther = Tree()

    def recoverData(self):
        self.tree.create_node(f"\n{Colorate.Color(Colors.yellow, self.name)}", "user")
        self.tree.create_node(f"{Colorate.Horizontal(Colors.yellow_to_green, 'Informations personnels')}",
                              "informations", parent="user")
        self.tree.create_node(f"Name : {self.Data['name']}", parent="informations")
        self.tree.create_node(f"Id : {self.Data['id']}", parent="informations")
        self.tree.create_node(f"Node Id : {self.Data['node_id']}", parent="informations")
        self.tree.create_node(f"Type : {self.Data['type']}", parent="informations")
        self.tree.create_node(f"Company : {self.Data['company']}", parent="informations")
        self.tree.create_node(f"Location : {self.Data['location']}", "treemail", parent="informations")

        self.treeEmails.create_node(f"{Colorate.Horizontal(Colors.yellow_to_green, 'Email(s)')}", 'emails')
        self.treeEmails.create_node(f"Email(s) : {self.Data['email']}", parent="emails")

        self.treeUrl.create_node(f"{Colorate.Horizontal(Colors.yellow_to_green, 'Urls Accounts')}", "url")
        self.treeUrl.create_node(f"Avatar url : {self.Data['avatar_url']}", parent="url")
        self.treeUrl.create_node(f"Followers url : {self.Data['followers_url']}", parent="url")
        self.treeUrl.create_node(f"Subscriptions url : {self.Data['subscriptions_url']}", parent="url")
        self.treeUrl.create_node(f"Organizations url : {self.Data['organizations_url']}", parent="url")
        self.treeUrl.create_node(f"Repos url : {self.Data['repos_url']}", parent="url")
        self.treeUrl.create_node(f"Received events url : {self.Data['received_events_url']}", parent="url")

        self.treeBlogAndNetworks.create_node(f"{Colorate.Horizontal(Colors.yellow_to_green, 'Blog and Networks')}", 1)
        self.treeBlogAndNetworks.create_node(f"Twitter : {self.Data['twitter_username']}", parent=1)
        self.treeBlogAndNetworks.create_node(f"Blog : {self.Data['blog']}", parent=1)

        self.treeGithubInfo.create_node(f"{Colorate.Horizontal(Colors.yellow_to_green, 'Github account informations')}",
                                        2)
        self.treeGithubInfo.create_node(f"Public repository : {self.Data['public_repos']}", parent=2)
        self.treeGithubInfo.create_node(f"Public gists: {self.Data['public_gists']}", parent=2)
        self.treeGithubInfo.create_node(f"Followers: {self.Data['followers']}", parent=2)
        self.treeGithubInfo.create_node(f"Following: {self.Data['following']}", parent=2)
        self.treeGithubInfo.create_node(f"Account created at: {self.Data['created_at']}", parent=2)
        self.treeGithubInfo.create_node(f"Last update: {self.Data['updated_at']}", parent=2)

        self.tree.paste('user', self.treeEmails)
        self.tree.paste('user', self.treeUrl)
        self.tree.paste('user', self.treeBlogAndNetworks)
        self.tree.paste('user', self.treeGithubInfo)
        self.tree.show(line_type="ascii-em")


gitsearch().recoverData()
