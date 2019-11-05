"""""
-------------------------------------------------------------------------------------

User Input and Replace String Template “Hello <<UserName>>, How are you?”

-------------------------------------------------------------------------------------
"""
class StringReplace:
    if __name__ == '__main__':
        s  = "“Hello <<UserName>>, How are you?”"
        print("Enter the name to change : ")
        st = input()
        # using string replace method to replace string
        s = s.replace("<<UserName>>",st)
        print(s)