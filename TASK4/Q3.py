#Add some records in the list and print the list in tabular form,
import pandas as pd

q = [ [1, "ajay", 95],
     [2, "sanjay", 88],
     [3, "vijay", 90]]

qf = pd.DataFrame(q, columns = ['roll_no','name','mark'])
print(qf)
#From created list, extract and print second record/row that contains
print(qf[1:2])