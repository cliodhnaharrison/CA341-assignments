#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random


class Node:
    def __init__(self, name, phone, address):
        """
        Initialises Node object with name, phone number and address attributes.
        Sets left and right children to None.
        """
        self.name = name
        self.phone = phone
        self.address = address
        self.left = None
        self.right = None


    def __str__(self):
        """
        Compiles a message of the name, phone number and address for a Node.
        """
        message = ""
        message += f"Name: {self.name}\n"
        message += f"Phone Number: {self.phone}\n"
        message += f"Address: {self.address}\n"
        return message


class NameTree:
    def __init__(self):
        """
        Initialises NameTree object with root as None.
        """
        self.root = None


    def set_root(self, name, phone, address):
        """
        Creates Node with given parameters and sets it as root.

        Args:
            name: string of name to be inserted
            phone: string of phone to be inserted
            address: string of address to be inserted
        """
        self.root = Node(name, phone, address)


    def insert(self, name, phone, address):
        """
        Creates node and inserts into NameTree. If the tree has no root then
        it is set to the created node, otherwise the params are passed to insert_node.

        Args:
            name: string of name to be inserted
            phone: string of phone to be inserted
            address: string of address to be inserted
        """
        if self.root:
            self.insert_node(self.root, name, phone, address)
        else:
            self.set_root(name, phone, address)


    def insert_node(self, curr, name, phone, address):
        """
        Checks if the given name is before or after the current node's name.

        If the given name is before the current name and the current node doesn't
        have a left child then a node with the given parameters is inserted
        there. If there is a left child then the parameters and the left child
        are passed to the function recursively.

        If the given name is after the current name and the current node doesn't
        have a right child then a node with the given parameters is inserted there.
        If there is a right child then the parameters and the right child are
        passed to the function recursively.

        Args:
            curr: Node object, current node to be checked for the insertion of
                  new node.
            name: string of name to be inserted
            phone: string of phone to be inserted
            address: string of address to be inserted
        """

        if name > curr.name:
            if curr.right:
                self.insert_node(curr.right, name, phone, address)
            else:
                curr.right = Node(name, phone, address)
        else:
            if curr.left:
                self.insert_node(curr.left, name, phone, address)
            else:
                curr.left = Node(name, phone, address)


    def find(self, name, curr=None):
        """
        Recursively searches for a match in the tree for the given name. If a current
        node to search from isn't passed then it is set to the root.

        Args:
            value: a string name

        Returns:
            curr: the Node that the name matches the value
        """
        if not curr:
            curr = self.root

        if curr.name == name:
            return curr
        elif name > curr.name:
            if curr.right:
                return self.find(name, curr.right)
            else:
                return None
        else:
            if curr.left:
                return self.find(name, curr.left)
            else:
                return None


    def remove(self, name):
        """
        Function to remove the node with the given phone number if it exists.

        Args:
            name: string of name to delete

        Returns:
            bool: True if node was deleted, False if not
        """
        if not self.root:
            return False
        elif self.root.name == name:
            if not self.root.left and not self.root.right:
                self.root = None
            elif self.root.left and not self.root.right:
                self.root = self.root.left
            elif self.root.right and not self.root.left:
                self.root = self.root.right
            else:
                del_parent = self.root
                del_node = self.root.right
                while del_node.left:
                    del_parent = del_node
                    del_node = del_node.left

                self.root.name = del_node.name
                self.root.phone = del_node.phone
                self.root.address = del_node.address

                if del_node.right:
                    if del_parent.name > del_node.name:
                        del_parent.left = del_node.right
                    else:
                        del_parent.right = del_node.right
                else:
                    if del_node.name < del_parent.name:
                        del_parent.left = None
                    else:
                        del_parent.right = None
            return True

        parent = None
        node = self.root

        while node and node.name != name:
            parent = node
            if name < node.name:
                node = node.left
            elif name > node.name:
                node = node.right

        if not node or node.name != name:
            return False

        elif not node.left and not node.right:
            if name < parent.name:
                parent.left = None
            else:
                parent.right = None
            return True

        elif node.left and not node.right:
            if name < parent.name:
                parent.left = node.left
            else:
                parent.right = node.left
            return True

        elif not node.left and node.right:
            if name < parent.name:
                parent.left = node.right
            else:
                parent.right = node.right
            return True

        else:
            del_parent = node
            del_node = node.right
            while del_node.left:
                del_parent = del_node
                del_node = del_node.left

            node.name = del_node.name
            node.phone = del_node.phone
            node.address = del_node.address

            if del_node.right:
                if del_parent.name > del_node.name:
                    del_parent.left = del_node.right
                elif del_parent.name < del_node.name:
                    del_parent.right = del_node.right
            else:
                if del_node.name < del_parent.name:
                    del_parent.left = None
                else:
                    del_parent.right = None

            return True


    def traverse(self, curr):
        """
        Traverses the tree in order and prints each node as it goes.
        """
        if curr:
            self.traverse(curr.left)
            print (curr)
            self.traverse(curr.right)


class PhoneTree:
    def __init__(self):
        """
        Initialises PhoneTree object with root as None.
        """
        self.root = None


    def set_root(self, name, phone, address):
        """
        Creates Node with given parameters and sets it as root.

        Args:
            name: string of name to be inserted
            phone: string of phone to be inserted
            address: string of address to be inserted
        """
        self.root = Node(name, phone, address)


    def insert(self, name, phone, address):
        """
        Creates node and inserts into PhoneTree. If the tree has no root then
        it is set to the created node, otherwise the params are passed to insert_node.

        Args:
            name: string of name to be inserted
            phone: string of phone to be inserted
            address: string of address to be inserted
        """
        if self.root:
            self.insert_node(self.root, name, phone, address)
        else:
            self.set_root(name, phone, address)


    def insert_node(self, curr, name, phone, address):
        """
        Checks if the given phone number is before or after the current node's
        phone number.

        If the given phone is before the current phone and the current node doesn't
        have a left child then a node with the given parameters is inserted
        there. If there is a left child then the parameters and the left child
        are passed to the function recursively.

        If the given phone is after the current phone and the current node doesn't
        have a right child then a node with the given parameters is inserted there.
        If there is a right child then the parameters and the right child are
        passed to the function recursively.

        Args:
            curr: Node object, current node to be checked for the insertion of
                  new node.
            name: string of name to be inserted
            phone: string of phone to be inserted
            address: string of address to be inserted
        """
        if phone > curr.phone:
            if curr.right:
                self.insert_node(curr.right, name, phone, address)
            else:
                curr.right = Node(name, phone, address)
        else:
            if curr.left:
                self.insert_node(curr.left, name, phone, address)
            else:
                curr.left = Node(name, phone, address)


    def find(self, phone, curr=None):
        """
        Recursively searches for a match in the tree for the given phone number.
        If a current node to search from isn't passed then it is set to the root.

        Args:
            value: a string phone number

        Returns:
            curr: the Node that the phone number matches the value
        """
        if not curr:
            curr = self.root

        if curr.phone == phone:
            return curr
        elif phone > curr.phone:
            if curr.right:
                return self.find(phone, curr.right)
            else:
                return None
        else:
            if curr.left:
                return self.find(phone, curr.left)
            else:
                return None


    def remove(self, phone):
        """
        Function to remove the node with the given phone number if it exists.

        Args:
            phone: string of phone number to delete

        Returns:
            bool: True if node was deleted, False if not
        """
        if not self.root:
            return False
        elif self.root.phone == phone:
            if not self.root.left and not self.root.right:
                self.root = None
            elif self.root.left and not self.root.right:
                self.root = self.root.left
            elif self.root.right and not self.root.left:
                self.root = self.root.right
            else:
                del_parent = self.root
                del_node = self.root.right
                while del_node.left:
                    del_parent = del_node
                    del_node = del_node.left

                self.root.name = del_node.name
                self.root.phone = del_node.phone
                self.root.address = del_node.address

                if del_node.right:
                    if del_parent.phone > del_node.phone:
                        del_parent.left = del_node.right
                    else:
                        del_parent.right = del_node.right
                else:
                    if del_node.phone < del_parent.phone:
                        del_parent.left = None
                    else:
                        del_parent.right = None
            return True

        parent = None
        node = self.root

        while node and node.phone != phone:
            parent = node
            if phone < node.phone:
                node = node.left
            elif phone > node.phone:
                node = node.right

        if not node or node.phone != phone:
            return False

        elif not node.left and not node.right:
            if phone < parent.phone:
                parent.left = None
            else:
                parent.right = None
            return True

        elif node.left and not node.right:
            if phone < parent.phone:
                parent.left = node.left
            else:
                parent.right = node.left
            return True

        elif not node.left and node.right:
            if phone < parent.phone:
                parent.left = node.right
            else:
                parent.right = node.right
            return True

        else:
            del_parent = node
            del_node = node.right
            while del_node.left:
                del_parent = del_node
                del_node = del_node.left

            node.name = del_node.name
            node.phone = del_node.phone
            node.address = del_node.address

            if del_node.right:
                if del_parent.phone > del_node.phone:
                    del_parent.left = del_node.right
                elif del_parent.phone < del_node.phone:
                    del_parent.right = del_node.right
            else:
                if del_node.phone < del_parent.phone:
                    del_parent.left = None
                else:
                    del_parent.right = None

            return True

    def traverse(self, curr):
        if curr:
            self.traverse(curr.left)
            print (curr)
            self.traverse(curr.right)


def random_phone():
    """
    Helper function that uses random choices to create a valid Irish phone number.

    Returns:
        string: random valid Irish phone number
    """
    prefix = "08" + "".join([str(x) for x in random.choices(range(5,10), k=1)])
    return prefix + "".join([str(x) for x in random.choices(range(0,10), k=7)])


def main():
    """
    Function that tests the functionality of the Node, PhoneTree and NameTree classes.
    """
    # Test data
    names = ["Cliodhna", "Zach", "Cory", "Betty", "Abraham", "Jordan", "Mary", "Joseph", "Zed"]
    phones = ["0855881892", "0884624315", "0850602678", "0868026665", "0887178084", "0858573472", "0856776227", "0873787608", "0890402726"]
    addresses = ["Apt 1", "Apt 2", "Apt 3", "Apt 4","Apt 5", "Apt 6", "Apt 7", "Apt 8", "Apt 9"]
    phone_tree = PhoneTree()
    name_tree = NameTree()


    # Demonstrates the insert function of both Tree classes
    for i in range(len(names)):
        name_tree.insert(names[i], phones[i], addresses[i])
        phone_tree.insert(names[i], phones[i], addresses[i])

    # Demonstrates the find functionality
    print(name_tree.find("Joseph"))
    print ("-----------------")
    print(phone_tree.find("0850602678"))
    print ("-----------------")

    # Demonstrates the remove functionality
    name_tree.remove("Joseph")
    name_tree.traverse(name_tree.root)
    print ("-----------------")
    phone_tree.remove("0850602678")
    phone_tree.traverse(phone_tree.root)

if __name__ == "__main__":
    main()
