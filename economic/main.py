#본인의 학과에 따른 진로 구분
major_dict={1:'기계공학과',2:'컴퓨터공학과',3:'화학공학과',4:'건축공학과',5:'경영학과',
6:'조경학과'}
major = major_dict[int(input('본인의 학과를 선택하시오. \n (1 : 기계 2 : 컴공 \
3 : 화공\n 4 : 건축 5 : 경영 6 : 조경)'))]
print('전공 : {}'.format(major))
credit = float(input('당신의 학점을 입력하세요.'))
print('학점 : {}'.format(credit))  #상위에 대한 값은 네이버 기준
if major == '기계공학과':
    if credit >= 4.5*85/100:    #상위 15%
        first_salary = 350
    elif credit >= 4.5*69/100:  #상위 31%
        first_salary = 275
    elif credit >= 4.5*49/100:  #상위 51%
        first_salary = 225
    elif credit >= 4.5*28/100:  #상위 72%
        first_salary = 175
    else :                      #그외
        first_salary = 75
elif major == '컴퓨터공학과':
    if credit>=4.5*(90)/100:    #상위 10%
        first_salary = 350
    elif credit>=4.5*(82)/100:  #상위 18%
        first_salary = 275
    elif credit>=4.5*(60)/100:  #상위 40%
        first_salary = 225
    elif credit>=4.5*(11)/100:  #상위 89%
        first_salary = 175
    else :                      #그외
        first_salary = 75
elif major == '화학공학과':
    if credit>=4.5*(88)/100:    #상위 12%
        first_salary = 350
    elif credit>=4.5*(77)/100:  #상위 23%
        first_salary = 275
    elif credit>=4.5*(57)/100:  #상위 43%
        first_salary = 225
    elif credit>=4.5*(27)/100:  #상위 73%
        first_salary = 175
    else :                      #그외
        first_salary = 75
elif major == '건축공학과':
    if credit>=4.5*(99)/100:    #상위 1%
        first_salary = 350
    elif credit>=4.5*(87)/100:  #상위 13%
        first_salary = 275
    elif credit>=4.5*(74)/100:  #상위 26%
        first_salary = 225
    elif credit>=4.5*(29)/100:  #상위 71%
        first_salary = 175
    else :                      #그외
        first_salary = 75
elif major == '경영학과':
    if credit>=4.5*(90)/100:    #상위 10%
        first_salary = 350
    elif credit>=4.5*(82)/100:  #상위 18%
        first_salary = 275
    elif credit>=4.5*(64)/100:  #상위 36%
        first_salary = 225
    elif credit>=4.5*(25)/100:  #상위 75%
        first_salary = 175
    else :                      #그외
        first_salary = 75
elif major == '조경학과':
    if credit>=4.5*(94)/100:    #상위 6%
        first_salary = 350
    elif credit>=4.5*(88)/100:  #상위 12%
        first_salary = 275
    elif credit>=4.5*(66)/100:  #상위 34%
        first_salary = 225
    elif credit>=4.5*(25)/100:  #상위 75%
        first_salary = 175
    else :                      #그외
        first_salary = 75

income=[0,0,0,0,0,0]
for i in range(6):
    income[i]= first_salary*1.276281**i   #연평균 물가상승에 맞춰 5%의 월급 상승 가정

import matplotlib.pyplot as plt

plt.plot([5,10,15,20,25,30],income)
plt.xlabel('x years later')
plt.ylabel('expected salary (10000WON)')
plt.title('top percentage : {:.3f}%'.format(100-credit/4.5*100)) # 학점에 대한 값으로 상위 퍼센트에 대한 값을 구해냄
plt.show()


save_percentage = int(input('당신은 월급의 몇 퍼센트를 저축하시겠습니까? '))/100
save_list=[0,0,0,0,0,0]
save_amount =0
for i in range(1,31):                                                                                   #저축 금리 == 1%
    save_amount+=save_amount*0.01-save_amount*0.01*0.154+first_salary*(1.05)**(i-1)*save_percentage*12  #이자소득 세금 == (원천징수세율+지방소득세율) == 15.4%
    if i%5==0:
        save_list[int(i/5)-1]=save_amount



plt.plot([5,10,15,20,25,30],save_list)
plt.xlabel('x years later')
plt.ylabel('(10000WON)')
plt.title('expected the amount of saving') # 저축에 따른 기댓값
plt.show()


stock_percentage = int(input('당신은 월급의 몇 퍼센트를 주식에 투자하시겠습니까? '))/100
stock_list=[0,0,0,0,0,0]
stock_amount = 0
annual = int(input('당신의 연평균 주식 상승률을 몇 퍼센트로 설정하시겠습니까?'))/100
for i in range(1,31):
    stock_amount+=(annual*(stock_amount)+first_salary*(1.05)**(i-1)*stock_percentage*12)
    if i%5==0:
        stock_list[int(i/5)-1]=stock_amount

plt.plot([5,10,15,20,25,30],stock_list)
plt.xlabel('x years later')
plt.ylabel('(10000WON)')

plt.title('expected the amount of blue-chips investment results\nannual rate of increase : {}%, percentage of salary : {}%'.format(annual*100,stock_percentage*100)) # 한글 패치를 하든지 영어로 바꾸든지 해야됨
plt.show()