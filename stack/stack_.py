# going to implement the stack by the list or array 
class stack_:
    def __init__(self):
        self.links_ = ['link1','link2','link3','link4',]
        self.stack2 = []
        

    def pop(self):
        val =  self.links_[len(self.links_) - 1]
        del self.links_[len(self.links_) - 1] 
        return val
    
    def push(self, val):
        self.links_.append(val)
        return self.links_[len(self.links_) - 1]
    
    def print(self):
        return self.links_
    
    def is_empty(self):
        return len(self.links_) == 0
    
    def size(self):
        return len(self.links_)
    
    def revers_string(self,word_):
        word_list = list(word_.strip())
        num = len(word_list) - 1
        stri_ = ''
        while num >= 0:
            stri_ += str(word_list[num])
            num -= 1
        return stri_
    
if __name__ == '__main__':
    stack1 = stack_()
    word = 'We will conquere COVI-19'
    word2 = 'I am the king'

    print(stack1.pop())
    print(stack1.pop())
    print(stack1.pop())
    print(stack1.push(20))
    print(stack1.print())
    print(stack1.is_empty())
    print(stack1.size())
    print(stack1.revers_string(word))
    print(stack1.revers_string(word2))





    from collections import deque
    stack = deque()

    # dir(stack) - will show the functions/ methods that we can use to manipulate the stack
    stack.append('link5')
    stack.append('link6')
    stack.append('link7')
    stack.append('link8')
    print(stack)
    print(stack.pop())
    print(stack)

    

