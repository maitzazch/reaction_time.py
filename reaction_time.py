import time
import random

print("Нажмите Enter, когда увидите движущийся объект.")
time.sleep(random.randint(2, 5))
start_time = time.time()

input()

end_time = time.time()

reaction_time = end_time - start_time

print("Ваше время реакции: ", round(reaction_time, 2), "секунд.")
