import os
import csv

# Location of election_data.csv:
PyPoll = os.path.join ('Resources', 'election_data.csv')

# Reading the csv file:
with open (PyPoll,'r',newline='') as votes:
  votes_reader = csv.reader (votes,delimiter=',')
  header = next(votes_reader)


  total = 0
  candidate_list = []
  unique_list=[]
  votes = 0
  no_votes=[]

  for row in votes_reader:

  #Calculating the Total Number of Votes:
    total+= 1

  #Creating a list of all candidate with duplicates:
    candidate_list.append(row[2])

  #Printing Election Results:
  print ("Election Results")
  print ("-----------------------------")

  #Printing Total Votes:
  print (f"Total Votes: {total}")
  print ("-----------------------------")

  #Creating a list of unique candidates:
  for unique in candidate_list:
    if unique not in unique_list:
      unique_list.append(unique)

  #Calculating Each Candidates Number of Votes:
  for candidate in unique_list:
    no_votes.append(candidate_list.count(candidate))
    #no_votes.append(round(((candidate_list.count(candidate)/total)*100),3))
    print(f"{candidate}:{round(((candidate_list.count(candidate)/total)*100),3)} % ({candidate_list.count(candidate)})")

  # Finding the Winner:
    if (candidate_list.count(candidate)) > votes:
      votes = (candidate_list.count(candidate))
      winner = candidate


  print ("-----------------------------")
  # Printing the Winner:
  print (f"Winner: {winner}")
  print ("-----------------------------")


# Location of PyPollExport.txt:
result = os.path.join ('PyPollExport.txt')

# Writing the output txt file:
with open (result,'w') as output:

  output.write("Election Results\n")
  output.write("-----------------------------\n")
  output.write(f"Total Votes: {total}\n")
  output.write("-----------------------------\n")

  for x in range(len(unique_list)):
    output.write(f"{unique_list[x]}: {round(((no_votes[x]/total)*100),3)}% ({no_votes[x]})\n")

  output.write("-----------------------------\n")
  output.write(f"Winner: {winner}\n")
  output.write("-----------------------------\n")
