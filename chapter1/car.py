машин = 100
проц = 4
водителей = 30
пассажиров = 90
не_рабочие_машины = машин - водителей
рабочие_машины = водителей
всего = не_рабочие_машины * проц
кол = пассажиров / рабочие_машины


print ("В наличии", машин, "автомобилей.")
print ("И только", водителей, "водителей вышли на работу.")
print ("Получается, что", не_рабочие_машины, "машин пустуют." )
print ("Мы можем перевезти сегодня", всего, "человек.")
print ("Сегодня нужно отвезти", пассажиров, "человек.")
print ("В каждой машине будет примерно", кол, "человек.")