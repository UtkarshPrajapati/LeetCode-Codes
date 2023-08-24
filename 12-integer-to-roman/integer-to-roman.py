class Solution:
    def intToRoman(self,num):
        return ["","M","MM","MMM"][num//1000]+["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"][(num%1000)//100]+["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"][(num%100)//10]+["","I","II","III","IV","V","VI","VII","VIII","IX"][num%10]   