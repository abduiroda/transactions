import numpy as np
transactions = np.array([
    [200, 500, -150, 1200, -50],  
    [450, 1200, -100, 800, 50],   
    [300, 700, -200, 0, 10],      
    [800, 120, -250, 300, 200],   
    [500, 250, -400, 1000, -30],  
])

#1. Суммарная транзакция по всем клиентам за каждый день
daily_tran_sum = np.sum(transactions, axis=1)
print("Суммарные транзакции по дням:", daily_tran_sum)

#2. Общая сумма транзакций за все 5 дней
total_tran = np.sum(transactions)
print("Общая сумма транзакций за 5 дней:", total_tran)

#3. Максимальная и минимальная сумма транзакций за весь период
max_tran = np.max(transactions)
min_tran = np.min(transactions)
print("Максимальная транзакция:", max_tran)
print("Минимальная транзакция:", min_tran)

#4. Среднее значение транзакций по каждому клиенту 
avrg_tran_client = np.mean(transactions, axis=0)
print("Среднее значение транзакций по каждому клиенту:", avrg_tran_client)

#5. Сколько раз клиент делал снятие денег 
withdrawal_tran_count = np.sum(transactions < 0, axis=0)
print("Количество снятий для каждого клиента:", withdrawal_tran_count)

#6. Количество дней с положительным балансом
positive_days_count = np.sum(daily_tran_sum > 0)
print("Количество дней с положительным балансом:", positive_days_count)

#7. Клиент, который сделал наибольшие депозиты 
positive_transactions = np.where(transactions > 0, transactions, 0)  
total_positive_per_client = np.sum(positive_transactions, axis=0)
max_deposit_client = np.argmax(total_positive_per_client)
print(f"Клиент с наибольшими депозитами: Клиент {max_deposit_client + 1}")
