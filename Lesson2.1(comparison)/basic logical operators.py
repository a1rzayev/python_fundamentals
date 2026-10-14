age = 16
has_ticket = True
is_vip = True

can_enter = (age >= 18 and has_ticket) or is_vip
print(can_enter)

# student can apply to university if he is at least 16 years old,
# and passed 550 points our of 700 in DIM, or passed Sat for at least 1200
# and ielts 6.5

dim = 550
sat = 1200
ielts = 6.5

can_apply = (age >= 16 and dim >= 550) or (sat >= 1200 and ielts >= 6.5)

can_apply2 = age >= 16 and (dim >= 550 or (sat >= 1200 and ielts >= 6.5)) 




 