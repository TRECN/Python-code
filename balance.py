balance = int(input());
gender = input();
bonus=0;
if(balance<5000):
    bonus=balance*0.02;
elif(gender =='female' and balance>5000):
    bonus=balance*0.05;

print(balance+bonus);