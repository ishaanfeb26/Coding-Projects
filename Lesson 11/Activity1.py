total_chores=4
original_count=total_chores
print(f"You have {original_count} chores to finish today!\n")


completed_count=0
chore_num=1


while chore_num<=total_chores:

  if chore_num==1:   next_chore="Make your bed"

  elif chore_num==2: next_chore="Feed the pet"

  elif chore_num==3: next_chore="Take out the trash"

  else: next_chore="Do the dishes"

  answer=input(f"Have you finished {next_chore}? (Y/N): ")

  if answer=='Y':
    completed_count+=1
    chore_num+=1
    print(f"Good job! You have completed {completed_count} chores so far.")
  else:
    print("Okay, finish it, and check again")


  print(f"Chores remaining: {total_chores - completed_count}")
  print()


  print("======== ALL CHORES COMPLETED ========")

          