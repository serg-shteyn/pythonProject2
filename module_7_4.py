team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = score_1+score_2
time_avg = round(((team1_time+team2_time)/tasks_total),2)


if score_1>score_2 and team1_time<team2_time:
	challenge_result = 'Победа команды Волшебники данных!'
elif score_2>score_1 and team2_time<team1_time:
	challenge_result = 'Победа команды Мастера кода!'	
else:
	challenge_result = 'Ничья!'	
	

# Использование %
print("В команде Мастера кода участников: %d! " % team1_num)
print("Итого сегодня в командах участников: %d и %d !"% (team1_num,team2_num))

# Использование format()

print("Команда Волшебники данных решила задач: {} !".format(score_2))
print("Волшебники данных решили задачи за {} с !".format(team2_time))

#Использование f-строк:
print(f"Команды решили {score_1} и {score_2} задач.")
print(f"Результат битвы: {challenge_result}")
print(f"Сегодня было решено {tasks_total} задач, в среднем по  {time_avg} секунды на задачу!.")

