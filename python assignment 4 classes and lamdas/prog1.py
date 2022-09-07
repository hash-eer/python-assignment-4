#Write a python class to convert an integer into a roman numeral and viceversa
class inToRoman:
    def int_to_rom(self,num):
        number=[1000, 900, 500, 400,100, 90, 50, 40,10, 9, 5, 4,1]
        roman=["M", "CM", "D", "CD","C", "XC", "L", "XL","X", "IX", "V", "IV","I"]
        i=0
        result=''
        
        while num!=0:
            if number[i]<=num:
                result+=roman[i]
                num = num-number[i]
            else:
                i=i+1
                
        return result
    
            
num=int(input("enter the number to see its roman number:"))
print(inToRoman().int_to_rom(num))