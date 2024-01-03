#https://leetcode.com/problems/reverse-words-in-a-string/description/

def reverseWords(self, s):
    #removing the space from front and back 
    s = s.strip()

    #spliting the string into list " "
    str_list = s.split(" ")
    
    #removing the space from front and back os each string 
    new_str =[item.strip() for item in str_list]

    # removing the empty string from the list 
    new_str = [item for item in new_str if item !=""]

    #reversing the list 
    new_str.reverse()
    print(new_str)
    return " ".join(new_str)

ans = reverseWords("the sky is blue")