per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float(input("Введите сумму планируемого пополнения:"))
tkb = per_cent['ТКБ']*money/100 #думаю можно обратиться ко всем объектам словаря, но я пока еще думаю, как лучше
skb = per_cent['СКБ']*money/100
vtb = per_cent['ВТБ']*money/100
sber = per_cent['СБЕР']*money/100
depozit = [tkb, skb, vtb, sber]
max_dep = round(max(depozit))
itogo = (list(map(round, depozit)))
print (itogo, '\n' 'Максимальная сумма, которую вы можете заработать:', max_dep)